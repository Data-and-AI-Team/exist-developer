"""Publish engineering or AI drafts; requires requests, PyYAML, Markdown."""

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re

import markdown
import requests
import yaml


ROOT = Path(__file__).resolve().parent
BASE = "https://kb.exist.com"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--publish", action="store_true", required=True)
    parser.add_argument("--space", choices=["EPAI", "AI"], default="EPAI")
    args = parser.parse_args()
    SPACE = args.space
    is_ai = SPACE == "AI"
    content_directory = "ai-initiative" if is_ai else "engineering-process"
    MANIFEST = ROOT / ("publication-ai.json" if is_ai else "publication-engineering.json")
    secret = yaml.safe_load((ROOT / "secrets.yml").read_text())
    session = requests.Session()
    session.headers.update({
        "Authorization": "Bearer " + secret["CONFLUENCE_PERSONAL_TOKEN"],
        "Accept": "application/json",
    })

    def api(method, path, **kwargs):
        response = session.request(method, BASE + path, timeout=60, **kwargs)
        response.raise_for_status()
        return response.json()

    space = api("GET", f"/rest/api/space/{SPACE}?expand=homepage")
    home_id = space["homepage"]["id"]
    home = api("GET", f"/rest/api/content/{home_id}?expand=body.storage,version,space,ancestors")

    manifest = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {
        "base_url": BASE, "space_key": SPACE, "pages": {}
    }
    if manifest["space_key"] != SPACE or manifest["base_url"] != BASE:
        raise RuntimeError("Manifest target does not match publication target")

    def save():
        MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n")

    pages = []
    for source in sorted((ROOT / "contents" / content_directory).glob("*.md")):
        text = source.read_text()
        title, body = text.split("\n", 1)
        pages.append((source, title.removeprefix("# "), body))
    if not pages or pages[0][0].name != "00-home.md":
        raise RuntimeError("Expected a home page followed by procedure pages")

    existing = []
    path = f"/rest/api/content?spaceKey={SPACE}&type=page&limit=100"
    while path:
        data = api("GET", path)
        existing.extend(data["results"])
        path = data.get("_links", {}).get("next")
    by_title = {p["title"]: p for p in existing}

    # Reserve IDs before rendering so all links use verified page IDs.
    for index, (source, title, body) in enumerate(pages):
        key = str(source.relative_to(ROOT))
        if key in manifest["pages"]:
            continue
        if index == 0:
            page = home
        else:
            if title in by_title:
                raise RuntimeError(f"Unmapped page already exists: {title}; reconcile before publishing")
            page = api("POST", "/rest/api/content", json={
                "type": "page", "title": title, "space": {"key": SPACE},
                "ancestors": [{"id": home_id}],
                "body": {"storage": {"value": "<p>Draft for review. Publication in progress.</p>", "representation": "storage"}},
            })
        manifest["pages"][key] = {
            "page_id": page["id"], "title": page["title"],
            "parent_page_id": None if index == 0 else home_id,
            "version": page["version"]["number"],
        }
        save()

    link_pages = {}
    for published_manifest in ROOT.glob("publication-*.json"):
        published = json.loads(published_manifest.read_text())
        if published.get("base_url") == BASE:
            link_pages.update(published.get("pages", {}))
    link_pages.update(manifest["pages"])

    for index, (source, title, body) in enumerate(pages):
        key = str(source.relative_to(ROOT))
        record = manifest["pages"][key]

        def link(match):
            label, target = match.groups()
            if "://" in target or target.startswith("#"):
                return match.group(0)
            resolved = (source.parent / target).resolve().relative_to(ROOT)
            destination = link_pages[str(resolved)]
            return f"[{label}]({BASE}/pages/viewpage.action?pageId={destination['page_id']})"

        linked_body = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link, body)
        html = markdown.markdown(linked_body, extensions=["tables", "fenced_code"])
        if index:
            html = '<ac:structured-macro ac:name="toc" ac:schema-version="1" />' + html
        digest = hashlib.sha256(source.read_bytes()).hexdigest()
        current = api("GET", f"/rest/api/content/{record['page_id']}?expand=version,space,ancestors,body.storage")
        if current["space"]["key"] != SPACE:
            raise RuntimeError("Mapped page is outside the target space")
        if current["version"]["number"] != record["version"]:
            raise RuntimeError(f"Concurrent edit detected: {current['title']}")
        if record.get("source_sha256") != digest or current["body"]["storage"]["value"] != html:
            payload = {
                "id": record["page_id"], "type": "page",
                "title": home["title"] if index == 0 else title,
                "version": {"number": record["version"] + 1, "message": f"Publish {content_directory} draft"},
                "body": {"storage": {"value": html, "representation": "storage"}},
            }
            if index:
                payload["ancestors"] = [{"id": home_id}]
            updated = api("PUT", f"/rest/api/content/{record['page_id']}", json=payload)
            record.update(title=updated["title"], version=updated["version"]["number"], source_sha256=digest)
            save()
        api("POST", f"/rest/api/content/{record['page_id']}/label", json=[
            {"prefix": "global", "name": content_directory},
            {"prefix": "global", "name": "draft"},
        ])
        verified = api("GET", f"/rest/api/content/{record['page_id']}?expand=body.storage,ancestors,space,version,metadata.labels")
        value = verified["body"]["storage"]["value"]
        assert "Draft for review" in value
        assert ".md)" not in value and 'href="0' not in value
        assert verified["space"]["key"] == SPACE
        assert verified["version"]["number"] == record["version"]
        assert {"draft", content_directory}.issubset({label["name"] for label in verified["metadata"]["labels"]["results"]})
        if index:
            assert verified["ancestors"][-1]["id"] == home_id
        else:
            for other in list(manifest["pages"].values())[1:]:
                assert f"pageId={other['page_id']}" in value
        record["url"] = f"{BASE}/pages/viewpage.action?pageId={record['page_id']}"
        save()
        print(f"Verified: {record['title']} — {record['url']}", flush=True)
    manifest["verified_at"] = datetime.now(timezone.utc).isoformat()
    save()
    print(f"Published and verified {len(pages)} pages in {SPACE}.")


if __name__ == "__main__":
    main()
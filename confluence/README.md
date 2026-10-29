# Confluence content and publishing

Markdown sources for two spaces on https://kb.exist.com (Confluence Data Center 9.2.3), plus the tooling that publishes them.

| Space name | Key | Home page | Source directory | Pages |
| --- | --- | --- | --- | --- |
| Engineering Procedures and AI Initiative | `EPAI` | [Engineering Procedures](https://kb.exist.com/pages/viewpage.action?pageId=236257361) | [contents/engineering-process](contents/engineering-process) | 14 |
| AI Initiatives | `AI` | [AI Initiatives](https://kb.exist.com/pages/viewpage.action?pageId=236257366) | [contents/ai-initiative](contents/ai-initiative) | 11 |

Each space has one home page (`00-home.md`) holding the table of contents, with every other page as its direct child.

## Layout

| Path | Purpose |
| --- | --- |
| `contents/README.md` | Inventory of source files and Confluence titles |
| `contents/<section>/NN-name.md` | One Confluence page per file; the numeric prefix sets publication order |
| `publish_engineering.py` | Publisher for both spaces |
| `publication-engineering.json`, `publication-ai.json` | Manifests mapping each source file to its page ID, parent, version, and source hash |
| `mcp_launcher.py` | Starts the Confluence MCP server using the local credentials file |
| `secrets.yml` | Local credentials; ignored by Git |
| `Plan.md` | Publication plan and acceptance criteria |

## Credentials

Create a personal access token in Confluence under **Profile > Personal Access Tokens**, then store it in `secrets.yml`:

```yaml
CONFLUENCE_PERSONAL_TOKEN: "<token>"
```

`secrets.yml` is listed in `.gitignore`. The publisher and the MCP launcher both read it. The token acts with the permissions of its owner, so the owner needs permission to create and edit pages in the target space.

## Publishing

Run from this directory. `uvx` supplies `requests`, `PyYAML`, and `Markdown` through the pinned `mcp-atlassian` package.

```bash
uvx --from 'mcp-atlassian==0.23.1' python publish_engineering.py --publish --space EPAI
uvx --from 'mcp-atlassian==0.23.1' python publish_engineering.py --publish --space AI
```

`--space` accepts `EPAI` (default) or `AI`; `--publish` is required.

If `uvx` is not on `PATH`, use `$HOME/.local/share/uv-bootstrap/bin/uvx`.

### What the publisher does

1. Reads the space home page ID from Confluence and loads the space's manifest.
2. Creates any page missing from the manifest as a child of the home page. An existing page with the same title that is not in the manifest stops the run so it can be reconciled by hand.
3. Converts each Markdown file to Confluence storage format. Relative links become links to the target page ID, resolved across both manifests, so the AI pages can link to engineering pages. Child pages get a table-of-contents macro.
4. Updates a page only when its source hash or rendered body differs from what is published. The home page keeps its existing Confluence title.
5. Stops without writing if a page's Confluence version differs from the manifest, which indicates an edit made in Confluence.
6. Applies labels: the section label (`engineering-process` or `ai-initiative`) and a lifecycle label (`approved` or `draft`), removing the opposite lifecycle label.
7. Reads every page back and checks status text, links, space, parent, version, and labels. Verified URLs and a `verified_at` timestamp are written to the manifest.

Runs are repeatable; unchanged pages are not rewritten.

### Source file requirements

- The first line is `# <Page title>`.
- A line `**Status:** Approved` or `**Status:** Draft for review` is required. It determines the lifecycle label.
- Links to other pages use relative Markdown paths, for example `[Title](02-pull-requests-and-code-review.md)` or `[Title](../engineering-process/09-architecture-and-design.md)`.
- Each section's `00-home.md` must exist and sorts first.

### Adding a page

1. Create `contents/<section>/NN-name.md` with the next number.
2. Add it to the table of contents in that section's `00-home.md` and to `contents/README.md`.
3. Run the publisher for that space.

## MCP server

`mcp_launcher.py` starts `mcp-atlassian` 0.23.1 against https://kb.exist.com with write operations enabled, and sets `CONFLUENCE_SSL_VERIFY=true`. The VS Code workspace registers it as `exist-confluence` in `.vscode/mcp.json`:

```json
{
  "servers": {
    "exist-confluence": {
      "type": "stdio",
      "command": "<path to uvx>",
      "args": ["--from", "mcp-atlassian==0.23.1", "python", "${workspaceFolder}/exist-developer/confluence/mcp_launcher.py"]
    }
  }
}
```

Restart the server in VS Code after changing the launcher or `secrets.yml`.

## Constraints

- Creating spaces requires the Confluence **Create Space** global permission; spaces are provisioned by an administrator.
- Pages are published through the REST API with the token owner's permissions. Page history in Confluence records the token owner as the author.

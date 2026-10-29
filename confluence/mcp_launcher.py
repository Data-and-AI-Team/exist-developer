"""Launch the MCP server using local, ignored credentials."""

import os
from pathlib import Path
import sys

import yaml


def main():
    secrets_path = Path(__file__).with_name("secrets.yml")
    with secrets_path.open(encoding="utf-8") as stream:
        secrets = yaml.safe_load(stream)
    token = (
        secrets.get("CONFLUENCE_PERSONAL_TOKEN")
        if isinstance(secrets, dict)
        else None
    )
    if not isinstance(token, str) or not token.strip():
        raise SystemExit(
            "Set CONFLUENCE_PERSONAL_TOKEN in confluence/secrets.yml before starting MCP."
        )
    os.environ["CONFLUENCE_PERSONAL_TOKEN"] = token.strip()
    os.environ["CONFLUENCE_URL"] = "https://kb.exist.com"
    os.environ["CONFLUENCE_SSL_VERIFY"] = "true"
    os.environ["READ_ONLY_MODE"] = "false"
    executable = str(Path(sys.executable).with_name("mcp-atlassian"))
    os.execv(executable, [executable])


if __name__ == "__main__":
    main()
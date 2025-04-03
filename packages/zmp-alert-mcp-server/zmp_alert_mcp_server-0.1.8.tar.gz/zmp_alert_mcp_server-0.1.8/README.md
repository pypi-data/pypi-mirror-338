# How to run
## sse
```bash
zmp-alert-mcp-server -e https://api.ags.cloudzcp.net -p 8888 -s zmp-f9aed626-c0d6-4293-8a66-c36755e8e948 --transport sse
```

## stdio
first install the zmp-alert-mcp-server
```bash
pip install zmp-alert-mcp-server
```

then configure the mcp server into the mcp host like claude desktop or cursor
```json
{
  "mcpServers": {
    "zmp-alert-mcp": {
      "command": "python3",
      "args": [
        "-m",
        "zmp_alert_mcp_server",
        "--transport",
        "stdio",
        "--endpoint",
        "https://api.ags.cloudzcp.net",
        "--access-key",
        "zmp-f9aed626-c0d6-4293-8a66-c36755e8e948"
      ]
    }
  }
}

```

```json
{
    "mcpServers": {
      "github": {
        "command": "npx",
        "args": [
          "-y",
          "@modelcontextprotocol/server-github"
        ],
        "env": {
          "GITHUB_PERSONAL_ACCESS_TOKEN": "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"
        }
      },
      "zmp-alert-mcp-server": {
        "transport": "sse",
        "url": "http://localhost:8888/sse"
      }
    }
}

{
    "mcpServers": {
      "github": {
        "command": "npx",
        "args": [
          "-y",
          "@modelcontextprotocol/server-github"
        ],
        "env": {
          "GITHUB_PERSONAL_ACCESS_TOKEN": "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"
        }
      },
      "zmp-alert-mcp": {
        "command": "python3",
        "args": [
          "-m",
          "zmp_alert_mcp_server",
          "--transport",
          "stdio",
          "--endpoint",
          "https://api.ags.cloudzcp.net",
          "--access-key",
          "zmp-f9aed626-c0d6-4293-8a66-c36755e8e948"
        ]
      }
    }
}
```
# MCP Inspector CLI for lowlevel server
```bash
$ npx @modelcontextprotocol/inspector uv --directory /Users/kks/IdeaProjects/aiops/zmp-openapi-mcp-server run zmp-openapi-mcp-server --transport stdio --endpoint https://api.ags.cloudzcp.net --access-key zmp-f9aed626-c0d6-4293-8a66-c36755e8e948 --spec-path /Users/kks/IdeaProjects/aiops/zmp-openapi-mcp-server/openapi/agent_apis_for_zcp_alert_manager.json
```

# fastmcp cli command
```bash
$ mcp dev src/zmp_openapi_mcp_server/fastmcp/zcp_alert_manager.py
$ mcp run src/zmp_openapi_mcp_server/fastmcp/zcp_alert_manager.py -t sse
$ mcp install src/zmp_openapi_mcp_server/fastmcp/zcp_alert_manager.py --name alert-manager --with zmp-openapi-toolkit,pyyaml
```

# How to run the lowlevel.server
## sse
```bash
zmp-openapi-mcp-server --port 9999 --transport sse -e https://api.ags.cloudzcp.net -s zmp-f9aed626-c0d6-4293-8a66-c36755e8e948 -p /Users/kks/IdeaProjects/aiops/zmp-openapi-mcp-server/openapi/zmp_mixed_api_spec.json
```

## stdio
first install the zmp-openapi-mcp-server
```bash
pip install zmp-openapi-mcp-server
```

then configure the mcp server into the mcp host like claude desktop or cursor
```json
{
  "mcpServers": {
    "zmp-openapi-mcp-server": {
      "command": "python3",
      "args": [
        "-m",
        "zmp_openapi_mcp_server",
        "--transport",
        "stdio",
        "--endpoint",
        "https://api.ags.cloudzcp.net",
        "--access-key",
        "zmp-f9aed626-c0d6-4293-8a66-c36755e8e948",
        "--spec-path",
        "/Users/kks/IdeaProjects/aiops/zmp-openapi-mcp-server/openapi/zmp_mixed_api_spec.json"
      ]
    }
  }
}
```


# backup the claude desktop mcp conf
```json
{
   "mcpServers": {
     "alert-manager": {
       "command": "uv",
       "args": [
         "run",
         "--with",
         "mcp[cli]",
         "--with",
         "zmp-openapi-toolkit,pyyaml",
         "mcp",
         "run",
         "/Users/kks/IdeaProjects/aiops/zmp-openapi-mcp-server/src/zmp_openapi_mcp_server/fastmcp/zcp_alert_manager.py"
       ]
     },
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
     "screenshot": {
       "command": "uv",
       "args": [
         "run",
         "--with",
         "mcp[cli],pyautogui",
         "mcp",
         "run",
         "/Users/kks/VscodeProjects/mcp/python-sdk/examples/fastmcp/screenshot.py"
       ]
     },
     "filesystem": {
       "command": "npx",
       "args": [
         "-y",
         "@modelcontextprotocol/server-filesystem",
         "/Users/kks/Downloads"
       ]
     }
   }
 }
 ```
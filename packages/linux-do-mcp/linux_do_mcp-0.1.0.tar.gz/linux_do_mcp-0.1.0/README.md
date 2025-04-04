## How to run locally?

I use the command `uv init linux-do-mcp` under the root path `src/linux-do-mcp/python`

If you want to run this MCP Server locally, you can follow the step bellow:

cd to `src/linux-do-mcp/python/linux-do-mcp`, and install the dependency

```
uv venv
uv pip install -e .
uv pip install "mcp[cli]" httpx
```

cd to `src/linux-do-mcp/python`, and run the following command to test in dev env

```
uv run main
```
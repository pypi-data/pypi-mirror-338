from typing import List

import anyio
import click
from mcp.server.lowlevel import Server
from mcp.types import TextContent, Tool, Prompt, GetPromptResult, Resource, FileUrl
from zmp_openapi_toolkit.models.operation import ZmpAPIOperation
from zmp_openapi_mcp_server.zmp_api_warrper import get_zmp_api_wrapper

import logging

logger = logging.getLogger(__name__)

@click.command()
@click.option("--transport", type=click.Choice(["stdio", "sse"]), default="stdio", help="Transport type")
@click.option("--port", default=9999, help="Port to listen on for SSE")
@click.option("--endpoint", "-e", type=str, required=True, help="ZMP OpenAPI endpoint")
@click.option("--access-key", "-s", type=str, required=True, help="ZMP OpenAPI access key")
@click.option("--spec-path", "-p", type=click.Path(exists=True), required=True, help="Path to the OpenAPI spec file")
@click.option("-v", "--verbose", count=True)
def main(
    port: int, transport: str, endpoint: str, access_key: str, spec_path: str, verbose: int = 2
) -> int:
    app = Server("zmp-openapi-mcp-server")
    zmp_api_wrapper = get_zmp_api_wrapper(endpoint, access_key, spec_path)
    operations: List[ZmpAPIOperation] = zmp_api_wrapper.get_operations()

    for operation in operations:
        logger.debug("-" * 100)
        logger.debug(f"args_schema: {operation.args_schema.model_json_schema()}")

    @app.call_tool()
    async def call_tool(name: str, arguments: dict) -> list[TextContent]:
        """
        Call the tool with the given name and arguments from llm.
        """
        logger.debug("=" * 100)
        logger.debug(f"call_tool: {name}")
        for key, value in arguments.items():
            logger.debug(f"\t{key}: {value}")
        logger.debug("=" * 100)

        operation = next((op for op in operations if op.name == name), None)
        if operation is None:
            # raise ValueError(f"Unknown tool: {name}")
            logger.error(f"Unknown tool: {name}")
            return [TextContent(type="text", text=f"Error: Unknown tool: {name}")]


        path_params = operation.path_params(**arguments) if operation.path_params else None
        query_params = operation.query_params(**arguments) if operation.query_params else None
        request_body = operation.request_body(**arguments) if operation.request_body else None

        logger.debug(f"path_params: {path_params}")
        logger.debug(f"query_params: {query_params}")
        logger.debug(f"request_body: {request_body}")

        try:
            result = zmp_api_wrapper.run(
                operation.method,
                operation.path,
                path_params=path_params,
                query_params=query_params,
                request_body=request_body,
            )
            
            return [TextContent(type="text", text=f"result: {result}")]
        except Exception as e:
            logger.error(f"Error: {e}")
            return [TextContent(type="text", text=f"Error: {e}")]

    @app.list_tools()
    async def list_tools() -> list[Tool]:
        """
        List all the tools available.
        """
        tools: List[Tool] = []
        for operation in operations:
            tool: Tool = Tool(
                name=operation.name,
                description=operation.description,
                inputSchema=operation.args_schema.model_json_schema(),
            )
            tools.append(tool)

            logger.debug("-" * 100)
            logger.debug(f":::: tool: {tool.name}\n{tool.inputSchema}")

        return tools
    
    @app.list_prompts()
    async def list_prompts() -> list[Prompt]:
        """
        List all the prompts available.
        """
        prompts: List[Prompt] = []
        return prompts

    @app.get_prompt()
    async def get_prompt(
        name: str, arguments: dict[str, str] | None = None
    ) -> GetPromptResult:
        """
        Get the prompt with the given name and arguments.
        """
        return None
    
    @app.list_resources()
    async def list_resources() -> list[Resource]:
        """
        List all the resources available.
        """
        return []
    
    @app.read_resource()
    async def read_resource(uri: FileUrl) -> str | bytes:
        """
        Read the resource with the given URI.
        """
        return None

    if transport == "sse":
        from mcp.server.sse import SseServerTransport
        from starlette.applications import Starlette
        from starlette.routing import Mount, Route

        sse = SseServerTransport("/messages/")

        async def handle_sse(request):
            async with sse.connect_sse(
                request.scope, request.receive, request._send
            ) as streams:
                await app.run(
                    streams[0], streams[1], app.create_initialization_options()
                )

        starlette_app = Starlette(
            debug=True,
            routes=[
                Route("/sse", endpoint=handle_sse),
                Mount("/messages/", app=sse.handle_post_message),
            ],
        )

        import uvicorn

        uvicorn.run(starlette_app, host="0.0.0.0", port=port)
    else:
        from mcp.server.stdio import stdio_server

        async def arun():
            async with stdio_server() as streams:
                await app.run(
                    streams[0], streams[1], app.create_initialization_options()
                )

        anyio.run(arun)

    return 0

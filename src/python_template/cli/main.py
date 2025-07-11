from pathlib import Path
from typing import Annotated
import typer
from typer import Typer


cli = Typer(name="example")


@cli.command(name="run", help="Run the FastAPI application")
def run(
    host: Annotated[
        str, typer.Option("--host", "-h", help="Host address.")
    ] = "127.0.0.1",
    port: Annotated[int, typer.Option("--port", "-p", help="App port.")] = 8001,
    reload: Annotated[
        bool, typer.Option(help="Reload the application on changes.")
    ] = False,
    root_path: Annotated[
        str, typer.Option("--root-path", "-r", help="Root path for the application.")
    ] = "/",
) -> None:
    import uvicorn

    uvicorn.run(
        "python_template.main:app",
        host=host,
        port=port,
        reload=reload,
        root_path=root_path,
    )


@cli.command(
    name="generate-openapi-schema", help="Generate openapi schema for the application."
)
def generate_openapi_schema(
    output_path: Annotated[
        Path,
        typer.Option(
            "--output-path",
            "-o",
            help="Output path for api schema.",
            exists=False,
            file_okay=True,
            dir_okay=False,
            writable=True,
            readable=False,
            resolve_path=True,
        ),
    ] = Path("resources/openapi.json"),
) -> None:
    from python_template.main import app
    from fastapi.openapi.utils import get_openapi
    import json

    openapi_schema = get_openapi(
        title="Example API",
        version="0.1.0",
        description="Example API",
        routes=app.routes,
    )
    with open(output_path, "w") as file:
        json.dump(openapi_schema, file, indent=4)

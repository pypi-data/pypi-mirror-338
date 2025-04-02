from streamlit.web import cli as st_cli

import click
from os import path
import pathlib


@click.command()
@click.option(
    "--server",
    prompt="Value API Server",
    help="The url of the value api server.",
    default="http://localhost",
)
@click.option(
    "--context",
    prompt="The root context",
    help="The root context for this frontend application.",
    default="default",
)
@click.option("--port", default=1, help="The port of the streamlit server.")
def cli(server, context, port):
    # TODO: how to run with a selected port or server ip?
    # TODO: add additional streamlit paramteters
    st_cli.main_run([
        path.join(pathlib.Path(__file__).parent.resolve(), "app.py"),
        server,
        context,
    ])

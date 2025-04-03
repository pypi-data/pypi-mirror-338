from typing import Annotated

import typer

from yaiclipy.core import YAICLI

CONTEXT_SETTINGS = {
    "help_option_names": ["-h", "--help"],
    "show_default": True,
}

app = typer.Typer(
    name="yaicli",
    context_settings=CONTEXT_SETTINGS,
    pretty_exceptions_enable=False,
    short_help="yaicli. Your AI interface in cli.",
    no_args_is_help=True,
    invoke_without_command=True,
)


@app.command()
def main(
    ctx: typer.Context,
    prompt: Annotated[
        str, typer.Argument(show_default=False, help="The prompt send to the LLM")
    ] = "",
    verbose: Annotated[
        bool, typer.Option("--verbose", "-V", help="Show verbose information")
    ] = False,
    chat: Annotated[bool, typer.Option("--chat", "-c", help="Start in chat mode")] = False,
    shell: Annotated[
        bool, typer.Option("--shell", "-s", help="Generate and execute shell command")
    ] = False,
):
    """yaicli. Your AI interface in cli."""
    if not prompt and not chat:
        typer.echo(ctx.get_help())
        raise typer.Exit()

    cli = YAICLI(verbose=verbose)
    cli.run(chat=chat, shell=shell, prompt=prompt)


if __name__ == "__main__":
    app()

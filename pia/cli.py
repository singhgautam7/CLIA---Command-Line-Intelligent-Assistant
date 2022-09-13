from datetime import datetime
from typing import Optional

import typer
import re
import random
import rich

from pia import __app_name__, __version__
import pia.constants as consts
import pia.regex as regx

app = typer.Typer()


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


def _process_query(lower_case_qry) -> str:
    """
    This will return the final output to be printed on the command line
    :param lower_case_qry: query in lower case
    :return: output
    """
    # Check if user is greeting
    if re.search(regx.GREETINGS, lower_case_qry):
        time_greetings = f"Good {['morning', 'morning', 'afternoon', 'evening'][int(datetime.now().hour/6)]}"
        possible_outputs = ["Hey there", "Hey human", "Hi"]
        return f"{random.sample(possible_outputs, 1)[0]}! {time_greetings}."

    # Check if user is closing
    if re.search(regx.CLOSINGS, lower_case_qry):
        time_greetings = f"Good {['night', 'bye', 'bye', 'night'][int(datetime.now().hour / 6)]}"
        possible_outputs = ["Take care", "See you", "See you soon", "Bye"]
        return f"{time_greetings}. {random.sample(possible_outputs, 1)[0]}."


@app.command(name='tell-me')
def tell_me(query: str) -> None:
    lower_case_qry = query.lower()
    output = _process_query(lower_case_qry)

    # if output not present
    if not output:
        rich.print("[bold red]Sorry, I did not get that[/bold red]")
        return
    rich.print(f"[blue]{output}[/blue]")


@app.callback()
def main(
        version: Optional[bool] = typer.Option(
            None,
            "--version",
            "-v",
            help="Show the application's version and exit",
            callback=_version_callback,
            is_eager=True,
        )
) -> None:
    return

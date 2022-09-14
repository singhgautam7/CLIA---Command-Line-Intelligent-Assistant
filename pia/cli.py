import random
import re
import webbrowser
from datetime import datetime
from time import sleep
from typing import Optional

import rich
import typer

from pia import __app_name__, __version__
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
    # Greetings
    if re.search(regx.GREETINGS, lower_case_qry):
        time_greetings = f"Good {['morning', 'morning', 'afternoon', 'evening'][int(datetime.now().hour / 6)]}"
        possible_outputs = ["Hey there", "Hey human", "Hi"]
        return f"{random.sample(possible_outputs, 1)[0]}! {time_greetings}."

    # Closing
    elif re.search(regx.CLOSINGS, lower_case_qry):
        time_greetings = f"Good {['night', 'bye', 'bye', 'night'][int(datetime.now().hour / 6)]}"
        possible_outputs = ["Take care", "See you", "See you soon", "Bye"]
        return f"{time_greetings}. {random.sample(possible_outputs, 1)[0]}."

    # How are you
    elif re.search(regx.HOW_ARE_YOU, lower_case_qry):
        possible_outputs = ["I am good.", "Okay-ish.", "I am good, thank you. Hope you are fine as well", "I am fine",
                            "I am well, thank you for asking"]
        return f"{random.sample(possible_outputs, 1)[0]}."

    # What is your name
    elif re.search(regx.WHATS_YOUR_NAME, lower_case_qry):
        possible_outputs = ["It's [bold green]Pia[/bold green]",
                            "My name is [bold  green]Pia[/bold green]",
                            "Well, people usually call me [bold green]Pia[/bold green], "
                            "but my real name is Python Intelligent Assistant."]
        return f"{random.sample(possible_outputs, 1)[0]}."

    # Time
    elif re.search(regx.WHATS_THE_TIME, lower_case_qry):
        return f"It is currently [bold green]{datetime.today().strftime('%I:%M %p')}[/bold green] at your location."

    # Date condition
    elif re.search(regx.WHATS_THE_DATE, lower_case_qry):
        return f"Today's date is [bold green]{datetime.today().strftime('%B %d, %Y')}[/bold green]."

    # Creator condition
    elif re.search(regx.CREATOR, lower_case_qry):
        return f"My creator goes by the name [bold green]Gautam Rajeev Singh[/bold green]. You can find more " \
               f"details about him at https://www.singhgautam.com/"

    # YouTube condition
    elif re.search(regx.YOUTUBE_SEARCH, lower_case_qry):
        search_term = re.sub('(search (for|about|on)*|(for|about|on)* youtube)', '', lower_case_qry)
        url = f"https://www.youtube.com/results?search_query={search_term}"
        rich.print("[blue]Here is what I found on[/blue] [bold red]YouTube[/bold red]")
        webbrowser.get().open(url)
        return f"Opened the results on your browser."

    # YouTube condition
    elif re.search(regx.GOOGLE_SEARCH, lower_case_qry):
        search_term = re.sub(regx.GOOGLE_SEARCH, '', lower_case_qry)
        url = f"https://google.com/search?q={search_term}"
        rich.print("[blue]Here is what I found on[/blue] [bold green]Google[/bold green]")
        webbrowser.get().open(url)
        return f"Opened the results on your browser."


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

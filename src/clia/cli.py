import random
import re
import webbrowser
from datetime import datetime
from time import sleep

import requests
import rich
import typer

try:
    from . import constants_regex as regx
except ImportError:
    import constants_regex as regx

app = typer.Typer()


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"PIA - Python Intelligent Assistant")
        raise typer.Exit()


def _google_search(search_term: str, flag_sleep: bool = False):
    url = f"https://google.com/search?q={search_term}"
    rich.print(f"[blue]Here is what I found on [bold green]Google[/bold green] "
               f"for [underline]{search_term}[/underline][/blue]")
    if flag_sleep:
        sleep(1)
    webbrowser.get().open(url)


def _youtube_search(search_term: str, flag_sleep: bool = False):
    url = f"https://www.youtube.com/results?search_query={search_term}"
    rich.print(f"[blue]Here is what I found on [bold red]YouTube[/bold red] "
               f"for [underline]{search_term}[/underline][/blue]")
    if flag_sleep:
        sleep(1)
    webbrowser.get().open(url)


def _wiki_search(search_term: str, flag_sleep: bool = False):
    url = f"https://en.wikipedia.org/wiki/Special:Search?go=Go&search={search_term}"
    rich.print(f"[blue]Here is what I found on [bold grey]Wikipedia[/bold grey] "
               f"for [underline]{search_term}[/underline][/blue]")
    if flag_sleep:
        sleep(1)
    webbrowser.get().open(url)


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
        possible_outputs = ["I am good", "Okay-ish", "I am good, thank you. Hope you are fine as well", "I am fine",
                            "I am well, thank you for asking"]
        return f"{random.sample(possible_outputs, 1)[0]}."

    # What is your name
    elif re.search(regx.WHATS_YOUR_NAME, lower_case_qry):
        possible_outputs = ["It's [bold green]Clia[/bold green]",
                            "My name is [bold  green]Clia[/bold green]",
                            "Well, people usually call me [bold green]Clia[/bold green], "
                            "but my real name is Command Line Intelligent Assistant"]
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
        search_term = re.sub('(search (for|about|on)*|(for|about|on|in)* youtube)', '', lower_case_qry)
        _youtube_search(search_term)
        return f"[grey itallic]Opened the results on your browser.[/grey itallic]"

    # Wikipedia condition
    elif re.search(regx.WIKI_SEARCH, lower_case_qry):
        search_term = re.sub('(search (for|about|on)*|(for|about|on|in)* (wikipedia))', '', lower_case_qry)
        _wiki_search(search_term)
        return f"[grey italic]Opened the results on your browser.[/grey italic]"

    # Google condition
    elif re.search(regx.GOOGLE_SEARCH, lower_case_qry):
        search_term = re.sub(regx.GOOGLE_SEARCH, '', lower_case_qry)
        _google_search(search_term)
        return f"[grey itallic]Opened the results on your browser.[/grey itallic]"

    elif re.search(regx.JOKE, lower_case_qry):
        r = requests.get('https://v2.jokeapi.dev/joke/Programming,Pun?format=txt')
        return r.text


@app.command(name='tell-me')
def tell_me(query: str) -> None:
    lower_case_qry = query.lower()
    output = _process_query(lower_case_qry)

    # if output not present
    if not output:
        _google_search(lower_case_qry, flag_sleep=True)
        return

    # If the print is already not formatted
    if '[' not in output and ']' not in output:
        rich.print(f"[blue]{output}[/blue]")
    else:
        rich.print(output)


@app.callback()
def main() -> None:
    return

import typer
from rich.console import Console

from APIQueries import APIQueries, format_response


def main(name: str = ""):
    console = Console()
    qery = APIQueries(api_key="2a3f462634msh63a4a8280da611ep1352acjsn54d03d9ef887")
    #with console.status("[bold green]Fetching data...[/bold green]", spinner="dots"):
    #    response = qery.current_weather(name)
    #format_response(response)
    print(qery.forecast(48.8583, 2.2945))


if __name__ == "__main__":
    typer.run(main)

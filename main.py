import typer
from rich.console import Console

from APIQueries import APIQueries, format_current_response, format_forecast_response


def main(choice: str, name: str ):
    console = Console()
    qery = APIQueries(api_key="2a3f462634msh63a4a8280da611ep1352acjsn54d03d9ef887")
    if choice == "cur":
        with console.status("[bold green]Fetching data...[/bold green]", spinner="dots"):
            response = qery.current_weather(name)
        format_current_response(response)
    elif choice == "for":
        with console.status("[bold green]Fetching data...[/bold green]", spinner="dots"):
            response = qery.forecast(48.8583, 2.2945)
            format_forecast_response(response)
if __name__ == "__main__":
    typer.run(main)

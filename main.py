import typer
from rich.console import Console

from APIQueries import APIQueries, format_current_response, format_forecast_response
from cities import get_coordinates

def main(choice: str, name: str ):
    console = Console()
    qery = APIQueries(api_key="2a3f462634msh63a4a8280da611ep1352acjsn54d03d9ef887")

    if choice == "cur":
        with console.status("[bold green]Fetching data...[/bold green]", spinner="dots"):
            response = qery.current_weather(name)
        format_current_response(response)
    elif choice == "for":
        try:
            coords = get_coordinates(name)
        except ValueError as e:
            typer.echo(e)
            raise typer.Exit(code=1)
        with console.status("[bold green]Fetching data...[/bold green]", spinner="dots"):
            response = qery.forecast(lat=float(coords["lat"]), lon=float(coords["lon"]))
        format_forecast_response(response)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    typer.run(main)

import typer

from APIQueries import APIQueries


def main(name: str=""):
    qery  = APIQueries(api_key="2a3f462634msh63a4a8280da611ep1352acjsn54d03d9ef887")
    response = qery.current_weather(name)
    print(response)

if __name__ == "__main__":
    typer.run(main)
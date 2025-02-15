import typer

def main(name: str, option: bool=False):
    if option:
        print(f"Option is enabled, Mister {name}")
    else:
        print(f"Aint got no option {name}")

if __name__ == "__main__":
    typer.run(main)
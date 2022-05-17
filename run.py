from simple_salesforce import Salesforce
from varian_utils_files import sf_tools
from varian_utils_files import my_errors
import pyreadline
from rich.console import Console
import typer
from rich import pretty, print
pretty.install()

app = typer.Typer()

@app.command()
def login_sf():
    sf = sf_tools.sf_login(sandbox=False)

@app.command()
def tools():

    print("[yellow]1.[/yellow]\tsf_tools\tWrap around [yellow]simple_salesforce[/yellow] for logging in Salesforce.\n" + 
    "[yellow]2.[/yellow]\tmy_errors\tImports and configure [yellow]pretty errors[/yellow] module for nice tracebacks exceptions reporting.\n"+
    "[yellow]3.[/yellow]\tmy_timer\t@my_timer decorator for looging execution time of functions.\n"+
    "[yellow]4.[/yellow]\tmystyle\t\tWrap around [yellow]colorama[/yellow] for console output coloring.\n")
if __name__ == "__main__":
    app()

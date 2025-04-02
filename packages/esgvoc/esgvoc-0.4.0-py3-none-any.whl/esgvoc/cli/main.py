import typer
from esgvoc.cli.get import app as get_app
from esgvoc.cli.status import app as status_app
from esgvoc.cli.valid import app as valid_app
from esgvoc.cli.install import app as install_app
from esgvoc.cli.drs import app as drs_app   
app = typer.Typer()

# Register the subcommands
app.add_typer(get_app)
app.add_typer(status_app)
app.add_typer(valid_app)
app.add_typer(install_app)
app.add_typer(drs_app)

def main():
    app()
    

if __name__ == "__main__":
    main()

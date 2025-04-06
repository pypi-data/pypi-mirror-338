from typer import Typer

app = Typer()
 
@app.command()
def login():
    print("Logging in...")
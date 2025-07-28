import click
import pyfiglet
from rich.console import Console

@click.command()
@click.option('--color', default='cyan', help='Color for the output text')
@click.option('--message', default='Developer of CLIck-Me-Codex3', help='Custom message')
def main(color, message):
    """Display a simple CLI profile."""
    console = Console()
    ascii_art = pyfiglet.figlet_format('Kim DaeHyun')
    console.print(ascii_art, style=color)
    console.print(message, style=color)

if __name__ == '__main__':
    main()

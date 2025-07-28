import click
import pyfiglet
from rich.console import Console


class ProfileCLI:
    """Simple class to display a CLI profile."""

    def __init__(self):
        self.console = Console()

    def display_profile(self, color: str, message: str) -> None:
        """Render the profile using Rich and PyFiglet."""
        ascii_art = pyfiglet.figlet_format('Kim DaeHyun')
        self.console.print(ascii_art, style=color)
        self.console.print(message, style=color)


@click.command()
@click.option(
    '--color',
    type=click.Choice(
        ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'],
        case_sensitive=False,
    ),
    default='cyan',
    help='Color for the output text',
)
@click.option('--message', default='Developer of CLIck-Me-Codex3', help='Custom message')
def main(color: str, message: str) -> None:
    """Entry point for the CLI command."""
    cli = ProfileCLI()
    cli.display_profile(color, message)


if __name__ == '__main__':
    main()

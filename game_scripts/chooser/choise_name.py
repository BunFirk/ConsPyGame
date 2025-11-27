from rich import box
from rich.console import Console
from rich.align import Align
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text
from modules.classes import local_player_class

console = Console()


def print_whats_your_name(text_bold: bool = True, text_color: str = "white", background_color: str = "black"):
    with console.screen(style=f'{"bold" if text_bold else ""} {text_color} on {background_color}') as screen:
        text_content = Align.center(
            Text.from_markup(f"""
[yellow]Давайте сначала выберем имя вашему персонажу![/yellow]
            """, justify="center"),
            vertical="middle",
        )
        screen.update(Panel(text_content, box=box.ROUNDED))

        inputNamePlayer = Prompt.ask("Имя вашенго персонажа: ", default="Странник")

        local_player_class.player_global.set_name(inputNamePlayer)
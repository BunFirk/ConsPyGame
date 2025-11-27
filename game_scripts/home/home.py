from rich import box
from rich.console import Console
from rich.align import Align
from rich.prompt import Prompt
from rich.text import Text
from rich.panel import Panel
import readchar

from modules.classes import local_player_class

console = Console()


def main(text_bold: bool = True, text_color: str = "white", background_color: str = "black"):
    with console.screen(style=f'{"bold" if text_bold else ""} {text_color} on {background_color}') as screen:
        text_content = Align.center(
            Text.from_markup(f"""
{local_player_class.player_global.get_player()}



:crossed_swords:  | [italic]Чтобы вступить в бой введите[/italic] [red]1[/red]
            """, justify="center"),
            vertical="middle",
        )
        screen.update(Panel(text_content, box=box.ROUNDED))

        broooLetsFight = Prompt.ask("[yellow]> [/yellow]")

        if broooLetsFight:
            pass


"""
[italic]:sparkles: | ваш уровень[/italic]: {self.invent}
"""
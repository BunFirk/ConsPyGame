from rich import box
from rich.console import Console
from rich.align import Align
from rich.text import Text
from rich.panel import Panel
import readchar

console = Console()


def print_dialog(dialog: str,text_bold: bool = True, text_color: str = "white", background_color: str = "black"):
    with console.screen(style=f'{"bold" if text_bold else ""} {text_color} on {background_color}') as screen:
        text_content = Align.center(
            Text.from_markup(f"""
            {dialog}   
            """, justify="center"),
            vertical="middle",
        )
        screen.update(Panel(text_content, box=box.ROUNDED))

        readchar.readkey()
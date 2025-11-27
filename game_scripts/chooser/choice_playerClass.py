from rich.console import Console
from rich.align import Align
from rich.prompt import Prompt
from rich.text import Text
from rich.panel import Panel
from rich.layout import Layout
from rich import box

from modules.classes import local_player_class
from modules.classes.local_player_class import Player

console = Console()


def print_choice(text_bold: bool = True, text_color: str = "white", background_color: str = "black"):

    witcher_content = Align.center(
        Text.from_markup(f"""
:heartpulse: | [italic]Здоровье[/italic] - [red]15[/red]
:brain: | [italic]Интеллект[/italic] - [yellow]60[/yellow]
:crystal_ball: | [italic]Мана[/italic] - [blue]10[/blue]
            """, justify="center"),
        vertical="middle",
    )
    mage_panel = Panel.fit(witcher_content, title="[yellow]:mage: Волшебник[/yellow]", height=10, box=box.ROUNDED)

    archer_content = Align.center(
        Text.from_markup(f"""
:heartpulse: | [italic]Здоровье[/italic] - [red]15[/red]
:bow_and_arrow: | [italic]Ловкость[/italic] - [green]16[/green]
:brain: | [italic]Интеллект[/italic] - [yellow]35[/yellow]
            """, justify="center"),
        vertical="middle",
    )
    archer_panel = Panel.fit(archer_content, title="[green]:bow_and_arrow: Лучник[/green]", height=10, box=box.ROUNDED)


    swordsman_content = Align.center(
        Text.from_markup(f'''
:heartpulse: | [italic]Здоровье[/italic] - [red]25[/red]
:bow_and_arrow: | [italic]Ловкость[/italic] - [green]16[/green]
:brain: | [italic]Интеллект[/italic] - [yellow]30[/yellow]
| 
''', justify="center"),
        vertical="middle"
    )
    swordsman_panel = Panel.fit(swordsman_content, title="[red]:crossed_swords: Мечник[/red]", height=10, box=box.ROUNDED)


    layout = Layout(name="main_layout")

    layout.split_column(
        Layout(name="header", size=5),
        Layout(name="choices_row")
    )

    layout["choices_row"].split_row(
        Layout(name="wizard"),
        Layout(name="archer"),
        Layout(name="swordsman")
    )

    header_content = Align.center(
        Text("Выберите класс:", justify="center", style="bold large"),
        vertical="middle",
    )
    layout["header"].update(Panel(header_content, box=box.SIMPLE))

    layout["wizard"].update(Align.center(mage_panel, vertical="middle"))
    layout["archer"].update(Align.center(archer_panel, vertical="middle"))
    layout["swordsman"].update(Align.center(swordsman_panel, vertical="middle"))


    with console.screen(style=f'{"bold" if text_bold else ""} {text_color} on {background_color}') as screen:
        final_content = Align.center(
            layout,
            vertical="middle",
            width=80
        )

        screen.update(final_content)
        inputPlayer_class = Prompt.ask("Какой класс выберешь? [yellow]>[/yellow]", choices=['Волшебник', 'Лучник', 'Мечник'])

        player = local_player_class.Player
        player(inputPlayer_class)


if __name__ == "__main__":
    print_choice()

from rich.console import Console
from rich.align import Align
from rich.prompt import Prompt
from rich.text import Text
from rich.panel import Panel
from rich.layout import Layout

console = Console()

def print_choice(text_bold: bool = True, text_color: str = "white", background_color: str = "black"):

    choose_class = Align.center(
        Text.from_markup(f"""
                Выберете класс:
                """, justify="center"),
        vertical="middle",
    )
    choose_panel = Panel.fit(choose_class, height=5)

    witcher_content = Align.center(

            Text.from_markup(f"""
:heartpulse: | [italic]Здровье[/italic] - [red]15[/red]

:crystal_ball: | [italic]Мана[/italic] - [blue]10[/blue]
            """, justify="center"),

            vertical="middle",

        )
    hello_panel = Panel.fit(witcher_content, title="[yellow]:mage: Волшебник[/yellow]", height=10)

    world_content = Align.center(

            Text.from_markup(f"""
:heartpulse: | [italic]Здровье[/italic] - [red]15[/red]

:crystal_ball: | [italic]Мана[/italic] - [blue]10[/blue]
            """, justify="center"),

            vertical="middle",

        )
    world_panel = Panel.fit(world_content, title=" Лучник", height=10)

    inner_layout = Layout(name="choice_row")

    inner_layout.split(
        Layout(name="upper"),
        Layout(name="lower"),
    )
    '''
    inner_layout.split_row(
        Layout(name="left", ratio=1, size=40),
        Layout(name="right", ratio=1, size=40),
    )
    '''

    inner_layout["lower"].split_column(
        Layout(name="left"),
        Layout(name="right"),
    )

    '''
    inner_layout["left"].update(world_panel)
    inner_layout["right"].update(world_panel)
    '''




    with console.screen(style=f'{"bold" if text_bold else ""} {text_color} on {background_color}') as screen:
        outer_panel = Panel(
            inner_layout
        )

        final_content = Align.center(
            outer_panel,
            vertical="middle",
        )

        screen.update(final_content)
        player_class = Prompt.ask("Какой класс выберешь? [yellow]>[/yellow]", choices=['Маг', 'Лучник'])

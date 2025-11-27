class Player:
    def __init__(self, player_game_class=None):
        self.name = "Странник"
        self.ex = 0
        self.hp = 0
        self.mana = 0
        self.agility = 0
        self.intelligence = 0
        self.invent = []

    def set_PlayerClass(self, player_game_class: str):
        self.player_game_class = player_game_class

        if player_game_class == "Волшебник":
            self.hp = 15
            self.mana = 10
            self.agility = 14
            self.intelligence = 40
            self.invent = ['Заклинание мороза', 'Магический доспех', 'Волшебный посох']

        elif player_game_class == "Лучник":
            self.hp = 20
            self.mana = 0
            self.agility = 18
            self.intelligence = 25
            self.invent = ['Проклятая стрела', 'Сапоги прыгуны', 'Длинный лук']

        elif player_game_class == "Мечник":
            self.hp = 25
            self.mana = 0
            self.agility = 20
            self.intelligence = 20
            self.invent = ['Каменный кулак', 'Щит дворфа', 'Закаленный меч']


    def set_name(self, name_inp:str):
        self.name = name_inp

    def get_player(self):
        return f"""
{self.name}
------------
:video_game: | [italic]ваш класс[/italic]: [green]{self.player_game_class}[/green]
:heartpulse: | [italic]ваше здоровье[/italic]: [red]{self.hp}[/red]
:: | [italic][/italic]: [violet]{self.ex}[/violet]
:crystal_ball: | [italic]ваша мана[/italic]: [blue]{self.mana}[/blue]
:high_voltage: | [italic]ваша ловкость[/italic]: [yellow]{self.agility}[/yellow]
:brain: | [italic]ваш интелект[/italic]: [deep_pink4]{self.intelligence}[/deep_pink4]
:package: | [italic]ваш инвентарь[/italic]: [cyan]{', '.join(self.invent)}[/cyan]
        """

player_global = Player()
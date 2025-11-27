import random

from rich import Console

from modules.classes import local_player_class

console = Console()

class Enemy:
    def __init__(self):
        self.max_hp = 0
        self.damage = 0
        self.hp = 0
        self.ex = 0
        self.name = "..."


    def generate_enemy(self):
        self.ex = random.randint(3, 10)
        self.hp = random.randint(20, 30)
        self.name = random.choice(['Дворф', 'Слизь', 'Эльф', 'Вампир'])

    def get_enemy(self):
        self.generate_enemy()
        self.max_hp = self.hp

        return f"""
[red]{self.name}[/red]
------------
[green]:heartpulse: | [italic]Здоровье[/italic]: {self.hp}/{self.max_hp}[/green]
[violet]{self.ex}[/violet]
"""

    def attack_enemy(self):
        self.damage = random.randint(1, 5)

        self.palyer_damage = random.randint(1, random.randint(3, 10))

        self.hp -= self.palyer_damage
        self.player_hp = local_player_class.player_global.hp - self.damage

        console.print(f'''
        Вы нанесли врагу {self.name} -> {self.palyer_damage}. Он наносит вам ответный удар {self.damage}.
''')


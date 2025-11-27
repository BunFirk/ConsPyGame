import json
class Player:
    def __init__(self):
        self.hp = None
        self.mana = None
        self.agility = None
        self.intelligence = None
        self.vezenie = None
        self.invent = None
        self.player_game_class = None
        self.name = None

    def set_name(self, name_inp:str):
        self.name = name_inp

    def set_player_class(self, player_game_class: str):
        self.player_game_class = player_game_class
        self.vezenie = 2

        if player_game_class == "Маг":
            self.hp = 15
            self.intelligence = 60
            self.mana = 10
            self.agility = 14

        elif player_game_class == "Лучник":
            self.hp = 15

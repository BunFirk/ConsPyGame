from game_scripts.chooser.choice_playerClass import print_choice
from game_scripts.dialogs import dialogs_1
from game_scripts.home import home


def main():
    dialogs_1.main()
    print_choice()
    home.main()



if __name__ == "__main__":
    main()
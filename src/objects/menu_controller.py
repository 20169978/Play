from curses import KEY_UP, KEY_DOWN

MENU_PETTERNS = {
    "playing": [
        ("Continue Game", "play"),
        ("Quit Game", "quit")
    ],
    "game_over": [
        ("Retry Game", "retry"),
        ("Quit Game", "quit")
    ],
    "win": [
        ("Next Stage", "next_stage"),
        ("Play Again", "retry"),
        ("Quit Game", "quit")
    ]
}

class MenuController:
    def __init__(self):
        self.__menu_state = "playing"
        self.__menu_options = []
        self.__selected_option = 0

    def set_menu_options(self, options):
        self.__menu_options = options
        self.__selected_option = 0

    def update_menu(self, key):
        if key == KEY_UP:
            self.__selected_option = (self.__selected_option - 1) % len(self.__menu_options)
        elif key == KEY_DOWN:
            self.__selected_option = (self.__selected_option + 1) % len(self.__menu_options)
        elif key == ord(" "):
            return self.__menu_options[self.__selected_option][1]

    def draw_menu(self, render):
        menu_text = ""
        for i, (option_text, _) in enumerate(self.__menu_options):
            if i == self.__selected_option:
                menu_text += "> " + option_text + " <\n"
            else:
                menu_text += "  " + option_text + "\n"
        render.draw_menu_area(menu_text)
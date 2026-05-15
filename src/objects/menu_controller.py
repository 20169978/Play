Menu_Pattern = {
    "default": [],
    "pouse": [
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
    ],
    "save_data": [
        ("Data_1", "data_1"),
        ("Data_2", "data_2"),
        ("Data_3", "data_3")
    ]
}

class MenuController:
    def __init__(self):
        self.__menu_options = []
        self.set_menu_options("default")
        self.__selected_option = 0

    def set_menu_options(self, options):
        self.__menu_options = Menu_Pattern[options]
        self.__selected_option = 0

    def update_menu(self, key):
        if key == "UP":
            self.__selected_option = (self.__selected_option - 1) % len(self.__menu_options)
        elif key == "DOWN":
            self.__selected_option = (self.__selected_option + 1) % len(self.__menu_options)
        elif key == "SHOOT":
            return self.__menu_options[self.__selected_option][1]

    def draw_menu(self, render):
        menu_text = ""
        for i, (option_text, _) in enumerate(self.__menu_options):
            if i == self.__selected_option:
                menu_text += "> " + option_text + " <\n"
            else:
                menu_text += "  " + option_text + "\n"
        render.draw_menu_area(menu_text)
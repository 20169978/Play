from render import BOTTOM_MENU
import math

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
    ],
    "stage_select": [
        ("Stage_1", ("stage",1)),
        ("Stage_2", "stage,2"),
        ("Stage_3", "stage,3"),
        ("Stage_4", "stage,4"),
        ("Stage_5", "stage,5"),
        ("Stage_6", "stage,6"),
        ("Stage_7", "stage,7"),
        ("Stage_8", "stage,8"),
        ("Stage_9", "stage,9"),
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
        if len(self.__menu_options) > BOTTOM_MENU[0]:
            column = math.ceil(len(self.__menu_options) / BOTTOM_MENU[0])
            
            for i in range(0, BOTTOM_MENU[0]):
                line_text = ""
                for j in range(0, column):
                    if j * BOTTOM_MENU[0] + i >= len(self.__menu_options):
                        break
                    text = ""
                    if j * BOTTOM_MENU[0] + i == self.__selected_option:
                        text = "> " + self.__menu_options[j * BOTTOM_MENU[0] + i][0] + " <"
                    else:
                        text = "  " + self.__menu_options[j * BOTTOM_MENU[0] + i][0] + "  "
                    line_text += text
                if i != BOTTOM_MENU[0] - 1:
                    line_text += "\n"
                menu_text += line_text

        else:
            for i, (option_text, _) in enumerate(self.__menu_options):
                if i == self.__selected_option:
                    menu_text += "> " + option_text + " <\n"
                else:
                    menu_text += "  " + option_text + "\n"
        render.draw_menu_area(menu_text)
import curses

# Height, Width
PLAY_AREA = 10 ,81
SEPARATOR = 1, 101
BOTTOM_MENU = 6 ,81
STATUS_AREA = 10, 20
KEY_EXPLAINER = 2, 101


# Colors
#safety colors
# curses.COLOR_BLACK
# curses.COLOR_RED
# curses.COLOR_GREEN
# curses.COLOR_YELLOW
# curses.COLOR_BLUE
# curses.COLOR_MAGENTA
# curses.COLOR_CYAN
# curses.COLOR_WHITE
MARGIN_FG = curses.COLOR_WHITE
MARGIN_BG = curses.COLOR_BLACK

PLAY_AREA_FG = curses.COLOR_BLACK
PLAY_AREA_BG = curses.COLOR_WHITE

SEPARATOR_FG = curses.COLOR_BLACK
SEPARATOR_BG = curses.COLOR_BLUE

BOTTOM_MENU_FG = curses.COLOR_WHITE
BOTTOM_MENU_BG = curses.COLOR_BLUE

KEY_EXPLAINER_FG = curses.COLOR_RED
KEY_EXPLAINER_BG = curses.COLOR_BLUE

STATUS_AREA_FG = curses.COLOR_BLACK
STATUS_AREA_BG = curses.COLOR_CYAN

SCORE_AREA_FG = curses.COLOR_WHITE
SCORE_AREA_BG = curses.COLOR_BLUE


class Render:
    def __init__(self, screen):
        self.__screen = screen

        # Clear screen
        curses.curs_set(0)  # Hide cursor
        curses.start_color()

        self.__screen.clear()
        self.__screen.refresh()
        self.__screen.nodelay(True)  # Non-blocking input

        # Initialize color pair
        curses.init_pair(1, PLAY_AREA_FG, PLAY_AREA_BG)        
        curses.init_pair(2, SEPARATOR_FG, SEPARATOR_BG)
        curses.init_pair(3, BOTTOM_MENU_FG, BOTTOM_MENU_BG)
        curses.init_pair(4, STATUS_AREA_FG, STATUS_AREA_BG)
        curses.init_pair(5, SCORE_AREA_FG, SCORE_AREA_BG)
        curses.init_pair(6, MARGIN_FG, MARGIN_BG)
        curses.init_pair(7, KEY_EXPLAINER_FG, KEY_EXPLAINER_BG)

        # Setup play area and bottom menu
        screen_size = self.__screen.getmaxyx()
        self.__left_top = (screen_size[0] // 2 - (PLAY_AREA[0] + BOTTOM_MENU[0] + KEY_EXPLAINER[0] + SEPARATOR[0]) // 2, screen_size[1] // 2 - (PLAY_AREA[1] + STATUS_AREA[1]) // 2)
        self.__play_area = curses.newwin(PLAY_AREA[0], PLAY_AREA[1], self.__left_top[0], self.__left_top[1])
        self.__separator = curses.newwin(SEPARATOR[0], SEPARATOR[1], self.__left_top[0] + PLAY_AREA[0], self.__left_top[1])
        self.__bottom_menu = curses.newwin(BOTTOM_MENU[0], BOTTOM_MENU[1], self.__left_top[0] + PLAY_AREA[0] + SEPARATOR[0], self.__left_top[1])
        self.__key_explainer = curses.newwin(KEY_EXPLAINER[0], PLAY_AREA[1] + STATUS_AREA[1], self.__left_top[0] + PLAY_AREA[0] + SEPARATOR[0] + BOTTOM_MENU[0], self.__left_top[1])

        self.__status_area = curses.newwin(STATUS_AREA[0], STATUS_AREA[1], self.__left_top[0], self.__left_top[1] + PLAY_AREA[1])
        self.__score_area = curses.newwin(BOTTOM_MENU[0], STATUS_AREA[1], self.__left_top[0] + PLAY_AREA[0] + SEPARATOR[0], self.__left_top[1] + BOTTOM_MENU[1])

        # Init margin
        self.__screen.bkgd(' ', curses.color_pair(2))
        self.__screen.clear()
        self.__screen.refresh()
        self.__screen.bkgd(' ', curses.color_pair(6))
        self.__screen.clear()
        self.__screen.refresh()
        #Init play area
        self.__play_area.bkgd(' ', curses.color_pair(1))
        self.__play_area.refresh()
        # Init separator
        self.__separator.bkgd('-', curses.color_pair(2))
        self.__separator.refresh()
        # Init menu
        self.__bottom_menu.bkgd(' ', curses.color_pair(3))
        self.__bottom_menu.refresh()
        # Init key explainer        
        self.__key_explainer.bkgd(' ', curses.color_pair(7))
        self.__key_explainer.addstr(0, 0, "[Play] <Space> Shoot | <Up>/<Down> Move | <M> Open Menu\n[Menu] <Space>Confirm | <Up>/<Down>Select")
        self.__key_explainer.refresh()
        # Init status area
        self.__status_area.bkgd(' ', curses.color_pair(4))
        self.__status_area.refresh()
        # Init score area
        self.__score_area.bkgd(' ', curses.color_pair(5))
        self.__score_area.refresh()

    def clear_play_area(self):
        self.__play_area.clear()
        self.__play_area.refresh()

    def draw_play_area(self, icon, position):
        # if color_pair:
        #    self.__play_area.addstr(position[0], position[1], icon, curses.color_pair(color_pair))
        # else:
        #     self.__play_area.addstr(position[0], position[1], icon)
        self.__play_area.addstr(0, 0, "`")
        icons = icon.split("\n")

        position = self.calc_pos(position)
        for i in range(0, len(icons)):
            if position[0] + i >= PLAY_AREA[0]:
                continue
            self.__play_area.addstr(position[0] + i, position[1], icons[i])
        
        self.__play_area.refresh()

    def draw_menu_area(self, text):
        self.__bottom_menu.clear()
        self.__bottom_menu.addstr(0, 0, text)
        self.__bottom_menu.refresh()

    def draw_status_area(self, text):
        self.__status_area.clear()
        self.__status_area.addstr(0, 0, text)
        self.__status_area.refresh()

    def draw_score_area(self, text):
        self.__score_area.clear()
        self.__score_area.addstr(0, 0, text)
        self.__score_area.refresh()


    def show_message(self, message):
        message_lines = message.split("\n")
        self.__message_box = curses.newwin(len(message_lines) + 4, 32, self.__left_top[0] + 1, self.__left_top[1] + PLAY_AREA[1] // 2 - 15)
        for cell in range(0, 31):
            self.__message_box.addstr(0, cell, "-")
            self.__message_box.addstr(len(message_lines) + 3, cell, "-")
        
        for i in range(0, len(message_lines)):
            self.__message_box.addstr(
                2 + i,
                15 - len(message_lines[i]) // 2,
                message_lines[i])
        self.__message_box.refresh()

    def clear_message(self):
        self.__message_box.clear()


    def calc_pos(self, pos):
        y = 0
        x = 0
        if type(pos[0]) is int:
            y = pos[0]
        else:
            y = PLAY_AREA[0] - 1 if int((pos[0] * 2 + 1)//2) > PLAY_AREA[0] - 1 else int((pos[0] * 2 + 1)//2)

        if type(pos[1]) is int:
            x = pos[1]
        else:
            x = int((pos[1] * 2 + 1)//2)

        return (y,x)
import curses

# Height, Width
PLAY_AREA = 10 ,80
BOTTOM_MENU = 6 ,80

# Colors
PLAY_AREA_FG = curses.COLOR_WHITE
PLAY_AREA_BG = curses.COLOR_BLACK
SEPARATOR_FG = curses.COLOR_BLACK
SEPARATOR_BG = curses.COLOR_WHITE
BOTTOM_MENU_FG = curses.COLOR_BLACK
BOTTOM_MENU_BG = curses.COLOR_WHITE


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
        
        # Setup play area and bottom menu
        self.__play_area = curses.newwin(PLAY_AREA[0], PLAY_AREA[1], 0, 0)
        self.__separator = curses.newwin(1, PLAY_AREA[1], PLAY_AREA[0], 0)
        self.__bottom_menu = curses.newwin(BOTTOM_MENU[0], BOTTOM_MENU[1], PLAY_AREA[0] + 1, 0)
    
        #Init play area
        self.__play_area.bkgd(' ', curses.color_pair(1))
        self.__play_area.refresh()
        # Init separator
        self.__separator.bkgd('-', curses.color_pair(2))
        self.__separator.refresh()
        # Init menu
        self.__bottom_menu.bkgd(' ', curses.color_pair(3))
        self.__bottom_menu.refresh()

    def clear_play_area(self):
        self.__play_area.clear()
        self.__play_area.refresh()

    def draw_play_area(self, icon, position):
        # if color_pair:
        #    self.__play_area.addstr(position[0], position[1], icon, curses.color_pair(color_pair))
        # else:
        #     self.__play_area.addstr(position[0], position[1], icon)
        icons = icon.split("\n")
        for i in range(0, len(icons)):
            if position[0] + i >= PLAY_AREA[0]:
                break
            self.__play_area.addstr(position[0] + i, position[1], icons[i])
        
        self.__play_area.refresh()

    def show_message(self, message):
        message_lines = message.split("\n")
        self.__message_box = curses.newwin(len(message_lines) + 4, 32, 1, PLAY_AREA[1]//2 - 15)
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
        del self.__message_box

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

    def draw_play_area(self, icon, position, color_pair=0):
        if color_pair:
            self.__play_area.addstr(position[0], position[1], icon, curses.color_pair(color_pair))
        else:
            self.__play_area.addstr(position[0], position[1], icon)
        self.__play_area.refresh()
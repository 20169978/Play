import curses

def main(stdscr):
    curses.start_color()

    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    stdscr.addstr(0, 0, "default\n")
    stdscr.addstr(1, 0, "white black\n", curses.color_pair(1))
    stdscr.addstr(2, 0, "red black\n", curses.color_pair(2))

    stdscr.getch()

curses.wrapper(main)
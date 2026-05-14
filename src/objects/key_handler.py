import curses

class KeyHandler:
    def __init__(self):
        self.key_config = {
            "UP": [curses.KEY_UP, ord("w")],
            "DOWN": [curses.KEY_DOWN, ord("s")],
            "SHOOT": [ord(" ")],
            "MENU": [ord("m")]
        }
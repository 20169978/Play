import curses

class KeyHandler:
    def __init__(self):
        self.__key_config = {
            "UP": [curses.KEY_UP, ord("w")],
            "DOWN": [curses.KEY_DOWN, ord("s")],
            "LEFT": [curses.KEY_LEFT, ord("a")],
            "RIGHT": [curses.KEY_RIGHT, ord("d")],
            "SHOOT": [ord(" ")],
            "MENU": [ord("m")]
        }

    def is_key_pushed(self, key, key_type):
        return key in self.__key_config[key_type]
    
    def get_key(self, key_pushed):
        for key, list in self.__key_config.items():
            for value in list:
                if value == key_pushed:
                    return key
        return None

    def set_key_config(self, key_pushed, key_type):
        if key_type in self.__key_config.keys:
            for key, value in self.__key_config.items():
                if value == key_pushed:
                    self.__key_config[key_type].remove(value)
            if len(self.__key_config[key_type]) > 1:
                self.__key_config[key_type].pop(0)             
            self.__key_config[key_type].append(key_pushed)
            return True
        else:
            return False


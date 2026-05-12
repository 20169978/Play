from objects.base import Base
from render import PLAY_AREA
from curses import KEY_UP, KEY_DOWN
from objects.hitbox import Hitbox

class Player(Base, Hitbox):
    def __init__(self):
        super().__init__()
        self.hitbox = (0, 0)
        self.__touching_endline = False

    def update(self, key):
        if key == KEY_UP:
            self.position = (max(0, self.position[0] - 1), self.position[1])
        elif key == KEY_DOWN:
            self.position = (min(PLAY_AREA[0] - 1, self.position[0] + 1), self.position[1])

    def hit(self, object_hit):
        pass

    @property
    def touching_endline(self):
        return self.__touching_endline
    
    @touching_endline.setter
    def touching_endline(self, value):
        self.__touching_endline = value
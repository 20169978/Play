from objects.base import Base
from render import PLAY_AREA, MOVABLE_AREA
from objects.hitbox import Hitbox


INVICIBILITY_DURATION = 10


class Player(Base, Hitbox):
    def __init__(self):
        super().__init__()
        self.__touching_endline = False
        self.__invicibility_timer = 0

    def update(self, key):
        self.ex_pos = self.position
        self.invicibility_timer = max(0, self.invicibility_timer - 1)
        if key == "UP":
            self.position = (max(MOVABLE_AREA[0][0], self.position[0] - 1), self.position[1])
        elif key == "DOWN":
            self.position = (min(MOVABLE_AREA[1][0], self.position[0] + 1), self.position[1])
        elif key == "LEFT":
            self.position = (self.position[0], max(MOVABLE_AREA[0][1], self.position[1] - 1))
        elif key == "RIGHT":
            self.position = (self.position[0], min(MOVABLE_AREA[1][1], self.position[1] + 1))

    def hit(self, object_hit):
        pass

    def damage(self, power):
        if self.invicibility_timer < 1:
            self.health -= power
            self.invicibility_timer = INVICIBILITY_DURATION

    @property
    def touching_endline(self):
        return self.__touching_endline
    
    @touching_endline.setter
    def touching_endline(self, value):
        self.__touching_endline = value

    @property
    def invicibility_timer(self):
        return self.__invicibility_timer
    
    @invicibility_timer.setter
    def invicibility_timer(self, value):
        self.__invicibility_timer = value
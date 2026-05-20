from objects.base import Base
from objects.base_enemy import BaseEnemy
from objects.hitbox import Hitbox
from objects.player import Player
from render import PLAY_AREA

class Enemy_U(Base, BaseEnemy, Hitbox):
    def __init__(self):
        super().__init__()
        self.score_value = 10
        self.power = 1
        self.dir = -1
        self.health = 1
        self.icon = "U"

    def update(self):
        self.ex_pos = self.position
        self.position = (self.position[0], self.position[1] + 0.6 * self.dir)
        if self.position[1] < 1:
            self.dir = 1
        if self.position[1] > PLAY_AREA[1] - 3:
            self.dir = -1
            
    def damage(self, power):
        self.health -= power
        if self.health < 1:
            self.kill()

    def hit(self, object_hit):
        if isinstance(object_hit, Player):
            object_hit.damage(self.power)
            self.kill(False)
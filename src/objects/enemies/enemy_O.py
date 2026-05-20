from objects.base import Base
from objects.base_enemy import BaseEnemy
from objects.hitbox import Hitbox
from objects.player import Player

class Enemy_O(Base, BaseEnemy, Hitbox):
    def __init__(self):
        super().__init__()
        self.score_value = 20
        self.power = 1
        self.health = 2
        self.icon = "O"

    def update(self):
        self.ex_pos = self.position
        self.position = (self.position[0], self.position[1] - 0.5)
        if self.position[1] < 1:
            self.kill(False)
            
    def damage(self, power):
        self.health -= power
        if self.health < 1:
            self.kill()
        elif self.health < 2:
            self.icon = "o"

    def hit(self, object_hit):
        if isinstance(object_hit, Player):
            object_hit.damage(self.power)
            self.kill(False)
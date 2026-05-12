from objects.base import Base
from objects.base_enemy import BaseEnemy
from objects.hitbox import Hitbox
from objects.player import Player

class Enemy_Test(Base, BaseEnemy, Hitbox):
    def __init__(self):
        super().__init__()
        self.hitbox = (0, -1)
        self.score_value = 10
        self.power = 1

    def update(self):
        self.position = (self.position[0], self.position[1] - 1)
        if self.position[1] < 1:
            self.kill(False)
            
    def damage(self, power):
        self.health -= power
        if self.health < 1:
            self.kill()

    def hit(self, object_hit):
        if isinstance(object_hit, Player):
            object_hit.damage(self.power)
            self.kill(False)
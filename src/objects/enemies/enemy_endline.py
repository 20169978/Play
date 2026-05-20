from objects.player import Player
from objects.base import Base
from objects.base_enemy import BaseEnemy
from objects.hitbox import Hitbox
from render import PLAY_AREA


class Enemy_Endline(Base, BaseEnemy, Hitbox):
    def __init__(self):
        super().__init__()
        self.icon = "⚑"

    def update(self):
        self.ex_pos = self.position
        if self.position[1] > 2:
            self.position = (self.position[0], self.position[1] - 0.3)
        else:
            self.position = (self.position[0], 2)
            
    def damage(self, power):
        pass

    def hit(self, object_hit):
        if isinstance(object_hit, Player):
            object_hit.touching_endline = True
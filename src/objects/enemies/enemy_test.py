from objects.base import Base
from objects.base_enemy import BaseEnemy
from objects.hitbox import Hitbox
from objects.player import Player
from render import PLAY_AREA
from objects.effects.effect_bomb import Effect_Bomb

class Enemy_Test(Base, BaseEnemy, Hitbox):
    def __init__(self):
        super().__init__()
        self.score_value = 10
        self.power = 1
        self.__dir = 1

    def update(self):
        self.ex_pos = self.position
        self.position = (self.position[0] + 0.1 * self.__dir, self.position[1] - 0.5)
        if self.position[1] < 1:
            self.kill(False)
        if self.position[0] < 1:
            self.__dir = 1
        if self.position[0] > PLAY_AREA[0] - 2:
            self.__dir = -1
            
    def damage(self, power):
        self.health -= power
        if self.health < 1:
            Effect_Bomb(self.position)
            self.kill()

    def hit(self, object_hit):
        if isinstance(object_hit, Player):
            object_hit.damage(self.power)
            self.kill(False)
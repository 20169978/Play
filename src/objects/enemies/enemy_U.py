from objects.base_enemy import BaseEnemy
from objects.hitbox import Hitbox
from render import PLAY_AREA

class Enemy_U(BaseEnemy, Hitbox):
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

        response = []
        for res in self.response:
            result = res()
            if result != None:
                response.append(result)
        if len(response) > 0:
            return response
        else:
            return None
            
    def damage(self, power):
        self.health -= power
        if self.health < 1:
            self.kill()
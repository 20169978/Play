from objects.base_enemy import BaseEnemy
from objects.hitbox import Hitbox

class Enemy_O(BaseEnemy, Hitbox):
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

        response = []
        for res in self.response:
            result = res()
            if result != None:
                response.append(result)
        if len(response) > 0:
            return response
        else:
            return None
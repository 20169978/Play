from objects.player import Player
from objects.base_enemy import BaseEnemy
from objects.hitbox import Hitbox


class Enemy_Endline(BaseEnemy, Hitbox):
    def __init__(self):
        super().__init__()
        self.icon = "⚑"
        self.response = []

    def update(self):
        self.ex_pos = self.position
        if self.position[1] > 2:
            self.position = (self.position[0], self.position[1] - 0.3)
        else:
            self.position = (self.position[0], 2)

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
        pass

    def hit(self, object_hit):
        if isinstance(object_hit, Player):
            object_hit.touching_endline = True
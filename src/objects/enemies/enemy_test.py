from objects.base_enemy import BaseEnemy
from objects.hitbox import Hitbox
from render import PLAY_AREA

class Enemy_Test(BaseEnemy, Hitbox):
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

        response = []
        for res in self.response:
            result = res()
            if result != None:
                for v in result:
                    response.append(v)
        if len(response) > 0:
            return response
        else:
            return None
        
    
            
    

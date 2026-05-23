from abc import ABC, abstractmethod

from objects.base import Base
from objects.player import Player

class BaseEnemy(Base, ABC):
    def __init__(self):
        super().__init__()
        self.__score_value = 0
        self.__death_effect = "bomb"
        self.__effect_events = []
        self.response = [self.res_death, self.res_effect]

    @property
    def score_value(self):
        return self.__score_value
    
    @score_value.setter
    def score_value(self, value):    
        self.__score_value = value

    @property
    def death_effect(self):
        return self.__death_effect
    
    @death_effect.setter
    def death_eefect(self, value):
        self.__death_effect = value

    def kill(self, killed_by_player=True):
        self.health = 0
        if not killed_by_player:
            self.score_value = 0

    def hit(self, object_hit):
        if isinstance(object_hit, Player):
            object_hit.damage(self.power)
            self.kill(False)
            

    def damage(self, power):
        self.health -= power
        if self.health < 1:
            self.add_effect(self.__death_effect, self.position)
            self.kill()

    def add_effect(self, type_of_effect, pos):
        self.__effect_events.append((type_of_effect,pos))

    def update(self):
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

    def res_death(self):
        if self.health < 1:
            return [("death", self.score_value)]
        else:
            return None
        
    def res_effect(self):
        res = []
        while len(self.__effect_events) > 0:
            res.append(("effect",self.__effect_events.pop(0)))

        return None if len(res) < 1 else res
            


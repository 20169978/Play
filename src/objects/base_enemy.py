from abc import ABC, abstractmethod

class BaseEnemy(ABC):
    def __init__(self):
        super().__init__()
        self.__score_value = 0

    @property
    def score_value(self):
        return self.__score_value
    
    @score_value.setter
    def score_value(self, value):    
        self.__score_value = value

    @abstractmethod
    def damage(self, power):
        pass

    def kill(self, killed_by_player=True):
        self.health = 0
        if not killed_by_player:
            self.score_value = 0
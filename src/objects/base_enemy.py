from abc import ABC, abstractmethod

class BaseEnemy(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def damage(self, power):
        pass
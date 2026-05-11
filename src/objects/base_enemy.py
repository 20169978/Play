from abc import ABC, abstractmethod

class BaseEnemy(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def damage(self, power):
        pass
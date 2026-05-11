from abc import ABC, abstractmethod

class Base(ABC):
    def __init__(self):
        super().__init__()
        self.__health = 1
        self.__position = (0, 0)
        self.__icon = "P"

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        self.__health = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

    @property
    def icon(self):
        return self.__icon

    @icon.setter
    def icon(self, value):
        self.__icon = value

    @abstractmethod
    def update(self):
        pass

    def kill(self):
        self.health = 0
from abc import ABC, abstractmethod

class BaseBullet(ABC):
    def __init__(self):
        super().__init__()
        self.__position = (0, 0)
        self.__icon = "*"
        self.__health = 1
        self.__speed = 1
        self.__power = 1

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

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        self.__health = value

    @property
    def speed(self):
        return self.__speed 

    @speed.setter
    def speed(self, value): 
        self.__speed = value

    @property
    def power(self):
        return self.__power
    
    @power.setter
    def power(self, value):
        self.__power = value

    @abstractmethod
    def update(self):
        pass
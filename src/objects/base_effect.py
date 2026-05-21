from abc import ABC

class Base_Effect(ABC):
    def __init__(self):
        super().__init__()
        self.__icon = ""
        self.__animation = []
        self.__position = (-1,-1)

    def next_icon(self):
        if len(self.__animation) < 1:
            return False
        self.__icon = self.__animation.pop(0)
        return True
    
    def update(self):
        pass

    @property
    def icon(self):
        return self.__icon
    
    @icon.setter
    def icon(self, value):
        self.__icon = value

    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, value):
        self.__position = value
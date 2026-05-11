from abc import ABC, abstractmethod


def Check_Hitbox():
    for obj in Hitbox.Objects:
        pos = obj.position
        hitbox_pos = (obj.position[0] + obj.hitbox[0], obj.position[1] + obj.hitbox[1])
        
        if pos[0] > hitbox_pos[0]:
            copy = pos[0]
            pos = (hitbox_pos[0], pos[1])
            hitbox_pos = (copy, hitbox_pos[1])
        if pos[1] > hitbox_pos[1]:
            copy = pos[1]
            pos = (pos[0], hitbox_pos[1])
            hitbox_pos = (hitbox_pos[0], copy)

        for obj_2 in Hitbox.Objects:
           if obj is obj_2:
               continue
           if pos[0] <= obj_2.position[0] <= hitbox_pos[0] and pos[1] <= obj_2.position[1] <= hitbox_pos[1]:
               obj.hit(obj_2)

class Hitbox(ABC):
    Objects = []

    def __init__(self): # size(x,y). 0,0 = 1 cell
        super().__init__()
        self.__hitbox = (0, 0)
        Hitbox.Objects.append(self)
        
    @property
    def hitbox(self):
        return self.__hitbox
    
    @hitbox.setter
    def hitbox(self, value):
        self.__hitbox = value

    @abstractmethod
    def hit(self, object_hit):
        pass

    def remove_hitbox(self):
        if self in Hitbox.Objects:
            Hitbox.Objects.remove(self)

    
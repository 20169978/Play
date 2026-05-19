from abc import ABC, abstractmethod


def Check_Hitbox():
    queue = []
    for i in range(0,len(Hitbox.Objects)):
        queue.append(i)
    for i in range(0, len(Hitbox.Objects)):
        obj = Hitbox.Objects[queue.pop(0)]
        pos = obj.position
        ex_pos = obj.ex_pos
        if ex_pos == (-1,-1):
            continue

        obj_hitbox_left_top = (
            pos[0] if pos[0] < ex_pos[0] else ex_pos[0],
            pos[1] if pos[1] < ex_pos[1] else ex_pos[1]
        )
        obj_hitbox_right_bottom = (
            ex_pos[0] if pos[0] < ex_pos[0] else pos[0],
            ex_pos[1] if pos[1] < ex_pos[1] else pos[1]
        )

        for j in queue:
            obj_2 = Hitbox.Objects[j]
            pos = obj_2.position
            ex_pos = obj_2.ex_pos
            obj2_hitbox_left_top = (
                pos[0] if pos[0] < ex_pos[0] else ex_pos[0],
                pos[1] if pos[1] < ex_pos[1] else ex_pos[1]
            )
            obj2_hitbox_right_bottom = (
                ex_pos[0] if pos[0] < ex_pos[0] else pos[0],
                ex_pos[1] if pos[1] < ex_pos[1] else pos[1]
            )
           
            if check_hit(obj_hitbox_left_top, obj_hitbox_right_bottom, obj2_hitbox_left_top, obj2_hitbox_right_bottom):
                obj.hit(obj_2)
                obj_2.hit(obj)
        

def check_hit(first_lt,first_rb,second_lt,second_rb):
    if (first_lt[0] > second_lt[0] and first_lt[0] > second_rb[0]) or (first_rb[0] < second_lt[0] and first_rb[0] < second_rb[0]):
        return False
    if (first_lt[1] > second_lt[1] and first_lt[1] > second_rb[1]) or (first_rb[1] < second_lt[1] and first_rb[1] < second_rb[1]):
        return False
    return True

def Hitbox_Clear():
    Hitbox.Objects = []

class Hitbox(ABC):
    Objects = []

    def __init__(self): # size(x,y). 0,0 = 1 cell
        super().__init__()
        self.__hitbox = (0, 0)
        self.__ex_pos = (-1, -1)
        Hitbox.Objects.append(self)
        
    @property
    def hitbox(self):
        return self.__hitbox
    
    @hitbox.setter
    def hitbox(self, value):
        self.__hitbox = value

    @property
    def ex_pos(self):
        return self.__ex_pos
    
    @ex_pos.setter
    def ex_pos(self, value):
        self.__ex_pos = value

    @abstractmethod
    def hit(self, object_hit):
        pass

    def remove_hitbox(self):
        if self in Hitbox.Objects:
            Hitbox.Objects.remove(self)

    
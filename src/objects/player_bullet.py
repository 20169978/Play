from objects.base_bullet import BaseBullet
from objects.hitbox import Hitbox
from objects.base_enemy import BaseEnemy

class PlayerBullet(BaseBullet, Hitbox):
    def __init__(self):
        super().__init__()
        self.hitbox = (0,1)

    def update(self):
        self.position = (self.position[0], self.position[1] + self.speed)

    def hit(self, object_hit):
        if isinstance(object_hit, BaseEnemy):
            object_hit.damage(self.power)
            self.health -= 1
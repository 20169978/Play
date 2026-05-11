from objects.player import Player
from render import PLAY_AREA
from objects.player_bullet import PlayerBullet

class PlayerManager:
    def __init__(self):
        super().__init__()
        self.__player = Player()
        self.__player.icon = ">"
        self.__player.position = (PLAY_AREA[0] // 2, 2)
        self.__player.health = 1
        self.__bullets = []

    def update_player(self, key):
        for bullet in self.__bullets:
            bullet.update()
            if bullet.position[1] >= PLAY_AREA[1]:
                self.__bullets.remove(bullet)
            if bullet.health < 1:
                bullet.remove_hitbox()
                self.__bullets.remove(bullet)

        if key == ord(" "):
            bullet = PlayerBullet()
            bullet.position = (self.__player.position[0], self.__player.position[1] + 1)
            self.__bullets.append(bullet)
        self.__player.update(key)        
        


    def draw_player(self, render):
        render.draw_play_area(self.__player.icon, self.__player.position)
        for bullet in self.__bullets:
            render.draw_play_area(bullet.icon, bullet.position)
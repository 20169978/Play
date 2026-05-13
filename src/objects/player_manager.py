from objects.player import Player
from render import PLAY_AREA
from objects.player_bullet import PlayerBullet

BULLET_COOLDOWN = 5

class PlayerManager:
    Player_Pos = (0,0)

    def __init__(self):
        super().__init__()
        self.__player = Player()
        self.__player.icon = ">"
        self.__player.position = (PLAY_AREA[0] // 2, 2)
        self.__player.health = 2
        self.__player.invicibility_timer = 0
        self.__player.touching_endline = False
        
        self.__bullets = []
        self.__bullet_cooldown = 0
        

    def update_player(self, key):
        response = []
        # Update bullets
        for bullet in self.__bullets:
            bullet.update()
            if bullet.position[1] >= PLAY_AREA[1]:
                self.__bullets.remove(bullet)
            if bullet.health < 1:
                bullet.remove_hitbox()
                self.__bullets.remove(bullet)
        # Bullet firing
        if key == ord(" "):
            if self.__bullet_cooldown <= 0:
                self.__bullet_cooldown = BULLET_COOLDOWN
                bullet = PlayerBullet()
                bullet.position = (self.__player.position[0], self.__player.position[1] + 1)
                self.__bullets.append(bullet)
        self.__bullet_cooldown = max(0, self.__bullet_cooldown - 1)
        
        # Update player position
        self.__player.update(key) 
        PlayerManager.Player_Pos = self.__player.position

        response.append(("bullet_cooldown", self.__bullet_cooldown if self.__bullet_cooldown > 0 else 0))
        response.append(("health", self.__player.health if self.__player.health > 0 else 0))
        response.append(("invicibility_timer", self.__player.invicibility_timer))
        
        # Check if player is touching endline
        if self.__player.touching_endline:
            self.__player.touching_endline = False
            response.append(("hit_endline", None))
        
        # Check if player is died
        if self.__player.health < 1:
            response.append(("died", None))
        return response


    def draw_player(self, render):
        render.draw_play_area(self.__player.icon, self.__player.position)
        for bullet in self.__bullets:
            render.draw_play_area(bullet.icon, bullet.position)
from objects.player import Player
from render import PLAY_AREA, MOVABLE_AREA
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

        self.__movable_area_border = []
        

    def update_player(self, key):
        response = []
        # Update bullets
        for bullet in self.__bullets:
            bullet.update()
            if bullet.position[1] > PLAY_AREA[1] - 2 or bullet.health < 1:
                bullet.remove_hitbox()
                self.__bullets.remove(bullet)
        # Bullet firing
        if key == "SHOOT":
            if self.__bullet_cooldown <= 0:
                self.__bullet_cooldown = BULLET_COOLDOWN
                bullet = PlayerBullet()
                bullet.position = (self.__player.position[0], self.__player.position[1] + 1)
                self.__bullets.append(bullet)
        self.__bullet_cooldown = max(0, self.__bullet_cooldown - 1)
        
        # Update player position
        player_response = self.__player.update(key) 
        PlayerManager.Player_Pos = self.__player.position

        if player_response != None:
            for res in player_response:
                if res[0] == "hit_endline":
                    response.append(("hit_endline", None))
                    continue
                if res[0] == "dead":
                    response.append(("died", None))
                    continue
                if res[0] == "touch_movable_border":
                    self.__movable_area_border.append(res[1])
                    continue



        response.append(("bullet_cooldown", self.__bullet_cooldown if self.__bullet_cooldown > 0 else 0))
        response.append(("health", self.__player.health if self.__player.health > 0 else 0))
        response.append(("invicibility_timer", self.__player.invicibility_timer))

        return response


    def draw_player(self, render):
        render.draw_play_area(self.__player.icon, self.__player.position)
        for bullet in self.__bullets:
            render.draw_play_area(bullet.icon, bullet.position)
        while len(self.__movable_area_border) > 0:
            border = self.__movable_area_border.pop(0)
            render.draw_play_area(border[0], border[1])
            
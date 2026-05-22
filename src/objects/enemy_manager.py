import random

from objects.enemies.enemy_test import Enemy_Test
from objects.enemies.enemy_endline import Enemy_Endline
from objects.enemies.enemy_O import Enemy_O
from objects.enemies.enemy_U import Enemy_U

from render import PLAY_AREA
from objects.player_manager import PlayerManager


Enemy_Reference = {
    "test": Enemy_Test,
    "endline": Enemy_Endline,

    "O": Enemy_O,
    "U": Enemy_U,
}


class EnemyManager:
    def __init__(self):
        super().__init__()
        self.enemies = []
        self.enemy_queue = []
        self.spawn_timer = 0

    def update_enemies(self):
        return_data = []

        self.spawn_timer += 1
        while True:
            if len(self.enemy_queue) < 1:
                break
            if self.enemy_queue[0][0] > self.spawn_timer:
                break
            enemy_data = self.enemy_queue.pop(0)
            enemy = enemy_data[1]()
            enemy.position = (
                random.randint(
                    PlayerManager.Player_Pos[0]  if enemy_data[2] == "p" else 
                    PLAY_AREA[0] - 1 if enemy_data[2] > PLAY_AREA[0] - 1 else enemy_data[2], 
                    PlayerManager.Player_Pos[0]  if enemy_data[3] == "p" else 
                    PLAY_AREA[0] - 1 if enemy_data[3] > PLAY_AREA[0] - 1 else enemy_data[3]),
                PLAY_AREA[1] - 2)
            self.enemies.append(enemy)

        score_gained = 0
        enemy_killed_counter = 0
        for enemy in self.enemies:
            enemy_response = enemy.update()
            if enemy_response != None:
                for res in enemy_response:
                    if res[0] == "death":
                        enemy.remove_hitbox()
                        if res[1] > 0:
                            score_gained += res[1]
                            enemy_killed_counter += 1
                        self.enemies.remove(enemy)
                        continue
                    if res[0] == "effect":
                        return_data.append(res)
                        continue

        if score_gained > 0:
            return_data.append(("score_gained", score_gained))
        if enemy_killed_counter > 0:
            return_data.append(("enemy_killed", enemy_killed_counter))
        return return_data if len(return_data) > 0 else None

    def draw_enemies(self, render):
        for enemy in self.enemies:
            render.draw_play_area(enemy.icon, enemy.position)

    def setup_enemies(self, stage):
        for enemy_data in stage:
            enemy_type = enemy_data[1]
            if enemy_type in Enemy_Reference:
                self.enemy_queue.append((enemy_data[0], Enemy_Reference[enemy_type], enemy_data[2], enemy_data[3]))
            
    
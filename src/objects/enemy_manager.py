import random

from objects.enemy_test import Enemy_Test
from objects.enemy_endline import Enemy_Endline

from render import PLAY_AREA
from objects.player_manager import PlayerManager


Enemy_Reference = {
    "test": Enemy_Test,
    "endline": Enemy_Endline
}


class EnemyManager:
    def __init__(self):
        super().__init__()
        self.enemies = []
        self.enemy_queue = []
        self.spawn_timer = 0

    def update_enemies(self):
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
                    PlayerManager.Player_Pos[0]  if enemy_data[2] == "p" else enemy_data[2], 
                    PlayerManager.Player_Pos[0]  if enemy_data[3] == "p" else enemy_data[3]),
                PLAY_AREA[1] - 1)
            self.enemies.append(enemy)

        score_gained = 0
        for enemy in self.enemies:
            enemy.update()
            if enemy.health < 1:
                enemy.remove_hitbox()
                if enemy.score_value > 0:
                    score_gained += enemy.score_value
                self.enemies.remove(enemy)
        return ("enemy_killed", score_gained) if score_gained > 0 else None
        

    def draw_enemies(self, render):
        for enemy in self.enemies:
            render.draw_play_area(enemy.icon, enemy.position)

    def setup_enemies(self, stage):
        for enemy_data in stage:
            enemy_type = enemy_data[1]
            if enemy_type in Enemy_Reference:
                self.enemy_queue.append((enemy_data[0], Enemy_Reference[enemy_type], enemy_data[2], enemy_data[3]))
            
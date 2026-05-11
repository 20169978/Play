from objects.enemy_test import Enemy_Test
from render import PLAY_AREA
import random

Enemy_Reference = {
    "test": Enemy_Test
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
            enemy.position = (random.randint(0, PLAY_AREA[0] - 1), PLAY_AREA[1] - 1)
            self.enemies.append(enemy)

        for enemy in self.enemies:
            enemy.update()
            if enemy.health < 1:
                enemy.remove_hitbox()
                self.enemies.remove(enemy)

    def draw_enemies(self, render):
        for enemy in self.enemies:
            render.draw_play_area(enemy.icon, enemy.position)

    def setup_enemies(self, stage):
        for enemy_data in stage:
            enemy_type = enemy_data[1]
            if enemy_type in Enemy_Reference:
                self.enemy_queue.append((enemy_data[0], Enemy_Reference[enemy_type]))
            
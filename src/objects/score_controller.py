class ScoreController:
    def __init__(self):
        self.__score = 0
        self.__distance = 0
        self.__enemy_killed = 0

    def add_score(self, points):
        self.__score += points

    def add_distance(self, distance):
        self.__distance += distance

    def add_enemy_killed(self, count):
        self.__enemy_killed += count

    def draw_score(self, render):
        render.draw_score_area(f"Score: {self.__score}\n\nDistance: {self.__distance}\n\nEnemy Kills: {self.__enemy_killed}")
class ScoreController:
    def __init__(self):
        self.__score = 0
        self.__distance = 0

    def add_score(self, points):
        self.__score += points

    def add_distance(self, distance):
        self.__distance += distance

    def draw_score(self, render):
        render.draw_score_area(f"Score: {self.__score}\n\nDistance: {self.__distance}")
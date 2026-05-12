class ScoreController:
    def __init__(self, render):
        self.__render = render
        self.__score = 0

    def add_score(self, points):
        self.__score += points
        self.__render.draw_score_area(f"Score: {self.__score}")
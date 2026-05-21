class EffectManager:
    def __init__(self):
        super().__init__()
        self.__effects = []

    def update_effects(self):
        for effect in self.__effects:
            res = effect.next_icon()
            if res == False:
                self.__effects.remove(effect)
            effect.update()

    def draw_effects(self, render):
        for effect in self.__effects:
            render.draw_play_area(effect.icon, effect.position)

    def append_effect(self, new_effect):
        self.__effects.append(new_effect)
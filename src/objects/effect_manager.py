from objects.effects.effect_bomb import Effect_Bomb

EFFECT_REF = {
    "bomb": Effect_Bomb
}


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

    def add_effect(self, new_effect_info):
        if new_effect_info[0] in EFFECT_REF.keys():
            effect = EFFECT_REF[new_effect_info[0]](new_effect_info[1])
            self.__effects.append(effect)
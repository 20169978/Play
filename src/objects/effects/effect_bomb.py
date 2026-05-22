from objects.base_effect import Base_Effect

class Effect_Bomb(Base_Effect):
    def __init__(self, pos):
        super().__init__()
        self.animation = [
            "·", "+", "x", "*", "#"
        ]
        self.position = pos
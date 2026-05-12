COOLDOWN_VISUALIZER = [
    "[===READY===]",
    "[========== ]",
    "[=========  ]",
    "[========   ]",
    "[=======    ]",
    "[======     ]",
    "[=====      ]",
    "[====       ]",
    "[===        ]",
    "[==         ]",
    "[=          ]",
    "[           ]"
]




class StatusController:
    def __init__(self):
        self.__bullet_cooldown = 0
        self.__health = 0
        self.__invicibility_timer = 0

    def set_bullet_cooldown(self, value):
        self.__bullet_cooldown = value
    
    def set_health(self, value):
        self.__health = value

    def set_invicibility_timer(self, value):
        self.__invicibility_timer = value

    def draw_status(self, render):
        output = ""
        # health
        if self.__invicibility_timer > 0:
            output += "HP: " + "♡" * self.__health + "\n"
        else:
            output += "HP: " + "♥" * self.__health + "\n"
        
        # bullet cooldown
        output += "Bullet:\n" + COOLDOWN_VISUALIZER[self.__bullet_cooldown] + "\n"
        render.draw_status_area(output)
        
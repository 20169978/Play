from objects.file_handler import Parse_Stage
from render import PLAY_AREA
from objects.enemy_manager import Enemy_Reference

class StageManager:
    def __init__(self):
        super().__init__()

    def get_stage(self, path):
        stage = Parse_Stage(path)

        stage_formed = []
        for data in stage:
            time = 0
            try:
                time = int(data[0])
            except ValueError:
                continue
            
            if not data[1] in Enemy_Reference.keys():
                continue

            pos_from = 0
            try:
                pos_from = int(data[2])
                if pos_from > PLAY_AREA[0]:
                    pos_from = PLAY_AREA[0]
            except ValueError:
                if data[2] == "p":
                    pos_from = "p"
                else:
                    continue
            pos_to = 0
            try:
                pos_to = int(data[3])
                if pos_to > PLAY_AREA[0]:
                    pos_to = PLAY_AREA[0]
            except ValueError:
                if data[3] == "p":
                    pos_to = "p"
                else:
                    continue
            
            stage_formed.append((
                time,
                data[1],
                pos_from,
                pos_to
            ))
        return stage_formed



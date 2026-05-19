from objects.file_handler import Open_File
from render import PLAY_AREA
from objects.enemy_manager import Enemy_Reference

class StageManager:
    def __init__(self):
        super().__init__()
        self.__current_stage = 0
        self.__stage = self.__form_stage_data(self.__current_stage)

    def __form_stage_data(self, stage_number):
        path = f"src/resource/stages/stage_{stage_number}.txt"
        data = Open_File(path)

        stage_lines = data.splitlines()
        stage = []
        for line in stage_lines:
            stage.append((line.split(",")[0].strip(), line.split(",")[1].strip(), line.split(",")[2].strip(), line.split(",")[3].strip()))
    
    
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

    def set_next_stage(self):
        self.__current_stage += 1
        self.__stage = self.__form_stage_data(self.__current_stage)

    def get_stage(self):
        return self.__stage

    @property
    def current_stage(self):
        return self.__current_stage
    
    @current_stage.setter
    def current_stage(self, stage_num):
        self.__current_stage = stage_num
        self.__form_stage_data(self.__current_stage)

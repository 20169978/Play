from objects.file_handler import Open_File

class SaveDataHandler():
    def __init__(self):
        self.__user_data_name = "data_1"
        text = Open_File(f"src/resource/save_data/save_data.txt")
        self.__save_data = {}
        for line in text.splitlines():
            values = line.split(",")
            key = values.pop(0).strip()

            def try_int(s):
                try:
                    return int(s)
                except ValueError:
                    return s
            
            self.__save_data[key] = (tuple([
                try_int(x.strip())
                for x in values]))
            
    def set_user_data(self, name):
        if name not in ["data_1", "data_2", "data_3"]:
            return False
        self.__user_data_name = name
            
    def get_all_data(self):
        return self.__save_data
    
    def get_data(self):
        return self.__save_data[self.__user_data_name] or False

    def save_data(self, data):
        self.__save_data[self.__user_data_name] = data
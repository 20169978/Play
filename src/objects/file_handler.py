def Open_File(path):
    with open(path, "r") as file_handler:
        data = file_handler.read()
        
    return data
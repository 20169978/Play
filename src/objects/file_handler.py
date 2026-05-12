def Parse_Stage(path):
    with open(path, "r") as file_handler:
        stage_data = file_handler.read()
        
    stage_lines = stage_data.splitlines()
    stage = []
    for line in stage_lines:
        stage.append((line.split(",")[0].strip(), line.split(",")[1].strip(), line.split(",")[2].strip(), line.split(",")[3].strip()))
    return stage
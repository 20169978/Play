class StatusController:
    def __init__(self, render):
        self.__render = render
        self.__status = "Ready"

    def update_status(self, new_status):
        self.__status = new_status
        self.__render.draw_status_area(f"Status: {self.__status}")
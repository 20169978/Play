import curses
from render import Render
from objects.player_manager import PlayerManager
from objects.enemy_manager import EnemyManager
from objects.stage_manager import StageManager
from objects.menu_controller import MenuController
from objects.status_controller import StatusController
from objects.score_controller import ScoreController
from objects.key_handler import KeyHandler
from objects.save_data_handler import SaveDataHandler

from objects.hitbox import Check_Hitbox, Hitbox_Clear

import time


DEBUG = False
FPS = 20
TITLE = "ShootingGame"

class Managers():
    def __init__(self,stdscr):
        self.render = Render(stdscr)
        self.stage_manager = StageManager()
        self.key_handler = KeyHandler()
        self.save_data_handler = SaveDataHandler()
        self.set_up()

    def set_up(self):
        Hitbox_Clear()
        self.player_manager = PlayerManager()
        self.enemy_manager = EnemyManager()
        self.menu_controller = MenuController()
        self.status_controller = StatusController()
        self.score_controller = ScoreController()
        self.menu_controller.draw_menu(self.render)
        self.enemy_manager.setup_enemies(self.stage_manager.get_stage())


def main(stdscr):
    m = Managers(stdscr)
    if DEBUG:
        mode = "message" # or "menu" or "quit" or "message"
        message = f"{TITLE}\ntestmode\n\nSHOOT to start" # shown message

        stage_manager = StageManager()
        player_manager = PlayerManager()
        enemy_manager = EnemyManager()
        menu_controller = MenuController()
        status_controller = StatusController()
        score_controller = ScoreController()
        key_handler = KeyHandler()

        #setup menu
        menu_controller.set_menu_options("default")
        menu_controller.draw_menu(render)
        #setup stage
        enemy_manager.setup_enemies(stage_manager.get_stage())
        while mode != "quit":
            while mode == "play":
                start_time = time.time()

                render.clear_play_area()
                player_manager.draw_player(render)
                enemy_manager.draw_enemies(render)
                score_controller.draw_score(render)
                status_controller.draw_status(render)

                key_pushed = stdscr.getch()
                key = key_handler.get_key(key_pushed)
                if key == "MENU":
                    message = "Paused"
                    render.show_message(message)
                    menu_controller.set_menu_options("pouse")
                    mode = "menu"
                    break

                response = player_manager.update_player(key)
                if response is not None:
                    if "hit_endline" in [x[0] for x in response]:
                        message = "You win!"
                        render.show_message(message)
                        menu_controller.set_menu_options("win")
                        mode = "menu"
                        break
                    if "died" in [x[0] for x in response]:
                        message = "You died!"
                        render.show_message(message)
                        menu_controller.set_menu_options("game_over")
                        mode = "menu"
                        break

                    for data in response:
                        if data[0] == "bullet_cooldown":
                            status_controller.set_bullet_cooldown(data[1])
                        if data[0] == "health":
                            status_controller.set_health(data[1])
                        if data[0] == "invicibility_timer":
                            status_controller.set_invicibility_timer(data[1])


                response = enemy_manager.update_enemies()
                if response is not None:
                    for data in response:
                        if data[0] == "score_gained":
                            score_controller.add_score(data[1])
                        elif data[0] == "enemy_killed":
                            score_controller.add_enemy_killed(data[1])

                score_controller.add_distance(1)
                Check_Hitbox()
            
                elapsed_time = time.time() - start_time
                sleep_time = max(0, (1 / FPS) - elapsed_time)
                time.sleep(sleep_time)


            while mode == "menu":
                start_time = time.time()
                key_pushed = stdscr.getch()
                key = key_handler.get_key(key_pushed)
                response = menu_controller.update_menu(key)
                if response is not None:
                    if response == "play":
                        mode = "play"
                        menu_controller.set_menu_options("default")
                        menu_controller.draw_menu(render)
                        break
                    elif response == "quit":
                        mode = "quit"
                        menu_controller.set_menu_options("default")
                        menu_controller.draw_menu(render)
                        break
                    elif response == "retry" or response == "next_stage":
                        Hitbox_Clear()
                        if response == "next_stage":
                            stage_manager.set_next_stage()
                        player_manager = PlayerManager()
                        status_controller = StatusController()
                        score_controller = ScoreController()
                        menu_controller = MenuController()
                        menu_controller.set_menu_options("default")
                        menu_controller.draw_menu(render)
                        enemy_manager = EnemyManager()
                        enemy_manager.setup_enemies(stage_manager.get_stage())

                        mode = "play"
                        break

                menu_controller.draw_menu(render)

                elapsed_time = time.time() - start_time
                sleep_time = max(0, (1 / FPS) - elapsed_time)
                time.sleep(sleep_time)

            while mode == "message":
                start_time = time.time()
                render.show_message(message)

                key_pushed = stdscr.getch()
                key = key_handler.get_key(key_pushed)
                if key == "SHOOT":
                    mode = "play"
                    render.clear_message()
                    break

                elapsed_time = time.time() - start_time
                sleep_time = max(0, (1 / FPS) - elapsed_time)
                time.sleep(sleep_time)
    else:
        mode = "message" # or "menu" or "quit" or "message"
        message = f"{TITLE}\n\nSHOOT to start" # shown message

        #setup menu
        m.menu_controller.set_menu_options("default")
        m.menu_controller.draw_menu(m.render)
        #setup stage
        m.enemy_manager.setup_enemies(m.stage_manager.get_stage())
        while mode != "quit":
            while mode == "play":
                start_time = time.time()

                m.render.clear_play_area()
                m.player_manager.draw_player(m.render)
                m.enemy_manager.draw_enemies(m.render)
                m.score_controller.draw_score(m.render)
                m.status_controller.draw_status(m.render)

                key_pushed = stdscr.getch()
                key = m.key_handler.get_key(key_pushed)
                if key == "MENU":
                    message = "Paused"
                    m.render.show_message(message)
                    m.menu_controller.set_menu_options("pouse")
                    mode = "menu"
                    break

                response = m.player_manager.update_player(key)
                if response is not None:
                    if "hit_endline" in [x[0] for x in response]:
                        message = "You win!"
                        m.render.show_message(message)
                        m.stage_manager.set_next_stage()
                        m.menu_controller.set_menu_options("win")
                        mode = "menu"
                        break
                    if "died" in [x[0] for x in response]:
                        message = "You died!"
                        m.render.show_message(message)
                        m.menu_controller.set_menu_options("game_over")
                        mode = "menu"
                        break

                    for data in response:
                        if data[0] == "bullet_cooldown":
                            m.status_controller.set_bullet_cooldown(data[1])
                        if data[0] == "health":
                            m.status_controller.set_health(data[1])
                        if data[0] == "invicibility_timer":
                            m.status_controller.set_invicibility_timer(data[1])


                response = m.enemy_manager.update_enemies()
                if response is not None:
                    for data in response:
                        if data[0] == "score_gained":
                            m.score_controller.add_score(data[1])
                        elif data[0] == "enemy_killed":
                            m.score_controller.add_enemy_killed(data[1])

                m.score_controller.add_distance(1)
                Check_Hitbox()
            
                elapsed_time = time.time() - start_time
                sleep_time = max(0, (1 / FPS) - elapsed_time)
                time.sleep(sleep_time)


            while mode == "menu":
                start_time = time.time()
                key_pushed = stdscr.getch()
                key = m.key_handler.get_key(key_pushed)
                results = m.menu_controller.update_menu(key)
                response = results[0] if type(results) is tuple else results
                if response is not None:
                    if response == "play":
                        mode = "play"
                        m.menu_controller.set_menu_options("default")
                        m.menu_controller.draw_menu(m.render)
                        break
                    elif response == "quit":
                        mode = "quit"
                        m.menu_controller.set_menu_options("default")
                        m.menu_controller.draw_menu(m.render)
                        break
                    elif response == "retry" or response == "next_stage":
                        m.set_up()

                        mode = "play"
                        break
                    elif response in ["data_1", "data_2", "data_3"]:
                        m.save_data_handler.set_user_data(response)
                        data = m.save_data_handler.get_data()
                        
                        message = f"Next stage is Stage_{data[0]}"
                        m.render.show_message(message)
                        m.stage_manager.current_stage = data[0]
                        m.menu_controller.set_menu_options("stage_select")
                    elif response == "stage":
                        stage_num = results[1]
                        if m.stage_manager.current_stage < stage_num:
                            print("here")
                            message = f"Stage_{stage_num} is locked.\nNext stage is Stage_{data[0]}"
                            m.render.show_message(message)
                        else:
                            m.stage_manager.current_stage = stage_num
                            m.set_up()
                            mode = "play"
                            break
                    elif response == "select_stage":
                        message = f"Next stage is Stage_{stage_manager.current_stage}"
                        m.render.show_message(message)
                        m.menu_controller.set_menu_options("stage_select")
                        

                m.menu_controller.draw_menu(m.render)

                elapsed_time = time.time() - start_time
                sleep_time = max(0, (1 / FPS) - elapsed_time)
                time.sleep(sleep_time)

            while mode == "message":
                start_time = time.time()
                m.render.show_message(message)

                key_pushed = stdscr.getch()
                key = m.key_handler.get_key(key_pushed)
                if key == "SHOOT":
                    mode = "menu"
                    m.render.clear_message()
                    m.render.show_message("Chose your data.")
                    m.menu_controller.set_menu_options("save_data")
                    break

                elapsed_time = time.time() - start_time
                sleep_time = max(0, (1 / FPS) - elapsed_time)
                time.sleep(sleep_time)




if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except curses.error as e:
        print("Curses error:", e)
        print("Please ensure your terminal supports the required features and is large enough to display the game.")
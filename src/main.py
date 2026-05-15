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



def main(stdscr):
    render = Render(stdscr)
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

        stage_manager = StageManager()
        player_manager = PlayerManager()
        enemy_manager = EnemyManager()
        menu_controller = MenuController()
        status_controller = StatusController()
        score_controller = ScoreController()
        key_handler = KeyHandler()
        save_data_handler = SaveDataHandler()

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
                    elif response in ["data_1", "data_2", "data_3"]:
                        save_data_handler.set_user_data(response)
                        data = save_data_handler.get_data()
                        

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
                    mode = "menu"
                    render.clear_message()
                    render.show_message("Chose your data.")
                    menu_controller.set_menu_options("save_data")
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
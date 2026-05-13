import curses
from render import Render
from objects.player_manager import PlayerManager
from objects.enemy_manager import EnemyManager
from objects.stage_manager import StageManager
from objects.menu_controller import MENU_PETTERNS, MenuController
from objects.status_controller import StatusController
from objects.score_controller import ScoreController

from objects.hitbox import Check_Hitbox, Hitbox_Clear

import time


DEBUG = True
FPS = 20

def main(stdscr):
    mode = "message" # or "menu" or "quit" or "message"
    message = "ShootingGame\n<test mode>\n\npress <SPACE> to start" # shown message

    render = Render(stdscr)
    if DEBUG:
        stage_manager = StageManager()
        player_manager = PlayerManager()
        enemy_manager = EnemyManager()
        menu_controller = MenuController()
        status_controller = StatusController()
        score_controller = ScoreController()

        #setup menu
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

                key = stdscr.getch()
                if key == ord("m"):
                    message = "Paused"
                    render.show_message(message)
                    menu_controller.set_menu_options(MENU_PETTERNS["playing"])
                    mode = "menu"
                    break

                response = player_manager.update_player(key)
                if response is not None:
                    if "hit_endline" in [x[0] for x in response]:
                        message = "You win!"
                        render.show_message(message)
                        menu_controller.set_menu_options(MENU_PETTERNS["win"])
                        mode = "menu"
                        break
                    if "died" in [x[0] for x in response]:
                        message = "You died!"
                        render.show_message(message)
                        menu_controller.set_menu_options(MENU_PETTERNS["game_over"])
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
                key = stdscr.getch()
                response = menu_controller.update_menu(key)
                if response is not None:
                    if response == "play":
                        mode = "play"
                        break
                    elif response == "quit":
                        mode = "quit"
                        break
                    elif response == "retry" or response == "next_stage":
                        Hitbox_Clear()
                        if response == "next_stage":
                            stage_manager.set_next_stage()
                        player_manager = PlayerManager()
                        status_controller = StatusController()
                        score_controller = ScoreController()
                        menu_controller = MenuController()
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

                key = stdscr.getch()
                if key == ord(" "):
                    mode = "play"
                    render.clear_message()
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
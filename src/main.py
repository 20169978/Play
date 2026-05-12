import curses
from render import Render
from objects.player_manager import PlayerManager
from objects.enemy_manager import EnemyManager
from objects.stage_manager import StageManager
from objects.hitbox import Check_Hitbox

import time


DEBUG = True
FPS = 20
STAGE = "src/resource/stages/test.txt" # Stage file path <- fix this

def main(stdscr):
    mode = "play" # or "menu" or "quit" or "message"
    message = "" # shown message

    render = Render(stdscr)
    if DEBUG:
        stage_manager = StageManager()
        player_manager = PlayerManager()
        enemy_manager = EnemyManager()

        stage = stage_manager.get_stage(STAGE)

        enemy_manager.setup_enemies(stage)
        while mode != "quit":
            while mode == "play":
                start_time = time.time()

                render.clear_play_area()
                player_manager.draw_player(render)
                enemy_manager.draw_enemies(render)

                key = stdscr.getch()
                if key == ord("q"):
                    mode = "quit"
                    break
                if key == ord("m"):
                    mode = "menu"
                    break
                player_manager.update_player(key)
                enemy_manager.update_enemies()
                Check_Hitbox()
            
                elapsed_time = time.time() - start_time
                sleep_time = max(0, (1 / FPS) - elapsed_time)
                time.sleep(sleep_time)


            while mode == "menu":
                key = stdscr.getch()
                if key == ord("q"):
                    mode = "quit"
                    break
                if key == ord("p"):
                    mode = "play"
                    break

                elapsed_time = time.time() - start_time
                sleep_time = max(0, (1 / FPS) - elapsed_time)
                time.sleep(sleep_time)

            while mode == "message":
                render.show_message(message)

                key = stdscr.getch()
                if key == ord("q"):
                    mode = "quit"
                    render.clear_message()
                    break
                if key == ord(" "):
                    mode = "play"
                    render.clear_message()
                    break
                if key == ord("m"):
                    mode = "menu"
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
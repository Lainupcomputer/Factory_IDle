import sys
import time
import pygame
from pygame.locals import *
from Resources.Player import Player
from Resources import screen_objects as sobj
from Resources.screen_objects import LPanel, RPanel
from Resources.entitys import worker, opt
from Resources.entitys import Player as P

# Debug Functions
debug = False
if "-debug" in sys.argv:
    debug = True
print(f"Debug Mode: {debug}")

# configuration

from Resources.ez_config import ez_config
cfg = ez_config()
cfg.initialise("save", debug=True)
#cfg.add("player", "name#game_time")


def quit_game():
    pygame.quit()
    sys.exit()


#  Window Setup
mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption("Factory Idle")
screen = pygame.display.set_mode((1280, 800), 0, 32)
font = pygame.font.SysFont(None, 20)


def load_game():  # Loading Screen
    while True:
        screen.fill((155, 0, 0))
        pygame.display.update()
        time.sleep(2)
        main_menu()


# Import Classes
Spieler = Player()  # Player class





def quit_no_save():
    pygame.quit()
    sys.exit()


def quit_save():
    Spieler.save_game()
    pygame.quit()
    sys.exit()






def main_menu():
    left_click = False
    asset = "Resources/Asset/menu_bg.png"
    user_profile = cfg.get("player", "name")  # Get Username from CFG

    while True:
        mx, my = pygame.mouse.get_pos()  # track mouse position
        screen.fill((0, 0, 0))
        screen.blit(pygame.image.load(asset), (0, 0))  # background image

        # Menu Buttons
        game_btn = pygame.Rect(501, 350, 210, 55)
        stats_btn = pygame.Rect(501, 450, 210, 55)
        settings_btn = pygame.Rect(501, 550, 210, 55)
        exit_btn = pygame.Rect(501, 650, 210, 55)

        if debug:
            pygame.draw.rect(screen, (255, 0, 0), game_btn)
            pygame.draw.rect(screen, (255, 0, 0), stats_btn)
            pygame.draw.rect(screen, (255, 0, 0), settings_btn)
            pygame.draw.rect(screen, (0, 0, 0), exit_btn)

        # TODO SET POS
        if user_profile != "":
            sobj.draw_text("Fortsetzen", (0, 0, 0), 501, 350, screen)
        else:
            sobj.draw_text("Start", (0, 0, 0), 501, 350, screen)

        # Handle Button Press
        if game_btn.collidepoint((mx, my)):
            if left_click:
                game()  # start game
        if stats_btn.collidepoint((mx, my)):
            if left_click:
                show_stats()  # show stats
        if settings_btn.collidepoint((mx, my)):
            if left_click:
                options_menu()  # show settings
        if exit_btn.collidepoint((mx, my)):
            if left_click:
                quit_game()
        left_click = False

        # Event Handler
        for event in pygame.event.get():
            if event.type == QUIT:
                quit_game()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit_game()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    left_click = True

        pygame.display.update()
        mainClock.tick(30)


def options_menu():
    scroll_pos = [0, 0]
    scroll_speed = 10  # TODO add scroll speed to options
    click_left = False
    click_right = False
    asset = "Resources/Asset/options_bg_new.png"
    asset_ok = "Resources/Asset/buttons/ok_btn.png"
    asset_abort = "Resources/Asset/buttons/abort_btn.png"

    while True:
        mx, my = pygame.mouse.get_pos()  # track mouse position
        mouse = pygame.mouse.get_pos()
        screen.fill((0, 0, 0))
        screen.blit(pygame.image.load(asset), (0, 0))  # background image

        bgm = opt()  # background Music Toggle
        bgm.name = "bgm"
        bgm.button(screen, mouse)
        if bgm.hover:
            if click_left:
                bgm.toggle()
                if debug:
                    print("bgm_toggle pressed")

        eff = opt()  # Sound Effects Toggle
        eff.name = "eff"
        eff.position_y += 40
        eff.button(screen, mouse)
        if eff.hover:
            if click_left:
                eff.toggle()
                if debug:
                    print("eff_toggle pressed")




        buy_worker_btn = pygame.Rect(501, 650, 210, 55)
        pygame.draw.rect(screen, (255, 0, 0), buy_worker_btn)
        if buy_worker_btn.collidepoint((mx, my)):
            if click_left:

                print("click")

        # Event handler
        click_left = False
        click_right = False

        scroll_area = pygame.Rect(50, 50, 500, 700)

        for event in pygame.event.get():
            if event.type == QUIT:
                Spieler.save_game()
                quit_no_save()

            if event.type == KEYDOWN:  # ESC -> Ingame Menu
                if event.key == K_ESCAPE:
                    ingame_menu()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    click_left = True

                if event.button == 3:  # Right Click
                    click_right = True

                if event.button == 4:  # Scroll down
                    if scroll_area.collidepoint((mx, my)):
                        scroll_pos[1] -= scroll_speed

                if event.button == 5:  # Scroll up
                    if scroll_area.collidepoint((mx, my)):
                        scroll_pos[1] += scroll_speed

        print(scroll_pos)
        # pygame.draw.rect(screen, (255, 0, 0), scroll_area)  # Show on screen DEBUG
        pygame.display.update()
        mainClock.tick(5)



def show_stats():
    # TODO Rework
    # savegame.check_savegame()  # Get Savegame

    # total_starts = savegame.get("total_starts")
    # total_balance = savegame.get("total_balance")
    # money_spend = savegame.get("money_spend")
    # money_received = savegame.get("money_received")
    # total_resets = savegame.get("total_resets")
    # total_workers = savegame.get("total_workers")
    # total_mechanics = savegame.get("total_mechanics")
    # total_vehicles = savegame.get("total_vehicles")

    while True:
        screen.fill((0, 0, 0))
        # background image
        screen.blit(pygame.image.load("Resources/Asset/stats_bg.png"), (0, 0))
        # draw_text(f"Spielzeit: {time_played}", font, (0, 0, 0), 160, 130)
        # draw_text(f"Spielstarts: {total_starts}", font, (0, 0, 0), 160, 150)
        # draw_text(f"Geld Insgesamt: {total_balance}", font, (0, 0, 0), 160, 170)
        # draw_text(f"Geld ausgegeben: {money_spend}", font, (0, 0, 0), 160, 190)
        # draw_text(f"Geld erhalten: {money_received}", font, (0, 0, 0), 160, 210)
        # draw_text(f"{total_resets} mal Neu gestartet.", font, (0, 0, 0), 160, 230)
        # draw_text(f"Arbeiter: {total_workers}", font, (0, 0, 0), 160, 250)
        # draw_text(f"Machienen: {total_mechanics}", font, (0, 0, 0), 160, 270)
        # draw_text(f"Fahrzeuge: {total_vehicles}", font, (0, 0, 0), 160, 290)

        for event in pygame.event.get():  # Event handler
            if event.type == QUIT:
                quit_no_save()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    menu()

        pygame.display.update()
        mainClock.tick(60)


def show_options():
    #  TODO load options
    while True:
        screen.fill((0, 0, 0))
        # background image
        screen.blit(pygame.image.load("Resources/Asset/options_bg.png"), (0, 0))
        # TODO add input for username

        for event in pygame.event.get():  # Event handler
            if event.type == QUIT:
                quit_no_save()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    menu()
        pygame.display.update()
        mainClock.tick(30)










def game():
    scroll_pos = [0, 0]
    scroll_speed = 10  # TODO add scroll speed to options
    click_left = False
    click_right = False

    while True:
        mx, my = pygame.mouse.get_pos()  # track mouse position
        screen.fill((0, 0, 0))
        screen.blit(pygame.image.load("Resources/Asset/game_bg.png"), (0, 0))  # Load Game Background

        player_panel = RPanel()  # Right Top Panel
        player_panel.show(screen, Spieler)

        worker = LPanel()  # Left Panel "Worker"
        worker.mouse = pygame.mouse.get_pos()
        worker.show(screen, scroll_pos)

        if worker.hover == 1:
            if click_left:
                print("Bought 1")
        if worker.hover == 2:
            if click_left:
                print("Bought 10")



        fabric = LPanel()
        fabric.y_offset = 110
        fabric.show(screen, scroll_pos)


        #sobj.render_worker(screen, Spieler, scroll_pos)

        #sobj.draw_text(f'{Spieler.worker}', font, (255, 255, 255), 800, 50, screen)



        # Buy Button
        buy_worker_btn = pygame.Rect(501, 650, 210, 55)

        pygame.draw.rect(screen, (255, 0, 0), buy_worker_btn)
        if buy_worker_btn.collidepoint((mx, my)):
            if click_left:
                bought = Spieler.buy_worker()
                print(bought)

        Spieler.worker_work()
        Spieler.save_game()


        # Event handler
        click_left = False
        click_right = False

        scroll_area = pygame.Rect(50, 50, 500, 700)

        for event in pygame.event.get():
            if event.type == QUIT:
                Spieler.save_game()
                quit_no_save()

            if event.type == KEYDOWN:  # ESC -> Ingame Menu
                if event.key == K_ESCAPE:
                    ingame_menu()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    click_left = True

                if event.button == 3:  # Right Click
                    click_right = True

                if event.button == 4:  # Scroll down
                    if scroll_area.collidepoint((mx, my)):
                        scroll_pos[1] -= scroll_speed

                if event.button == 5:  # Scroll up
                    if scroll_area.collidepoint((mx, my)):
                        scroll_pos[1] += scroll_speed

        print(scroll_pos)
        #pygame.draw.rect(screen, (255, 0, 0), scroll_area)  # Show on screen DEBUG
        pygame.display.update()
        mainClock.tick(30)


def ingame_menu():
    # TODO ingame menü schreiben ? abfrage speichern/ quit
    click = False
    while True:
        mx, my = pygame.mouse.get_pos()  # track mouse position

        screen.fill((0, 0, 0))
        # background image
        screen.blit(pygame.image.load("Resources/Asset/ingame_menu.png"), (0, 0))
        # Create Button
        resume_btn = pygame.Rect(501, 450, 210, 55)
        save_btn = pygame.Rect(501, 550, 210, 55)
        exit_btn = pygame.Rect(501, 650, 210, 55)
        # Draw Button
        # pygame.draw.rect(screen, (255, 0, 0), resume_btn)
        # pygame.draw.rect(screen, (255, 0, 0), save_btn)
        # pygame.draw.rect(screen, (255, 0, 0), exit_btn)

        sobj.draw_text('pause menu', (255, 255, 255), 20, 20, screen)

        if save_btn.collidepoint((mx, my)):
            if click:
                # save game & exit
                print("save")
                quit_save()
        if resume_btn.collidepoint((mx, my)):
            if click:
                # show stats
                game()

        if exit_btn.collidepoint((mx, my)):
            if click:
                quit_no_save()
        click = False

        for event in pygame.event.get():  # Event handler
            if event.type == QUIT:
                quit_no_save()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    game()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


load_game()

import json
import pygame
from Resources.ez_config import ez_config

cfg = ez_config()
cfg.initialise("options.txt", debug=False)
profile = ez_config()
profile.initialise("profile.json", debug=False)

#cfg.add("OPTIONS", "bgm#eff")

file_path = "savegame2"


def save(file):  # Save data to savegame
    with open(file_path, "w") as f:
        json.dump(file, f, indent=2)


def get(category, request):  # get data from savegame
    with open(file_path, "r") as f:
        data = json.load(f)
        saved = data[str(category)][request]
        return saved


class Player:
    # setup defaults
    name = ""
    playtime = 0
    coins = 0
    gems = 0
    # Basic
    base_income = 1


    def __init__(self):
        # setup the class
        p = "PLAYER"
        try:
            # if found get values
            self.name = profile.get(p, "name")
            self.playtime = profile.get(p, "playtime")
            self.coins = profile.get(p, "coins")
            self.gems = profile.get(p, "gems")

        except KeyError:
            # add if not found
            profile.add(p, "name#playtime#coins#gems")

    def save_game(self):
        p = "PLAYER"
        profile.edit(p, "name", self.name)
        profile.edit(p, "playtime", self.playtime)
        profile.edit(p, "coins", self.coins)
        profile.edit(p, "gems", self.gems)


class worker:
    name = ""
    base_price = 0
    price_multi = 0
    amt = 0
    lvl = 0

    def __init__(self):
        while True:
            try:
                # Load Player Data
                self.base_price = get(self.name, "base_price")
                self.price_multi = get(self.name, "price_multi")
                self.amt = get(self.name, "amt")
                self.lvl = get(self.name, "lvl")

            except FileNotFoundError:
                with open(file_path, "w") as f:
                    f.write("{\n\n}")

            except KeyError:
                with open(file_path, "r") as f:
                    file = json.load(f)
                    file[self.name] = {}
                    file[self.name]["base_price"] = 0
                    file[self.name]["price_multi"] = 0
                    file[self.name]["amt"] = 0
                    file[self.name]["lvl"] = 0
                    save(file)
            break


class opt:
    name = ""
    # Import Assets
    asset_ok = "Resources/Asset/buttons/ok_btn.png"
    asset_abort = "Resources/Asset/buttons/abort_btn.png"
    # Positions
    position_x = 340
    position_y = 305
    dimension = 50
    # Values
    hover = False
    status = False
    debug = False
    static_cfg = "OPTIONS"
    # bar
    bar_value = 1
    area = ""
    bar_width = 100

    def data(self):
        self.status = cfg.get(self.static_cfg, self.name)

    def button(self, screen, mouse):
        self.data()

        opt_btn = pygame.Rect(self.position_x, self.position_y, self.dimension, self.dimension)  # set Button

        if self.status:
            screen.blit(pygame.image.load(self.asset_ok), (self.position_x, self.position_y))

        else:
            screen.blit(pygame.image.load(self.asset_abort), (self.position_x, self.position_y))

        if opt_btn.collidepoint((mouse[0], mouse[1])):  # Check if mouse hover
            self.hover = True

        if self.debug:
            pygame.draw.rect(screen, (0, 155, 0), opt_btn)  # Draw if debug
        # TODO REFACTOR TOGGLE btn.toggle

    def toggle(self):
        if self.status:
            status = False
            cfg.edit(self.static_cfg, self.name, status)  # Save cfg

        if not self.status:
            status = True
            cfg.edit(self.static_cfg, self.name, status)  # Save cfg

    def bar(self, screen, mouse):
        from Resources.Asset.animation.animation import bar_animation
        self.data()


        screen.blit((bar_animation[self.bar_value]), (self.position_x, self.position_y))

        self.area = pygame.Rect(self.position_x, self.position_y, self.bar_width, self.dimension)  # set Bar
       # pygame.draw.rect(screen, (0, 155, 0), self.area)  # Draw if debug

        if self.area.collidepoint((mouse[0], mouse[1])):  # Check if mouse hover
            self.hover = True

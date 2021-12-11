import json
import pygame
from Resources.ez_config import ez_config

cfg = ez_config()
cfg.initialise("options.txt", debug=True)

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
    name = ""
    money = 0
    gems = 0
    playtime = 0

    def __init__(self):
        while True:
            try:
                # Load Player Data
                self.name = get("player", "name")
                self.money = get("player", "money")
                self.gems = get("player", "gems")
                self.playtime = get("player", "playtime")

            except FileNotFoundError:
                with open(file_path, "w") as f:
                    f.write("{\n\n}")

            except KeyError:
                with open(file_path, "r") as f:
                    file = json.load(f)
                    file[str("player")] = {}
                    file[str("player")]["name"] = ""
                    file[str("player")]["money"] = 0
                    file[str("player")]["gems"] = 0
                    file[str("player")]["playtime"] = 0
                    save(file)
            break


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

    def data(self):
        self.status = cfg.get(self.static_cfg, self.name)
        print("call")

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

    def toggle(self):
        if self.status:
            status = False
            cfg.edit(self.static_cfg, self.name, status)  # Save cfg

        if not self.status:
            status = True
            cfg.edit(self.static_cfg, self.name, status)  # Save cfg

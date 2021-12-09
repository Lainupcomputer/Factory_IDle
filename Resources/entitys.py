import json

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
                self.playtime = get("player", "playtime" )

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



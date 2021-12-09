import json
import pygame

file_path = "Savegame"


def save(file):  # Save data to savegame
    with open(file_path, "w") as f:
        json.dump(file, f, indent=2)


def get(category, request):  # get data from savegame
    with open(file_path, "r") as f:
        data = json.load(f)
        saved = data[str(category)][request]
        return saved


class Player:
    # Variable
    # PLAYER
    money = 0
    gems = 0
    # WORKER
    worker = 1
    worker_lvl = 1
    worker_earnings = 0
    next_worker_price = 0

    def __init__(self):
        while True:
            try:
                # Load Player Data
                self.money = get(category="player", request="money")
                self.gems = get(category="player", request="gems")
                self.worker = get(category="worker", request="worker")
                self.worker_lvl = get(category="worker", request="worker_lvl")
                self.worker_earnings = get(category="worker", request="worker_earnings")
                self.next_worker_price = 0
            except FileNotFoundError:
                with open(file_path, "w") as f:
                    f.write("{\n\n}")

            except KeyError:
                with open(file_path, "r") as f:
                    file = json.load(f)
                    file[str("player")] = {}
                    file[str("player")]["money"] = 0
                    file[str("player")]["gems"] = 0
                    file[str("worker")] = {}
                    file[str("worker")]["worker"] = 1
                    file[str("worker")]["worker_lvl"] = 1
                    file[str("worker")]["worker_earnings"] = 0
                    file[str("worker")]["next_worker_price"] = 0
                    save(file)

            break

    def save_game(self):  # Save all Game date
        with open(file_path, "r") as f:
            file = json.load(f)
            file[str("player")] = {}
            file[str("player")]["money"] = self.money
            file[str("player")]["gems"] = self.gems
            file[str("worker")] = {}
            file[str("worker")]["worker"] = self.worker
            file[str("worker")]["worker_lvl"] = self.worker_lvl
            file[str("worker")]["worker_earnings"] = self.worker_earnings
            file[str("worker")]["next_worker_price"] = self.next_worker_price
            save(file)

    def worker_work(self):
        multi = self.worker_lvl / 1000
        worker_earnings = self.worker * multi
        self.money += worker_earnings
        self.worker_earnings += worker_earnings
        return self.money

    def buy_worker(self):
        self.next_worker_price = self.worker * 1.33
        if self.money >= self.next_worker_price:
            self.worker += 1
            self.money = self.money - self.next_worker_price
            bought = True
            return bought, self.next_worker_price, self.money, self.worker,
        if self.money <= self.next_worker_price:
            bought = False
            return bought, self.next_worker_price



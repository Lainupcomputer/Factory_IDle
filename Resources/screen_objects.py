import pygame
# Helper


def draw_game_numbers(text, color, x, y, surface):  # Draw generic Numbers
    font = pygame.font.SysFont("comicsansms", 20)
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def draw_text(text, color, x, y, surface):  # draw on screen
    font = pygame.font.SysFont(None, 20)
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def render_cur_panel(screen, Spieler):
    screen.blit(pygame.image.load("Resources/Asset/player_bg.png"), (0, 0))
    round_money = round(Spieler.money, 4)
    draw_game_numbers(f'{round_money}', (255, 255, 255), 1030, 40, screen)  # TODO Change screen location
    draw_game_numbers(f'{Spieler.gems}', (255, 255, 255), 1030, 70, screen)




class RPanel:
    Asset = "Resources/Asset/player_bg.png"


    def show(self, screen, Spieler):
        screen.blit(pygame.image.load(self.Asset), (0, 0))
        round_money = round(Spieler.money, 4)
        draw_game_numbers(f'{round_money}', (255, 255, 255), 1030, 40, screen)  # TODO Change screen location
        draw_game_numbers(f'{Spieler.gems}', (255, 255, 255), 1030, 70, screen)


class LPanel:
    Asset = "Resources/Asset/Object_panel.png"
    debug = False
    mouse = (0, 0)
    hover = 0

    base_x = 0
    x_offset = 0
    base_y = 0
    y_offset = 0

    buy_1_btn_x = 250
    buy_1_btn_y = 50
    buy_10_btn_x = 250
    buy_10_btn_y = 5

    def show(self, screen, scroll_offset):
        self.hover = 0
        screen.blit(pygame.image.load(self.Asset), (self.base_x + self.x_offset, self.base_y + self.y_offset + scroll_offset[1]))

        buy_1_btn = pygame.Rect(self.buy_1_btn_x, self.buy_1_btn_y + self.y_offset + scroll_offset[1], 40, 40)
        buy_10_btn = pygame.Rect(self.buy_10_btn_x, self.buy_10_btn_y + self.y_offset + scroll_offset[1], 40, 40)

        if self.debug:
            pygame.draw.rect(screen, (255, 0, 0), buy_1_btn)
            pygame.draw.rect(screen, (0, 211, 0), buy_10_btn)

        if buy_1_btn.collidepoint((self.mouse[0], self.mouse[1])):
            self.hover = 1

        if buy_10_btn.collidepoint((self.mouse[0], self.mouse[1])):
            self.hover = 2


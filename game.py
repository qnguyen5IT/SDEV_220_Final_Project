import pygame
from pygame.locals import *
from screentype import ScreenType
from screen import *
from resources import *
from playerdata import PlayerData

class Game():
    def __init__(self, window):
        self.screen_type = ScreenType.HOME
        self.window = window
        self.clock = pygame.time.Clock()

        self.screen = HomeScreen(self)


    def switch_screen(self, screen_type):

        if self.screen_type == ScreenType.HOME:
            PlayerData.reset_player_game_state()

        # Check if player beat high score.
        elif self.screen_type == ScreenType.GAME:
            PlayerData.check_for_high_score()

        self.screen_type = screen_type

        self.screen.dispose()

        match screen_type:
            case ScreenType.HOME: self.screen = HomeScreen(self)
            case ScreenType.GAME: self.screen = GameScreen(self)
            case ScreenType.DEATH: self.screen = DeathScreen(self)

    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        self.window.blit(img, (x, y))

    def run(self):
        self.window.blit(Resources.BACKGROUND_IMAGE, (0, 0))
        
        if self.screen.update() == False:
            self.__handle_screen_swap()

        self.screen.draw()

        pygame.display.update()

        self.clock.tick(Resources.FPS)

    def __handle_screen_swap(self):
        match self.screen_type:
            case ScreenType.HOME: self.switch_screen(ScreenType.GAME)
            case ScreenType.GAME: self.switch_screen(ScreenType.DEATH)
            case ScreenType.DEATH: self.switch_screen(ScreenType.HOME)

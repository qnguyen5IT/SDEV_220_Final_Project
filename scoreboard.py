import pygame, sys
from pygame.locals import *
from resources import Resources
from playerdata import PlayerData

class Scoreboard:
    def __init__(self, window):
        # Set up variables to use, also where rects will be created at.
        self.window = window

    def update(self):
        # This is where things like collision detection, animations changes, checks to
        # see if the player was hit by a bullet or an alien crashed into them.
        # Scoreboard probably won't have much here other than changing what the text says.
        pass


    def draw(self):
        # This is where the sprites get drawn to the screen.
        img = Resources.TEXT_FONT.render(f"SCORE : {PlayerData.CURRENT_SCORE}", True, (255,255,255))
        self.window.blit(img, (20, 30))

        # .draw_text("SCORE : 0", Resources.TEXT_FONT,(225, 225, 225), 20, 30) #Line to call for the text of the scoreboard

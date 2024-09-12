import pygame, sys
from pygame.locals import *


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
        pass

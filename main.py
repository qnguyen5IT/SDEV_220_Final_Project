# AUTHORS: Anthony Hernandez, Iteoluwakiisi George Olaniyan, Mang Nung, Marcus Ed. Butler, Quang Nguyen
# VERSION: 2024-09-12_R0
# DESCRIPTION: A simple re-creation of Space Invaders.

import pygame, sys
from pygame.locals import *

from game import Game
from resources import *

# Has to run before using most of pygame's cmds.
# Don't honstly know why, but it works.
pygame.init()

# Create the window to draw to.

window = pygame.display.set_mode((Resources.WINDOW_WIDTH, Resources.WINDOW_HEIGHT))
Resources.WINDOW_WIDTH, Resources.WINDOW_HEIGHT = pygame.display.get_surface().get_size()

print((Resources.WINDOW_WIDTH, Resources.WINDOW_HEIGHT))

Resources.BACKGROUND_IMAGE = pygame.image.load('Assets/game_background.png')
Resources.BACKGROUND_IMAGE = pygame.transform.scale(Resources.BACKGROUND_IMAGE, (Resources.WINDOW_WIDTH, Resources.WINDOW_HEIGHT))

Resources.TEXT_FONT = pygame.font.Font("Assets/advanced-led-board-7.regular.ttf", 36)
Resources.SPRITE_SHEET = pygame.image.load('Assets/Sprite_sheet.png').convert_alpha()

game = Game(window)

# Set the text in the title bar.
pygame.display.set_caption("Space Invaders")

""" === MAIN LOOP === """
while True:
    """ == CHECK FOR EVENTS == """
    # Checks for events like key presses, mouse clicks,
    # and things like resizing the window.

    # TODO: We only ever want to run a single event get loop inside main while loop, so we need a single event loop that pools all events into a list and check if event is there

    # for event in pygame.event.get():
        # Check if the user clicked the close button X.
        # if event.type == QUIT:
            # pygame.quit()
            # sys.exit()
            
    game.run()


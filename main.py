# AUTHORS: Marcus Ed. Butler, 
# VERSION: 2024-09-12_R0
# DESCRIPTION: A simple re-creation of Space Invaders.


import pygame, sys
from pygame.locals import *

from player import Player
from alien import Alien
from scoreboard import Scoreboard


# Has to run before using most of pygame's cmds.
# Don't honstly know why, but it works.
pygame.init()


# Create the window the game will be shown in.
# Resolution
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 900
# Create the window to draw to.
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Setup clock speed aka frames per second(FPS)
FPS = 60
clock = pygame.time.Clock()

# Set the text in the title bar.
pygame.display.set_caption("Space Invaders")


# Create the objects.
player = Player(window)
alien = Alien(window)
scoreboard = Scoreboard(window)


""" === MAIN LOOP === """
while True:
    """ == CHECK FOR EVENTS == """
    # Checks for events like key presses, mouse clicks,
    # and things like resizing the window.
    for event in pygame.event.get():
        # Check if the user clicked the close button X.
        if event.type == QUIT:
            # Close the game.
            pygame.quit()
            sys.exit()        


    """ == UPDATE CALLS ==  """
    # This is where things are checked like collisions, did the player
    # get hit by a projectile.
    player.update()
    alien.update()
    scoreboard.update()

    
    """ == DRAW CALLS ==  """
    # Draw the background. this should always run first.
    # Makes the background black.
    # Get weird results if not drawn.
    window.fill((0,0,0))

    # This is where all of the sprites and the score get drawn
    # to the screen.
    player.draw()
    alien.draw()
    scoreboard.draw()

    # Puts everything drawn on to the screen.
    # Needs to be the last thing ran other than FPS.
    # Is the same as pygame.display.flip()
    pygame.display.update()

    # limits the FPS to 60.
    clock.tick(FPS)

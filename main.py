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
WINDOW_WIDTH, WINDOW_HEIGHT = 1920, 1080

# Create the window to draw to.
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

WINDOW_WIDTH, WINDOW_HEIGHT = pygame.display.get_surface().get_size()

#Load the background image
background_image = pygame.image.load('Assets/game_background.png')

background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

#Load the font style
text_font = pygame.font.SysFont("advanced-led-board-7", 30)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    window.blit(img, (x, y))

# Setup clock speed aka frames per second(FPS)
FPS = 60
clock = pygame.time.Clock()

# Set the text in the title bar.
pygame.display.set_caption("Space Invaders")


# Create the objects.
player = Player(window)
alien = Alien(window)
scoreboard = Scoreboard(window)


# Variable to track fullscreen state
fullscreen = False

def toggle_fullscreen():
    global fullscreen, window
    if fullscreen:
        window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # Windowed mode
    else:
        window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # Fullscreen mode
    fullscreen = not fullscreen  # Toggle the state

""" === MAIN LOOP === """
while True:
    """ == CHECK FOR EVENTS == """
    # Checks for events like key presses, mouse clicks,
    # and things like resizing the window.
    for event in pygame.event.get():
        # Check if the user clicked the close button X.
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Exit full screen or close the game on pressing the escape key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                 pygame.quit()
                 sys.exit()
            elif event.key == pygame.K_RETURN and pygame.key.get_mods() & pygame.KMOD_ALT:
                toggle_fullscreen()


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
    window.blit(background_image, (0, 0))

    draw_text("SCORE : 0", text_font,(225, 225, 225), 20, 30) #Line to call for the text of the scoreboard
                                                               

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

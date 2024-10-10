# AUTHORS: Anthony Hernandez, Iteoluwakiisi George Olaniyan, Mang Nung, Marcus Ed. Butler, Quang Nguyen
# VERSION: 2024-09-12_R0
# DESCRIPTION: A simple re-creation of Space Invaders.


import pygame, sys
from pygame.locals import *

from player import Player
from alien import Alien
from scoreboard import Scoreboard
from playerhealth import PlayerHealth
from projectiles import Bullet
from projectiles import Explosion


# Has to run before using most of pygame's cmds.
# Don't honstly know why, but it works.
pygame.init()


# Create the window the game will be shown in.
# Resolution
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
print(pygame.display.list_modes())

# Create the window to draw to.
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

WINDOW_WIDTH, WINDOW_HEIGHT = pygame.display.get_surface().get_size()



        
bullet = Bullet(window)
explosion = Explosion()

explosion_group = pygame.sprite.Group()

#Load the background image
background_image = pygame.image.load('Assets/game_background.png')

background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

#Load player sprite sheet
spritesheet = pygame.image.load('Assets/Sprite_sheet.png').convert_alpha()
# spritesheet = pygame.transform.scale(spritesheet, (WINDOW_WIDTH-580, WINDOW_HEIGHT-480))


#Color for the sprite sheet's background to make it transparent
white_color = (255,255,255)



# Get a frame from the sprite sheet
# 1st frame


#Load the font style
text_font = pygame.font.Font("Assets/advanced-led-board-7.regular.ttf", 36)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    window.blit(img, (x, y))

# Setup clock speed aka frames per second(FPS)
FPS = 60
clock = pygame.time.Clock()

# Set the text in the title bar.
pygame.display.set_caption("Space Invaders")


# Create the objects.
alien_speed = 0
alien = Alien(window, 'Assets/Sprite_sheet.png', 947, 49, 981, 673, 30, 20, 2, 0)
alien.create_aliens(row_amount=5)
scoreboard = Scoreboard(window)
health = PlayerHealth(text_font, 3)
#Create a Player object(pass both window and spritesheet)
player = Player(window, spritesheet, white_color)

# Starting positions of aliens. 
alien_x = 20
alien_y = 20


# Starting point of the ship
ship_x = 400
ship_y = 500


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
                pygame.display.toggle_fullscreen()

            # Player Controls
            if event.key == pygame.K_RIGHT:
                player.right = True
            if event.key == pygame.K_LEFT:
                player.left = True


        if event.type == pygame.KEYUP:
           # Player Controls
            if event.key == pygame.K_RIGHT:
                player.right = False
            if event.key == pygame.K_LEFT:
                player.left = False
 

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            explosion.create(pos[0], pos[1])
            explosion_group.add(explosion)
   



    """ == UPDATE CALLS ==  """
    # This is where things are checked like collisions, did the player
    # get hit by a projectile.
    scoreboard.update()
    player.update()
    alien.update(bullet)

    """ == DRAW CALLS ==  """
    # Draw the background. this should always run first.
    # Makes the background black.
    # Get weird results if not drawn.
    window.blit(background_image, (0, 0))


    explosion_group.draw(window)
    explosion_group.update()





    draw_text("SCORE : 0", text_font,(225, 225, 225), 20, 30) #Line to call for the text of the scoreboard
                                                               
    # This is where all of the sprites and the score get drawn
    # to the screen.
    ship_x += 1
    # window.blit(frame, (ship_x,ship_y))
    scoreboard.draw()
    alien.draw()
    player.draw()
    health.draw(window)
    bullet.update()

    # Puts everything drawn on to the screen.
    # Needs to be the last thing ran other than FPS.
    # Is the same as pygame.display.flip()
    pygame.display.update()

    # limits the FPS to 60.
    clock.tick(FPS)

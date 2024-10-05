# AUTHORS: Anthony Hernandez, Iteoluwakiisi George Olaniyan, Mang Nung, Marcus Ed. Butler, Quang Nguyen
# VERSION: 2024-09-12_R0
# DESCRIPTION: A simple re-creation of Space Invaders.


import pygame, sys
from pygame.locals import *

from player import Player
from alien import Alien
from scoreboard import Scoreboard
from playerhealth import PlayerHealth


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

#Create explosion class
class Explosion(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(1, 7):
            img = pygame.image.load(f"img/exp{num}.png")
            img = pygame.transform.scale(img, (100, 100))
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        
    def create(self, x, y):
        self.index = 0
        self.rect.center = [x, y]
        self.counter = 0
    
    def update(self):
        explosion_speed = 4
        #update explosion animation
        self.counter += 1

        if self.counter >= explosion_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

        #if the animation is complete, reset the animation index
        if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
            self.kill()

explosion = Explosion()

explosion_group = pygame.sprite.Group()

#Load the background image
background_image = pygame.image.load('Assets/game_background.png')

background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

#Load player sprite sheet
spritesheet = pygame.image.load('Assets/Sprite_sheet.png').convert_alpha()

#Color for the sprite sheet's background to make it transparent
white_color = (255,255,255)


#Create a Player object(pass both window and spritesheet)
player = Player(window, spritesheet)

# Get a frame from the sprite sheet
frame_0 = player.draw(0, 617, 866, 0.05, white_color) #1st frame

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
alien = Alien(window, 'Assets/Sprite_sheet.png', 947, 49, 981, 673, 50, 75)
scoreboard = Scoreboard(window)
health = PlayerHealth(text_font, 3)


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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            explosion.create(pos[0], pos[1])
            explosion_group.add(explosion)


    """ == UPDATE CALLS ==  """
    # This is where things are checked like collisions, did the player
    # get hit by a projectile.
    scoreboard.update()
    player.update()
    alien.update()

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
    window.blit(frame_0, (400,550))
    scoreboard.draw()
    alien.draw()
    health.draw(window)

    # Puts everything drawn on to the screen.
    # Needs to be the last thing ran other than FPS.
    # Is the same as pygame.display.flip()
    pygame.display.update()

    # limits the FPS to 60.
    clock.tick(FPS)

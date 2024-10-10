import pygame, sys
from pygame.locals import *
from projectiles import Bullet
from projectiles import Explosion
from alien import Alien
from scoreboard import Scoreboard
from playerhealth import PlayerHealth
from player import Player
from resources import *

class Screen:
    def __init__(self, game):
        self.game = game

    def dispose(self):
        pass

    def update(self):
        return True

    def draw(self):
        pass

class HomeScreen(Screen):
    def __init__(self, game):
        Screen.__init__(self, game)
        self.play_button = Resources.TEXT_FONT.render('Play', True, (255, 255, 255))

    def update(self):
        rect = self.play_button.get_rect()
        rect.center = (400, 300)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and pygame.key.get_mods() & pygame.KMOD_ALT:
                    pygame.display.toggle_fullscreen()

                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect.collidepoint(event.pos):
                    return False
        
        return True
    
    def draw(self):
        rect = self.play_button.get_rect()
        rect.center = (400, 300)
        self.game.window.blit(self.play_button, rect)

class GameScreen(Screen):
    def __init__(self, game):
        Screen.__init__(self, game)
        
        self.bullet = Bullet(game.window)
        self.explosion = Explosion()
        self.explosion_group = pygame.sprite.Group()
        self.alien_speed = 0
        self.alien = Alien(game.window, 'Assets/Sprite_sheet.png', 947, 49, 981, 673, 30, 20, 2, 0)
        self.alien.create_aliens(row_amount=5)
        self.scoreboard = Scoreboard(game.window)
        self.health = PlayerHealth(3)
        #Create a Player object(pass both window and spritesheet)
        self.player = Player(game.window, Resources.SPRITE_SHEET, (255, 255, 255))

        self.ship_x = 400
        self.ship_y = 500
        self.alien_x = 20
        self.alien_y = 20

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()


                # Player Controls
                if event.key == pygame.K_RIGHT:
                    self.player.right = True
                if event.key == pygame.K_LEFT:
                    self.player.left = True

            if event.type == pygame.KEYUP:
            # Player Controls
                if event.key == pygame.K_RIGHT:
                    self.player.right = False
                if event.key == pygame.K_LEFT:
                    self.player.left = False
    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                self.explosion.create(pos[0], pos[1])
                self.explosion_group.add(self.explosion)
   
        # This is where things are checked like collisions, did the player
        # get hit by a projectile.
        self.scoreboard.update()
        self.player.update()
        self.alien.update(self.bullet)
        self.explosion_group.update()
        self.bullet.update()

        # WHENEVER PLAYER DIES, RETURN FALSE

        self.ship_x += 1 

        return True

    def draw(self):     
        self.scoreboard.draw()
        self.alien.draw()
        self.player.draw()
        self.explosion_group.draw(self.game.window)
        self.health.draw(self.game.window)

        self.game.draw_text("SCORE : 0", Resources.TEXT_FONT,(225, 225, 225), 20, 30) #Line to call for the text of the scoreboard

    def dispose(self):
        self.alien.dispose()
        self.player.dispose()
        self.bullet.dispose()
        self.explosion.dispose()
         
class DeathScreen(Screen):
    def __init__(self, game):
        Screen.__init__(self, game)
        self.play_button = Resources.TEXT_FONT.render('Return', True, (255, 255, 255))

    def update(self):
        rect = self.play_button.get_rect()
        rect.center = (400, 300)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect.collidepoint(event.pos):
                    return False
        
        return True
    
    def draw(self):
        rect = self.play_button.get_rect()
        rect.center = (400, 300)
        self.game.window.blit(self.play_button, rect)

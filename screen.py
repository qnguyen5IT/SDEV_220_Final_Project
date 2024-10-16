import pygame, sys
from pygame.locals import *
from projectiles import Bullet
from projectiles import Explosion
from alien import Alien
from scoreboard import Scoreboard
from playerhealth import PlayerHealth
from player import Player
from resources import *
from playerdata import PlayerData

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

                elif event.key == pygame.K_ESCAPE:
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


                # Player Controls (keydown)
                if event.key == pygame.K_RIGHT:
                    self.player.right = True
                if event.key == pygame.K_LEFT:
                    self.player.left = True
                ## Fire button
                if event.key == pygame.K_SPACE:
                    self.player.fire = True

            if event.type == pygame.KEYUP:
                # Player Controls (keyup)
                if event.key == pygame.K_RIGHT:
                    self.player.right = False
                if event.key == pygame.K_LEFT:
                    self.player.left = False
    
   
        # This is where things are checked like collisions, did the player
        # get hit by a projectile.
        self.scoreboard.update()
        self.player.update(self.health, self.bullet)
        self.alien.update(self.bullet)
        self.explosion_group.update()
        self.bullet.update(self.player, self.health, self.explosion, self.explosion_group, self.alien)

        self.ship_x += 1 

        return not PlayerData.GAME_OVER

    def draw(self):     
        self.scoreboard.draw()
        self.alien.draw()
        self.player.draw()
        self.explosion_group.draw(self.game.window)
        self.health.draw(self.game.window)

        

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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    

        
        return True
    
    def draw(self):
        death_text = ""

        if PlayerData.PLAYER_WON:
            death_text = "You Won"
        else:
            death_text = "You Lost"

        death_text_surface = Resources.TEXT_FONT.render(death_text, True, (255, 255, 255))
        best_score_text_surface = Resources.TEXT_FONT.render("Best Score: " + PlayerData.BEST_SCORE.__str__(), True, (255, 255, 255))
        score_text_surface = Resources.TEXT_FONT.render("Score: " + PlayerData.CURRENT_SCORE.__str__(), True, (255, 255, 255))

        rect = self.__set_centered_surface(death_text_surface, (400, 100))
        self.game.window.blit(death_text_surface, rect)

        rect = self.__set_centered_surface(best_score_text_surface, (400, 150))
        self.game.window.blit(best_score_text_surface, rect)
        
        rect = self.__set_centered_surface(score_text_surface, (400, 200))
        self.game.window.blit(score_text_surface, rect)

        rect = self.__set_centered_surface(self.play_button, (400, 300))
        self.game.window.blit(self.play_button, rect)

    def __set_centered_surface(self, surface, pos):
        rect = surface.get_rect()
        rect.center = pos
        return rect

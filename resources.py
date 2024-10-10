import pygame

class Resources:
    game_over = False
    player_won = False
    FPS:int = 60
    WINDOW_WIDTH:int = 800
    WINDOW_HEIGHT:int = 600
    BACKGROUND_IMAGE:pygame.surface.Surface = None
    TEXT_FONT:pygame.font.Font = None
    SPRITE_SHEET:pygame.surface.Surface = None

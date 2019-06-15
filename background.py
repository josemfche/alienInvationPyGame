import pygame
from pygame.sprite import Sprite


class Background(Sprite):

    def __init__(self, ai_game):
    	#call Sprite initializer
    	super().__init__()  
    	self.screen = ai_game.screen
    	self.settings = ai_game.settings
    	self.screen_rect = ai_game.screen.get_rect()

    	self.image = pygame.image.load('images/backg.bmp')
    	self.rect = self.image.get_rect()

    	self.rect.left = self.screen_rect.left


    def blitme(self):
    	"""Draw the ship at its curent location."""
    	self.screen.blit(self.image, self.rect)
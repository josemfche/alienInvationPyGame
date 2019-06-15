import pygame
from pygame.sprite import Sprite



class Alien(Sprite):

	"""Una clase para representar un solo alien de la flota."""

	def __init__(self, ai_game):
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings


		# Cargar imagen de alien y establecer su atributo rectangular.
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()


		#Crear cada alien cerca del borde superior derecho de la pantalla.
		self.rect.x = self.rect.width 
		self.rect.y = self.rect.height 


		#Guardar la posición horizontal exacta del alien.
		self.x = float(self.rect.x)

	def draw_alien(self):
		"""Dibujar el alien en la pantalla"""	
		pygame.draw.rect(self.screen, self.color, self.rect)

	def update(self):
		"""Mover el alien a la izquierda o derecha"""
		self.x += (self.settings.alien_speed * self.settings.fleet_direction)
		self.rect.x = self.x

	def check_edges(self):
		"""Devolver True si el alien toca un borde de la pantalla."""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right or self.rect.left <= 0:
			return True




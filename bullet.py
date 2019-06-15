import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
	"""Clase para manejar las balas disparadas desde la nave"""

	def __init__(self, ai_game):
		"""Crear un objeto bala en la posición actual de la nave."""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = self.settings.bullet_color


		#Crear un rectagulo-bala en (0, 0) y luego colocarlo en la posición correcta.
		self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
		self.rect.midtop = ai_game.ship.rect.midtop


		#Guardar la posición de la bala como un valor decimal.
		self.y = float(self.rect.y)

	def update(self):
		"""Mover la bala hacía arriba de la pantalla"""
		#Actualizar la posición decimal de la bala.
		self.y -= self.settings.bullet_speed
		#Actulizar la posición del rectangulo-bala
		self.rect.y = self.y


	def draw_bullet(self):
		"""Dibujar la bala en la pantalla"""	
		pygame.draw.rect(self.screen, self.color, self.rect)










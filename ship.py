import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	"""Clase para controlar la nave."""

	def __init__(self, ai_game):
		"""inicializar la nave y colocar su posición inicial"""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		# Cargar la imagen de la nave y su atributo rectangular.
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()

		# Colocar cada nueva nave en el fondo y centro de la pantalla.
		self.rect.midbottom = self.screen_rect.midbottom

		# Guardar su pocición inicial como valor decimal.
		self.x = float(self.rect.x)

		#Marcas de movimiento
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""Atualizar la posción de la nave según su marca de movimiento."""
		#Actulizar la posición horizontal de la nave, no el atributo rectangular.
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed  


		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed

		#Actualizar objeto rectangular desde self.x
		self.rect.x = self.x

	def blitme(self):
		"""Dibujar la nave en su posición inicial."""

		self.screen.blit(self.image, self.rect)

	def center_ship(self):
		"""Centrar la nave en la pantalla."""
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)

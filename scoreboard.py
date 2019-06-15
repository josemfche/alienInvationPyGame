import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard:
	"""Clase para reportar la información de puntuación."""

	def __init__(self, ai_game):
		"""Inicializar los procedimientos de puntuaciones."""
		self.ai_game = ai_game
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = ai_game.settings
		self.stats = ai_game.stats

		# Formato de texto para información de puntuación.
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)

		# Preparar las imagenes iniciales de puntuación.
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_ships()


	def prep_score(self):

		"""Convertir la puntuación en una imagen renderizada."""
		rounded_score = round(self.stats.score, -1)
		score_str = "{:,}".format(rounded_score) 
		self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

		# Mostrar la puntuación en la parte superior derecha de la pantalla.
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20

	def prep_high_score(self):
		"""Convertir la puntuación máxima en una imagen renderizada."""
		high_score = round(self.stats.high_score, -1)
		high_score_str = "{:,}".format(high_score)
		self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

		#Centrar la puntuación máxima en la parte superior central de la pantalla.
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.score_rect.top

	def check_high_score(self):
		"""Revisar si hay una nueva puntuación máxima"""
		if self.stats.score > self.stats.high_score:
			self.stats.high_score = self.stats.score
			self.prep_high_score()

	def show_score(self):
		"""Dibujar puntuación y nivel en la pantalla."""
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		self.ships.draw(self.screen)

	def prep_level(self):
		"""Convertir el nivel en una imagen renderizada."""
		level_str = str(self.stats.level)
		self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

		#Colocar el nivel debajo de la puntuación
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom + 10

	def prep_ships(self):
		"""Mostrar cuantas naves quedan."""
		self.ships = Group()
		for ship_number in range(self.stats.ships_left):
			ship = Ship(self.ai_game)
			ship.rect.x = 10 + ship_number * ship.rect.width
			ship.rect.y = 10
			self.ships.add(ship)




		


import pygame
from settings import Settings

class GameStats:
	"""Medir las estadísticas de Alien_invasion."""

	def __init__(self, ai_game):
		"""Inicializar estadísticas."""
		self.settings = ai_game.settings
		self.reset_stats()

		#Empezar juego en estado activo.
		self.game_active = False

		#Puntuación máxima nunca debe ser reiniciada.
		self.high_score = 0


	def reset_stats(self):
		"""Inicializar estadísticas de juego que pueden cambiar durante el juego."""
		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.level = 1
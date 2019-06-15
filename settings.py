

class Settings:
	""" Clase para guardar toda la configuración de alien_invasion."""

	def __init__(self):
		"""Inicializar configuración estática del juego."""

		#Configuración de pantalla
		self.screen_width = 864
		self.screen_height = 576
		self.bg_color = (230, 230, 230)

		# Configuración de balas

		self.bullet_width = 4
		self.bullet_height = 15
		self.bullet_color = (255, 0, 0)
		self.bullets_allowed = 10

		#Configuración del alien
		self.fleet_drop_speed = 10

		#Configiración de la nave
		self.ship_limit = 2

		# Que tan rápido acelera el juego
		self.speedup_scale = 1.1

		# Que tan rápido aumentan los puntos por alien destruido
		self.score_scale = 1.5

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""inicializar configuración que cambia durante el juego."""
		self.ship_speed = 1.1
		self.bullet_speed = 3.0
		self.alien_speed = 1.0

		# Dirección de la flota 1 representa derecha; -1 representa izquierda.
		self.fleet_direction = 1

		# Puntos por alien 
		self.alien_points = 10

	def increase_speed(self):
		"""Incrementar configuración de velocidad."""
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)





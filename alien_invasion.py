import sys 
import pygame
from time import sleep
from settings import Settings	
from ship import Ship
from bullet import Bullet
from alien import Alien
from scoreboard import Scoreboard
from game_stats import GameStats
from pygame.sprite import Sprite
from button import Button
from background import Background

class AlienInvasion:
	"""Clase para manejar todos los módulos y precedimientos"""

	def __init__(self):
		"""Inicializar juego, y crear recursos de juego."""
		pygame.init()
		self.settings = Settings()

		# Código para iniciar juego en pantalla completa
		#self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		#self.settings.screen_width = self.screen.get_rect().width
		#self.settings.screen_height = self.screen.get_rect().height

		self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion - Che")

		# Crear una instancia para almacenar estadísticas del juego.
		# y crear un tablero de puntuación.
		self.stats = GameStats(self)
		self.sb = Scoreboard(self)

		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()

		self._create_fleet()


		#Colocar color de fondo.
		self.bg_color = (self.settings.bg_color)

		# Iniciar alien_invasión en estado activo.
		self.game_active = True

		#Crear el botón "Jugar".

		self.play_button = Button(self, "Jugar")



	def run_game(self):
		"""Iniciar el ciclo principal del juego"""

		while True:
			self._check_events()

			if self.stats.game_active:

				self.ship.update()
				self._update_bullets()
				self._update_aliens()

			self._update_screen()

	def _create_fleet(self):
		"""Crear flota de aliens."""
		#Crear un alien y calcular el número de aliens en una fila.
		#Espacio entre cada alien es igual al ancho de un alien.

		#Hacer un alien.
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		available_space_x = self.settings.screen_width - (2 * alien_width)
		number_aliens_x = available_space_x // (int(2.5) * alien_width)

		#Determinar el número de filas de aliens en la pantalla
		ship_height = self.ship.rect.height
		available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
		number_rows = available_space_y // (int(2.5) * alien_height)

		#Crear una flota completa de aliens
		for row_number in range(number_rows):
			#Calcular espacio para colocar el alien.
			for alien_number in range(number_aliens_x):
				self._create_alien(alien_number, row_number)

	def _create_alien(self, alien_number, row_number):
		"""Crear un alien y colocarlo en la fila. """
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x = alien.x
		alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
		self.aliens.add(alien)

	def _check_fleet_edges(self):
		"""Responder de forma correcta si los aliens alcanzan un borde"""
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
				break
	def _change_fleet_direction(self):
		"""Cambiar la dirección de la flota completa."""
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.fleet_drop_speed
		self.settings.fleet_direction *= -1


	def _check_events(self):
		#Revisar eventos de ratón y teclado
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)

			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_play_button(mouse_pos)

	def _check_play_button(self, mouse_pos):
		"""Empezar un nuevo juego cuando el jugador presiona jugar."""
		button_clicked = self.play_button.rect.collidepoint(mouse_pos)
		if button_clicked and not self.stats.game_active:
			# Reiniciar estadísticas de juego.
			self.settings.initialize_dynamic_settings()
			self.stats.reset_stats()
			self.stats.game_active = True
			self.sb.prep_score()
			self.sb.prep_level()
			self.sb.prep_ships()

			# Eliminar balas y aliens restantes.
			self.aliens.empty()
			self.bullets.empty()

			# Crear nueva flota y centrar la nave .
			self._create_fleet()
			self.ship.center_ship()

			# Esconder el cursor.
			pygame.mouse.set_visible(False)

				

	def _check_keydown_events(self, event):
		"""Responder a presión de alguna tecla."""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		if event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		if event.key == pygame.K_q:
			sys.exit()
		if event.key == pygame.K_SPACE:
			self._fire_bullet()

	def _check_keyup_events(self, event):
		"""Responder a soltar las teclas."""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		if event.key == pygame.K_LEFT:
			self.ship.moving_left = False

	def _fire_bullet(self):
		"""Crear una nueva bala y añadirla al grupo de balas."""
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)


	def _update_screen(self):
		"""Actualizar imágenes en la pantalla, y pasarlas a la pantalla."""
		#Re dibujar la pantalla durante cada ciclo del bucle.
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()

		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.aliens.draw(self.screen)

		# Dibujar la información de puntuación.
		self.sb.show_score()

		#Dibujar en botón jugar si el juego está inactivo.
		if not self.stats.game_active:
			self.play_button.draw_button()
		#Hacer visible la pantalla dibujada más reciente
		pygame.display.flip()

	def _update_bullets(self):
		#Actualizar posición de las balas y eliminar las viejas.

		
		# Eliminar las balas que salen de la pantalla.
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)

		self._check_bullet_alien_collisions()

	def _check_bullet_alien_collisions(self):
		"""Responder a las colisiones de Aliens-Balas."""
		#Remove any bullets and aliens that have collided.
		collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

		if collisions:
			for aliens in collisions.values():
				self.stats.score += self.settings.alien_points * len(aliens)
			self.sb.prep_score()
			self.sb.check_high_score()

		self.bullets.update()

		if not self.aliens:
			#Destruir balas existentes y crear nueva flota.
			self.bullets.empty()
			self._create_fleet()
			self.settings.increase_speed()
		#print(len(self.bullets))

			# Subir nivel
			self.stats.level += 1
			self.sb.prep_level()


	def _ship_hit(self):
		"""Respuesta a la nave siendo golpeada por un alien."""
		if self.stats.ships_left > 0:
			#Decrementar naves restantes, actulizar tabla de puntuación.

			self.stats.ships_left -= 1
			self.sb.prep_ships()

			#Eliminar cualquier bala o alien restante.
			self.aliens.empty()
			self.bullets.empty()

			#Crear una nueva flota y centrar la nave.
			self._create_fleet()
			self.ship.center_ship()
			# Pausa.
			sleep(0.5)
		else: 
			self.stats.game_active = False
			pygame.mouse.set_visible(True)


	def _check_aliens_bottom(self):
		"""Revisar si las naves han llegado al fondo de la pantalla."""
		screen_rect = self.screen.get_rect()
		for alien in self.aliens.sprites():
			if alien.rect.bottom >= screen_rect.bottom:
				# Tratar esto igual como si la nave fuese golpeada.
				self._ship_hit()
				break



	def _update_aliens(self):
		"""Actulizar posiciones de todos en la flota."""

		"""Revisar si la flota está en un borde,
		luego actulizar la posición de todos los aliens en la flota.
		"""

		self._check_fleet_edges()
		self.aliens.update()

		# Buscar colisiones entre la flota y la nave.
		if pygame.sprite.spritecollideany(self.ship, self.aliens):
			self._ship_hit()

		# Revisar si los aliens tocaron el fondo de la pantalla.
		self._check_aliens_bottom()


if __name__ == '__main__':
	#Crear una intancia del juego, correr el juego.

	ai = AlienInvasion()
	ai.run_game()










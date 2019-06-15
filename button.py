import pygame.font


class Button:

	def __init__(self, ai_game, msg):
		"""Inciar atributos del botón."""
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()

		#Colocar dimensiones y propiedades del botón.
		self.width, self.height = 200, 50
		self.button_color = (0, 255, 0)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)

		#Crear el objeto rectangular del botón y centrarlo.
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center

		#El mensaje del botón debe ser preparado una sola vez.
		self._prep_msg(msg) 

	def _prep_msg(self, msg):
		"""Volver el mensaje una imagen y centrarlo sobre el botón."""
		self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		# Dibujar el botón y luego dibujar el texto imagen.
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)




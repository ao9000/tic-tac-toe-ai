import pygame
from game_interface.color import color_to_rgb
from game_interface.pygame_class.rectobj import RectObj


class Rect(RectObj):
    def __init__(self, color, left_top, width_height, width=0):
        super().__init__(left_top, width_height)
        self._color = color_to_rgb(color)
        self._width = width

    def draw_to_screen(self, screen):
        pygame.draw.rect(screen, self._color, self._rect, self._width)

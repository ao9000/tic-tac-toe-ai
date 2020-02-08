import pygame
from game_interface.color import color_to_rgb


class Line:
    def __init__(self, color, start_pos, end_pos, line_width=1):
        self._color = color_to_rgb(color)
        self._start_pos = start_pos
        self._end_pos = end_pos
        self._line_width = line_width
        self._rect = None

    def draw_to_screen(self, screen):
        self._rect = pygame.draw.line(screen, self._color, self._start_pos, self._end_pos, self._line_width)

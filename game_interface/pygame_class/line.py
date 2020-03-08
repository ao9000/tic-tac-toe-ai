"""
    This is a class made from Pygame.draw.line object
    Pygame.draw.line object is for drawing lines in the pygame window

    More documentation can be found at the pygame official documentation
    https://www.pygame.org/docs/ref/draw.html#pygame.draw.line
"""

import pygame
from game_interface.color import color_to_rgb


class Line:
    """
    Pygame.draw.line object adapted into a class for standardisation within the script
    """
    def __init__(self, color, start_pos, end_pos, line_width=1):
        """
        Constructor for Line class

        :param color: type: str
        Color name of the line

        :param start_pos: type: tuple
        X & Y coordinates of the start position of the line being drawn
        Note: The X & Y coordinates start at the top left corner of the window.
        Example: (0, 0) is at the top left corner of the window

        :param end_pos: type: tuple
        X & Y coordinates of the end position of the line being drawn
        Note: The X & Y coordinates start at the top left corner of the window.
        Example: (0, 0) is at the top left corner of the window

        :param line_width: type: int
        Integer representing the thickness of the line.
        Defaults to 1
        """
        self._color = color_to_rgb(color)
        self._start_pos = start_pos
        self._end_pos = end_pos
        self._line_width = line_width
        self._rect = None

    # Getter & setter methods
    @property
    def start_pos(self):
        return self._start_pos

    @property
    def end_pos(self):
        return self._end_pos

    def draw_to_screen(self, screen):
        """
        Renders the line object to pygame window/screen and saves the created rect object

        :param screen: type: pygame.surface
        The surface/screen of the game for displaying purposes
        """
        self._rect = pygame.draw.line(screen, self._color, self._start_pos, self._end_pos, self._line_width)

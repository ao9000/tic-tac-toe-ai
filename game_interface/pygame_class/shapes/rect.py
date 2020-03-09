"""
    This is a class made from Pygame.draw.rect object
    Pygame.draw.rect object is for drawing rectangles in the pygame window

    More documentation can be found at the pygame official documentation
    https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect
"""

import pygame
from game_interface.color import color_to_rgb
from game_interface.pygame_class.rectobj import RectObj


class Rect(RectObj):
    """
    Pygame.draw.rect object adapted into a class for standardisation within the script
    """
    def __init__(self, color, left_top, width_height, width=0):
        """
        Constructor for Rect class

        :param color: type: str
        Color name of the rectangle

        :param left_top: type: tuple
        Tuple of the X & Y coordinates of the left top corner of the rect
        Note: The X & Y coordinates start at the top left corner of the window.
        Example: (0, 0) is at the top left corner of the window

        :param width_height: type: tuple
        Tuple of the width & height of the rect

        :param width: type: int
        Thickness of the lines used to draw the rectangle
        Note: if width = 0, fill the rectangle
        """
        super().__init__(left_top, width_height)
        self._color = color_to_rgb(color)
        self._width = width

    def draw_to_screen(self, screen):
        """
        Renders the rect object to pygame window/screen and saves the created rect object

        :param screen: type: pygame.surface
        The surface/screen of the game for displaying purposes
        """
        self._rect = pygame.draw.rect(screen, self._color, self._rect, self._width)

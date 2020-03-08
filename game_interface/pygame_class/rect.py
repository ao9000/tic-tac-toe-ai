"""
    This is a class made from Pygame.Rect object
    Pygame.Rect object is for storing rectangular coordinates, most of pygame display elements contains a rect object

    More documentation can be found at the pygame official documentation
    https://www.pygame.org/docs/ref/rect.html
"""

import pygame


class Rect:
    """
    Pygame.rect object adapted into a class for standardisation within the script
    """
    def __init__(self, left_top, width_height):
        """
        Constructor for Rect class

        :param left_top: type: tuple
        Tuple of the X & Y coordinates of the left top corner of the rect
        Note: The X & Y coordinates start at the top left corner of the window.
        Example: (0, 0) is at the top left corner of the window

        :param width_height: type: tuple
        Tuple of the width & height of the rect
        """
        self._left_top = left_top
        self._width_height = width_height
        self._rect = pygame.Rect(left_top, width_height)

    # Getter & setter methods
    @property
    def left_top(self):
        return self._left_top

    @property
    def width_height(self):
        return self._width_height

    def get_middle_point_coordinates(self):
        """
        Calculates the (X,Y) coordinates of the middle point in the rect object

        :return: type: tuple
        Tuple containing the X & Y coordinates of the middle point in rect
        """
        # Calculate half width & height
        half_width_height = (value * (1/2) for value in self._width_height)
        return tuple(map(sum, zip(self._left_top, half_width_height)))

    def is_mouse_hover(self, mouse_position):
        """
        Checks if the mouse position is within the X & Y coordinates of the rect object

        :param mouse_position: type: tuple
        Tuple of the mouse X & Y coordinates in pygame window

        :return: type: bool
        True if mouse position is within the rect object, False otherwise
        """
        # Check if mouse pos intersect
        if self._rect.collidepoint(mouse_position):
            return True

        return False

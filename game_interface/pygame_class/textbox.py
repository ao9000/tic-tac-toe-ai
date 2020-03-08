"""
    This is a class made from Pygame.font object
    Pygame.font object is for creating text in textboxes in the pygame window

    More documentation can be found at the pygame official documentation
    https://www.pygame.org/docs/ref/font.html
"""

import pygame
from game_interface.color import color_to_rgb


class Textbox:
    """
    Pygame.font object adapted into a class for standardisation within the script
    """
    def __init__(self, text, text_color, font_name, font_size, center_x, center_y):
        """
        Constructor for the Textbox class

        :param text: type: str
        Text in the textbox to be displayed

        :param text_color: type: str
        Color name of the text to be displayed

        :param font_name: type: str
        Font name of the text to be displayed

        :param font_size: type: int
        Font size of the text to be displayed

        :param center_x: type: int
        Middle X coordinates of the textbox

        :param center_y: type: int
        Middle Y coordinates of the textbox
        """
        self._text = text
        self._text_color = color_to_rgb(text_color)
        self._font_name = font_name
        self._font_size = font_size
        self._center_x = center_x
        self._center_y = center_y
        self._font = self.load_font()
        self._rect = None

    # Getter & setter methods
    @property
    def text_color(self):
        return self._text_color

    @text_color.setter
    def text_color(self, val):
        self._text_color = color_to_rgb(val)

    def load_font(self):
        """
        Detects if the font is supported in pygame.font library. If supported, directly load the font from the library
        else, load the font from a external directory

        :return: type: pygame.font.Font
        The loaded font object
        """
        # Font handler
        # Check if custom font or system font
        if self._font_name not in pygame.font.get_fonts():
            # Load custom font from file
            font = pygame.font.Font("game_interface/fonts/{}.ttf".format(self._font_name), self._font_size)
        else:
            # Load system font
            font = pygame.font.SysFont(self._font_name, self._font_size)

        return font

    def create_textbox(self):
        """
        Render the textbox with all provided configurations onto a new surface

        :return: type: pygame.surface
        pygame.surface that contains the rendered textbox
        """
        # Render text on new surface
        text = self.load_font().render(self._text, True, self._text_color)

        return text

    def is_mouse_hover(self, mouse_position):
        """
        Checks if the mouse position is within the X & Y coordinates of the textbox object

        :param mouse_position: type: tuple
        Tuple of the mouse X & Y coordinates in pygame window

        :return: type: bool
        True if mouse position is within the rect object, False otherwise
        """
        # Get text width & height
        width, height = self.create_textbox().get_size()

        # Check if mouse is hovering above
        if self._center_x - (width * 1/2) < mouse_position[0] < self._center_x + (width * 1/2) and \
                self._center_y - (height * 1/2) < mouse_position[1] < self._center_y + (height * 1/2):
            return True

        return False

    def draw_to_screen(self, screen):
        """
        Blit/copy the created textbox onto the pygame window

        :param screen: type: pygame.surface
        The surface/screen of the game for displaying purposes
        """
        text = self.create_textbox()

        # Render surface to screen & define rect
        self._rect = screen.blit(text, (self._center_x - (text.get_width() // 2), self._center_y - (text.get_height() // 2)))

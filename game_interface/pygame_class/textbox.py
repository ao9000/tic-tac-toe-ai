import pygame
from game_interface.color import color_to_rgb
from game_interface.pygame_class.rect import Rect


class Textbox(Rect):
    def __init__(self, text, text_color, font_name, font_size, x, y):
        self._text = text
        self._text_color = color_to_rgb(text_color)
        self._font_name = font_name
        self._font_size = font_size
        self._x = x
        self._y = y
        self._rect = None

    # Getter & setter methods
    @property
    def text_color(self):
        return self._text_color
    
    @text_color.setter
    def text_color(self, val):
        self._text_color = color_to_rgb(val)

    def load_font(self):
        # Font handler
        # Check if custom font or system font
        if self._font_name not in pygame.font.get_fonts():
            # Load custom font from file
            font = pygame.font.Font(self._font_name, self._font_size)
        else:
            # Load system font
            font = pygame.font.SysFont(self._font_name, self._font_size)

        return font

    def draw_to_screen(self, screen):
        # Render text on new surface
        text = self.load_font().render(self._text, True, self._text_color)

        # Render surface to screen & define rect
        self._rect = screen.blit(text, (self._x - (text.get_width() // 2), self._y - (text.get_height() // 2)))

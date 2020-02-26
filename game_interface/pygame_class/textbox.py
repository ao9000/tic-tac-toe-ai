import pygame
from game_interface.color import color_to_rgb


class Textbox:
    def __init__(self, text, text_color, font_name, font_size, center_x, center_y):
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
        # Font handler
        # Check if custom font or system font
        if self._font_name not in pygame.font.get_fonts():
            # Load custom font from file
            font = pygame.font.Font(self._font_name, self._font_size)
        else:
            # Load system font
            font = pygame.font.SysFont(self._font_name, self._font_size)

        return font

    def render_text(self):
        # Render text on new surface
        text = self.load_font().render(self._text, True, self._text_color)

        return text

    def draw_to_screen(self, screen):
        text = self.render_text()

        # Render surface to screen & define rect
        self._rect = screen.blit(text, (self._center_x - (text.get_width() // 2), self._center_y - (text.get_height() // 2)))

    def is_mouse_hover(self, mouse_position):
        # Get text width & height
        width, height = self.render_text().get_size()

        # Check if mouse is hovering above
        if self._center_x - (width * 1/2) < mouse_position[0] < self._center_x + (width * 1/2) and \
                self._center_y - (height * 1/2) < mouse_position[1] < self._center_y + (height * 1/2):
            return True

        return False

import pygame


class Rect:
    def __init__(self, left_top, width_height):
        self._left_top = left_top
        self._width_height = width_height
        self._rect = pygame.Rect(left_top, width_height)

    # Getter & setter methods
    @property
    def rect(self):
        return self._rect

    def is_mouse_hover(self):
        # Get mouse position (x,y)
        mouse_position = pygame.mouse.get_pos()

        # Check if mouse pos intersect
        if self._rect.collidepoint(mouse_position):
            return True

        return False

    def is_clicked_on(self, event):
        # Get mouse position (x,y)
        mouse_position = pygame.mouse.get_pos()

        # Get mouse events
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if mouse pos intersect
            if self._rect.collidepoint(mouse_position):
                return True

        return False

import pygame.draw


# noinspection PyArgumentList
class TFigures(object):
    def __init__(self, color, pos, surface, radius):
        self.color = color
        self.pos = pos
        self.surface = surface
        self.radius = radius

    def __del__(self):
        print(f'Figure {self.color} has been deleted')

    def draw(self):
        pygame.draw.circle(self.surface, self.color, self.pos, self.radius, False, False, True, False, True)

    def movement(self, zuege):
        self.pos += zuege
        return self.pos



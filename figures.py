import pygame.draw
from gameboard import Fields, screen
from dictionarys import Color

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


Figures = {'GREEN_F1': TFigures(Color['GREEN'], Fields['GREEN_S_1'], screen, 15),
           'GREEN_F2': TFigures(Color['GREEN'], Fields['GREEN_S_2'], screen, 15),
           'GREEN_F3': TFigures(Color['GREEN'], Fields['GREEN_S_3'], screen, 15),
           'GREEN_F4': TFigures(Color['GREEN'], Fields['GREEN_S_4'], screen, 15),

           'RED_F1': TFigures(Color['RED'], Fields['RED_S_1'], screen, 15),
           'RED_F2': TFigures(Color['RED'], Fields['RED_S_2'], screen, 15),
           'RED_F3': TFigures(Color['RED'], Fields['RED_S_3'], screen, 15),
           'RED_F4': TFigures(Color['RED'], Fields['RED_S_4'], screen, 15),

           'BLUE_F1': TFigures(Color['BLUE'], Fields['BLUE_S_1'], screen, 15),
           'BLUE_F2': TFigures(Color['BLUE'], Fields['BLUE_S_2'], screen, 15),
           'BLUE_F3': TFigures(Color['BLUE'], Fields['BLUE_S_3'], screen, 15),
           'BLUE_F4': TFigures(Color['BLUE'], Fields['BLUE_S_4'], screen, 15),

           'YELLOW_F1': TFigures(Color['DARK_YELLOW'], Fields['YELLOW_S_1'], screen, 15),
           'YELLOW_F2': TFigures(Color['DARK_YELLOW'], Fields['YELLOW_S_2'], screen, 15),
           'YELLOW_F3': TFigures(Color['DARK_YELLOW'], Fields['YELLOW_S_3'], screen, 15),
           'YELLOW_F4': TFigures(Color['DARK_YELLOW'], Fields['YELLOW_S_4'], screen, 15),
           }

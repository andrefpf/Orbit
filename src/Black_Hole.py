from Celestial import Celestial
import math

class Black_Hole(Celestial):
    def __init__(self, x, y):
        size  = 10
        mass  = 2000
        color = (255, 255, 255)
        interation_distance = 30
        Celestial.__init__(self, x, y, mass, size, color, interation_distance)

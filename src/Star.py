from Celestial import Celestial

class Star(Celestial):
    def __init__(self, x, y):
        mass  = 800
        size  = 20
        color = (200, 200, 50)
        interation_distance = 80
        Celestial.__init__(self, x, y, mass, size, color, interation_distance)

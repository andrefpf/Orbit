from Celestial import Celestial

class Star(Celestial):
    def __init__(self, x, y):
        mass  = 100
        size  = 20
        color = (200, 200, 50)
        Celestial.__init__(self, x, y, mass, size, color)

from Celestial import Celestial

class Black_Hole(Celestial):
    def __init__(self, x, y):
        size  = 10
        mass  = 20
        color = (255, 255, 255)
        Celestial.__init__(self, x, y, mass, size, color)
    
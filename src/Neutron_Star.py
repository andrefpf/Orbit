from Celestial import Celestial

class Neutron_Star(Celestial):
    def __init__(self, x, y):
        mass  = 4000
        size  = 20
        color = (50, 200, 255)
        interation_distance = 120
        Celestial.__init__(self, x, y, mass, size, color, interation_distance)

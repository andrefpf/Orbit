from Celestial import Celestial

import math

class Planet(Celestial):
    def __init__(self, x, y):
        color = (50, 100, 200)
        size  = 10
        mass  = 200
        Celestial.__init__(self, x, y, mass, size, color)

        self.throw_velocity = 8
    
    def throw(self, mouse_x, mouse_y):
        x = mouse_x - self.pos_x
        y = self.pos_y - mouse_y
        
        if x == 0:
            x += 1
            
        angulo = math.atan(y/x)

        if mouse_x < self.pos_x:
            angulo += math.pi

        self.velocity_x =  math.cos(angulo) * self.throw_velocity
        self.velocity_y = -math.sin(angulo) * self.throw_velocity
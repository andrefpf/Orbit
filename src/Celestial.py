import pygame
import math

class Celestial:
    def __init__(self, x, y, mass, size, color, interation_distance):
        self.pos_x = x
        self.pos_y = y
        self.mass = mass
        self.size = size
        self.color = color
        self.interation_color = (50, 40, 60)
        self.interation_distance = interation_distance

        self.velocity_x = 0
        self.velocity_y = 0
        self.aceleration_x = 0
        self.aceleration_y = 0

    def show(self, background):
        pygame.draw.circle(background, 
                           self.interation_color, 
                           [int(self.pos_x), int(self.pos_y)], 
                           self.interation_distance,
                           1)

        pygame.draw.circle(background, 
                           self.color, 
                           [int(self.pos_x), int(self.pos_y)], 
                           self.size)
    
    def update(self):
        self.velocity_x += self.aceleration_x 
        self.velocity_y += self.aceleration_y
        self.pos_x += self.velocity_x
        self.pos_y += self.velocity_y

        self.aceleration_x = self.aceleration_y = 0

    def gravity(self, other):
        distance = self.distance(other.pos_x, other.pos_y, self.pos_x, self.pos_y)

        dif_x = other.pos_x - self.pos_x
        dif_y = other.pos_y - self.pos_y

        if distance < other.interation_distance:
            if distance > self.size + other.size:
                force = self.mass * other.mass / distance ** 2
                self.aceleration_x = 2 * (dif_x / distance) * force / self.mass
                self.aceleration_y = 2 * (dif_y / distance) * force / self.mass
    
    def contact(self, other):
        distance = self.distance(other.pos_x, other.pos_y, self.pos_x, self.pos_y)
        if distance <= self.size + other.size:
            return True

    def distance(self, x1, y1, x2, y2):
        a = (x1 - x2)**2
        b = (y1 - y2)**2
        return math.sqrt(a + b)
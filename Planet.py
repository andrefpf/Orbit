import math

class Planet:
    def __init__(self, x, y, mass, color):
        self.pos_x = x
        self.pos_y = y
        self.color = color
        self.mass = mass
        self.size = int(math.sqrt(self.mass))

        self.velocity_x = 0
        self.velocity_y = 0
        self.aceleration_x = 0
        self.aceleration_y = 0

    def show(self, background, pygame):
        pygame.draw.circle(background, self.color, [int(self.pos_x), int(self.pos_y)], self.size)
    
    def update(self):
        self.velocity_x += self.aceleration_x
        self.velocity_y += self.aceleration_y
        self.pos_x += self.velocity_x
        self.pos_y += self.velocity_y

        # print(self.pos_x, self.pos_y)

    def gravity(self, other):
        dif_x = other.pos_x - self.pos_x
        dif_y = other.pos_y -self.pos_y
        distance = math.sqrt(dif_x**2 + dif_y**2)

        if distance > self.size + other.size:
            force = self.mass * other.mass / distance ** 2
            self.aceleration_x = (dif_x / distance) * force / self.mass
            self.aceleration_y = (dif_y / distance) * force / self.mass
        else:
            self.aceleration_x = self.aceleration_y = 0
            self.velocity_x = self.velocity_y = 0
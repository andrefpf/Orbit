import pygame
from Planet import Planet

blue = (50, 100, 200)
grey = (200, 200, 250)

earth = Planet(200, 200, 500, blue)
moon  = Planet(100, 100, 10, grey)

moon.velocity_x = 1
moon.velocity_y = -1

def update():
    earth.show(background, pygame)
    earth.update() 
    earth.gravity(moon)

    moon.show(background, pygame)
    moon.update()
    moon.gravity(earth)
    
background = pygame.display.set_mode((400,400))
pygame.display.set_caption('orbit')
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    background.fill(0)
    update()
    pygame.display.update()
    pygame.time.Clock().tick(30)

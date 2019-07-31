import pygame

# from Main_Menu import Main_Menu
from Game import Game

screen = pygame.display.set_mode((400, 700))
pygame.display.set_caption('orbit')
running = True
level = 0

# menu = Main_Menu(screen)
game = Game(screen, level)
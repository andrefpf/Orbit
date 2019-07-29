import pygame
from Celestial import Celestial
from Game import Game

screen = pygame.display.set_mode((400, 700))
pygame.display.set_caption('orbit')
running = True

game = Game(screen)
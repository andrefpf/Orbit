import pygame
from Celestial import Celestial
from Game import Game

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption('orbit')
running = True

game = Game(screen)
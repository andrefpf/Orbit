import settings
import pygame
import math

from Game import Game

class Main_Menu:
    def __init__(self, screen):
        self.screen = screen
        self.play_pos = (200, 400)
        self.play_size = 80
        self.in_menu = True 
        self.__draw_menu()

        # while self.in_menu:
        #     self.__check_event()

    def __draw_menu(self):
        self.screen.fill((255, 255, 255))
        # pygame.draw.circle(self.screen, (10, 200, 50), self.play_pos, self.play_size)
        # pygame.time.Clock().tick(30)

    def __check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                x1, y1 = event.pos[0], event.pos[1]
                x2, y2 = self.play_pos[0], self.play_pos[1]
                distance = self.distance(x1, y1, x2, y2)

                if distance < self.play_size:
                    game = Game(self.screen, settings.level)
                else:
                    self.in_menu = False
                    
    def distance(self, x1, y1, x2, y2):
        a = (x1 - x2)**2
        b = (y1 - y2)**2
        return math.sqrt(a + b)
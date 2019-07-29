import pygame
import math

from Planet import Planet
from Star import Star
from Black_Hole import Black_Hole

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.in_game = True
        self.FPS = 30

        self.hurled = False

        self.__create_objects()
        self.__game_loop()

    ##
    def __create_objects(self):
        self.earth = self.__create_earth()
        self.stars = self.__create_stars()
        # self.black_hole = self.__create_black_hole()

    def __create_earth(self):
        pos_x, pos_y = 200, 700
        return Planet(pos_x, pos_y)
    
    def __create_stars(self):
        stars_position = [(200, 200)]
        stars = []
        for pos in stars_position:
            pos_x, pos_y = pos[0], pos[1]
            stars.append(Star(pos_x, pos_y))
        return stars

    def __create_black_hole(self):
        pos_x, pos_y = 200, 100
        return Black_Hole(pos_x, pos_y)


    ##
    def __game_loop(self):
        while self.in_game:
            self.__check_events() 
            self.__clear_screen()
            self.__show()
            self.__update()
            self.__gravity_interation()
            self.__set_fps()
            pygame.display.update()

    def __check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.in_game = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos[0], event.pos[1]
                if not self.hurled: self.earth.throw(x, y)
                self.hurled = True

            if event.type == pygame.KEYDOWN and event.unicode == ' ':
                self.__init__(self.screen)
                

    def __clear_screen(self):
        self.screen.fill((10, 0, 20))

    def __show(self):
        self.earth.show(self.screen)
        # self.black_hole.show(self.screen)
        for star in self.stars:
            star.show(self.screen)
    
    def __update(self):
        self.earth.update()
    
    def __gravity_interation(self):
        if self.hurled:
            for i in self.stars:
                self.earth.gravity(i)
            # self.earth.gravity(self.black_hole)

    def __set_fps(self):
        pygame.time.Clock().tick(self.FPS)


import math
import pygame

from Planet import Planet
from Star import Star
from Black_Hole import Black_Hole
from Neutron_Star import Neutron_Star

class Game:
    def __init__(self, screen, level):
        self.screen = screen
        self.level = level
        self.level_data = ''
        self.FPS = 30

        self.in_game = True
        self.hurled = False 

        self.__load_level()
        self.__create_objects()
        self.__load_positions()
        self.__game_loop()

    ##
    def __load_level(self):
        try:
            path = '../data/levels/level_{}.lvl'.format(self.level)
            self.level_data = open(path)
            self.level_data = self.level_data.read().split('\n')
        except:
            self.in_game = False
        
        if self.level_data == ['']:
            self.in_game = False

    def __create_objects(self):
        if self.in_game:
            self.earth = ''
            self.black_hole = ''
            self.stars = []
            self.neutron_stars = []

    def __load_positions(self):
        for data in self.level_data:
            name, x, y = self.__break_data(data)

            if name == 'earth':
                self.earth = Planet(x, y)
            if name == 'black_hole':
                self.black_hole = Black_Hole(x, y)
            if name == 'star':
                self.stars.append(Star(x, y))
            if name == 'neutron_star':
                self.neutron_stars.append(Neutron_Star(x, y))
    
    def __break_data(self, data):
        data = data.split()
        return data[0], int(data[1]), int(data[2])
        

    def __game_loop(self):
        while self.in_game:
            self.__clear_screen()
            self.__check_events() 
            self.__show()
            self.__update()
            self.__gravity_interation()
            self.__set_fps()
            self.__check_game_status()
            pygame.display.update()

    ##
    def __check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.in_game = False

            if event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos[0], event.pos[1]
                if not self.hurled: 
                    self.earth.throw(x, y)
                    self.hurled = True

            if event.type == pygame.KEYDOWN and event.unicode == ' ':
                self.__init__(self.screen, self.level)
                
    def __clear_screen(self):
        self.screen.fill((10, 0, 20))

    def __show(self):
        self.earth.show(self.screen)
        self.black_hole.show(self.screen)
        for star in self.stars:
            star.show(self.screen)
        for star in self.neutron_stars:
            star.show(self.screen)
    
    def __update(self):
        self.earth.update()
    
    def __gravity_interation(self):
        if self.hurled:
            for i in self.stars:
                self.earth.gravity(i)

            for i in self.neutron_stars:
                self.earth.gravity(i)

            self.earth.gravity(self.black_hole)

    def __set_fps(self):
        pygame.time.Clock().tick(self.FPS)

    def __check_game_status(self):
        if self.earth.contact(self.black_hole):
            self.next_level()
            return

        for i in self.stars:
            if self.earth.contact(i):
                self.in_game = False
                return
        
        for i in self.neutron_stars:
            if self.earth.contact(i):
                self.in_game = False
                return

    def next_level(self):
        new_level = self.level + 1
        self.__init__(self.screen, new_level)

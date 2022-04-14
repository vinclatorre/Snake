import pygame
from pygame.sprite import Sprite

class Grid(Sprite):
    '''Background layout'''
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        # Define rows size and distance
        self.rows = 20
        self.size = 600
        self.color = (100,100,100)
        self.distance = self.size / self.rows
        
    def draw(self,x,y):
        '''Draw the lines to make the grid'''
        for i in range(self.rows):
            x += self.distance
            y += self.distance
            pygame.draw.line(self.screen,self.color,(x,0),(x,self.size))
            pygame.draw.line(self.screen,self.color,(0,y),(self.size,y))

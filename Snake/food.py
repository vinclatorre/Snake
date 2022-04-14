import pygame
import random
from pygame.sprite import Sprite

class Food(Sprite):
    '''A class to make food'''

    def __init__(self, game):
        '''Inizialize food and set its position'''
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.score = game.score

        #Create food rect.
        self.x = 30*random.randint(0,19)
        self.y = 30*random.randint(0,19)
        self.rect = pygame.Rect(self.x,self.y,30,30)

    def collision(self, snake):
        '''Manage snake-food collisions'''
        if self.x == snake.x and self.y == snake.y:
            pygame.mixer.Sound.play(self.score)
            self.x = 30*random.randint(0,19)
            self.y = 30*random.randint(0,19)
            snake.x_pos.append(snake.x_pos[-1])
            snake.y_pos.append(snake.y_pos[-1])

        #Set rect x,y positions
        self.rect.x = self.x
        self.rect.y = self.y
        

    def draw(self):
        '''Draw the food'''
        pygame.draw.rect(self.screen,((255,0,0)), self.rect)

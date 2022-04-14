import pygame
from pygame.sprite import Sprite

class Snake(Sprite):
    '''A class to make the snake'''

    def __init__(self, game):
        '''Inizialize the snake and set its starting position'''
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.alive = True
        self.die_sound = game.die_sound
        
        #Create the snake's coordinates and body.
        self.x_pos = [270]
        self.y_pos = [270]
        
        #Movement flag
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False

        #Speed
        self.xspeed = 0
        self.yspeed = 0

    def update(self):
        '''Update snake's position to make it moves'''
        #Compute new head
        self.x, self.y = self.x_pos[0], self.y_pos[0]

        #Update snake position
        self.x = (self.x + self.xspeed)%self.screen_rect.height
        self.y = (self.y + self.yspeed)%self.screen_rect.width

        #Update speed
        if self.yspeed == 0:
            if self.moving_up:
                self.yspeed = -30
                self.xspeed = 0
            if self.moving_down:
                self.yspeed = 30
                self.xspeed = 0
        if self.xspeed == 0:
            if self.moving_right:
                self.xspeed = 30
                self.yspeed = 0
            if self.moving_left:
                self.xspeed = -30
                self.yspeed = 0

        #Add new head at head of lists
        self.x_pos = [self.x] + self.x_pos
        self.y_pos = [self.y] + self.y_pos

        #Delete snake's tail
        del self.x_pos[-1]
        del self.y_pos[-1]

    def die(self):
        '''Kill the snake when it hit itself'''
        if (self.x_pos[0], self.y_pos[0]) in zip(self.x_pos[3:],self.y_pos[3:]):
            self.alive = False
            pygame.mixer.Sound.play(self.die_sound)
            self.reset()

    def reset(self):
        '''Reset snake's position and speed'''
        self.x_pos = [270]
        self.y_pos = [270]
        self.xspeed = 0
        self.yspeed = 0
        
        
    def draw(self):
        '''Draw the snake'''
        for(x,y) in zip(self.x_pos,self.y_pos): 
            pygame.draw.rect(self.screen,((0,255,0)),(x,y,30,30))

        




    
        

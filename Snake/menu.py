import pygame
import sys

class Menu:
    '''Create a menu'''
    def __init__(self, game):
        '''Inizialize menu'''
        pygame.init()
        self.screen = pygame.display.set_mode((600,600))

        #Set fonts and render strings
        self.font = pygame.font.SysFont('8-BIT WONDER', 80, bold = True)
        self.font2 = pygame.font.SysFont('8-BIT WONDER', 50, bold = True)
        self.title = self.font.render('Snake', False, (255,255,255))
        self.normal = self.font2.render('Normal', False, (255,255,255))
        self.hard = self.font2.render('Hard', False, (255,255,255))

        #Arrow to select difficult
        self.sel_height = 245
        self.select = self.font2.render('>', False, (255,255,255))

        #Movement flag
        self.flag = False
        #Starting flag
        self.start = False
        #Difficult flag
        self.difficult = False

    def run(self):
        '''Functions calling'''
        self.check_event()
        self.update_screen()

    def check_event(self):
        '''Manage keypress'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)

    def check_keydown_events(self,event):
        '''Manage arrow movement and select difficult'''
        #Move the arrow
        if event.key == pygame.K_UP and self.flag:
            self.sel_height -= 50
            self.flag = False
        if event.key == pygame.K_DOWN and not self.flag:
            self.sel_height += 50
            self.flag = True

        #Start the game when enter is pressed and set difficult
        if event.key == pygame.K_RETURN:
            if self.flag:
                self.difficult = True
            if not self.flag:
                self.difficult = False
            self.start = True

    def draw(self):
        '''Draw the writings'''
        self.screen.blit(self.title,(200,50))
        self.screen.blit(self.normal,(250,250))
        self.screen.blit(self.hard,(250,300))
        self.screen.blit(self.select,(220,self.sel_height))

    def update_screen(self):
        '''Fill the color, call draw and update functions'''
        self.screen.fill((0,0,20))
        self.draw()
        pygame.display.update()

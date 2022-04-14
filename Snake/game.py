import pygame
import sys
import time
from snake import Snake
from food import Food
from grid import Grid
from menu import Menu


class SnakeGame:
    '''Main class'''
    def __init__(self):
        '''Inizialize the game'''
        pygame.init()
        pygame.mixer.pre_init(44100,-16,2,512)
        self.screen = pygame.display.set_mode((600,600))
        self.clock = pygame.time.Clock()
        self.FPS = 10

        #Sound effect
        self.score = pygame.mixer.Sound('point.wav')
        self.die_sound = pygame.mixer.Sound('dead.wav')
        
        #Game stat
        self.loop = False
        self.snake = Snake(self)
        self.food = Food(self)
        self.grid = Grid(self)
        self.menu = Menu(self)    

    def run_game(self):
        '''Main loop'''
        self.run_menu()
        while self.loop:
            self.game_speed()
            self.clock.tick(self.FPS)
            self.check_events()
            self.snake.update()
            self.food.collision(self.snake)
            self.snake.die()
            self.game_over()
            self.update_screen()

    def run_menu(self):
        '''Menu's loop'''
        while not self.loop:
            self.menu.run()
            if self.menu.start:
                self.loop = True
        
    def check_events(self):
        '''Respond to keypress'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            if event.type == pygame.KEYUP:
                self.check_keyup_events(event)

    def check_keydown_events(self, event):
        '''Key press'''
        if event.key == pygame.K_UP:
            self.snake.moving_up = True
        if event.key == pygame.K_DOWN:
            self.snake.moving_down = True
        if event.key == pygame.K_RIGHT:
            self.snake.moving_right = True
        if event.key == pygame.K_LEFT:
            self.snake.moving_left = True

    def check_keyup_events(self, event):
        '''Key release'''
        if event.key == pygame.K_UP:
            self.snake.moving_up = False
        if event.key == pygame.K_DOWN:
            self.snake.moving_down = False
        if event.key == pygame.K_RIGHT:
            self.snake.moving_right = False
        if event.key == pygame.K_LEFT:
            self.snake.moving_left = False

    def game_over(self):
        if not self.snake.alive:
            self.loop = False
            self.menu.start = False
            self.snake.alive = True
            self.run_menu()

    def game_speed(self):
        '''Change FPS to looks snake run faster or slower'''
        if self.menu.difficult:
            self.FPS = 15
        else:
            self.FPS = 10
                 
    def update_screen(self):
        '''Update rect on the screen'''
        self.screen.fill((0,0,20))
        self.grid.draw(0,0)
        self.snake.draw()
        self.food.draw()
        pygame.display.update()


    
if __name__ == '__main__':
    snake = SnakeGame()
    snake.run_game()

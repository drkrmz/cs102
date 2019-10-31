import pygame
from pygame.locals import *

from life import GameOfLife
from ui import UI


class GUI(UI):

    def __init__(self, life: GameOfLife, cell_size: int=10, speed: int=10) -> None:
        self.cell_size = cell_size
        self.speed = speed
        self.screen = pygame.display.set_mode((life.cols * self.cell_size, life.rows * self.cell_size))
        super().__init__(life)

    def draw_lines(self) -> None:
        """ Отрисовать сетку """
        for x in range(0, life.cols*self.cell_size, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('white'),
                    (x, 0), (x, life.rows*self.cell_size))
        for y in range(0, life.rows*self.cell_size, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('white'),
                    (0, y), (life.cols*self.cell_size, y))

    def draw_grid(self) -> None:
        """
        Отрисовка списка клеток с закрашиванием их в соответствующе цвета.
        """
        for i in range(life.rows):
            for j in range(life.cols):
                if life.curr_generation[i][j] == 1:
                    pygame.draw.rect(self.screen, pygame.Color('Green'), (j*self.cell_size, i*self.cell_size, self.cell_size, self.cell_size))
                else:
                    pygame.draw.rect(self.screen, pygame.Color('Black'), (j*self.cell_size, i*self.cell_size, self.cell_size, self.cell_size))

    def run(self) -> None:
        """ Запустить игру """
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('black'))

        running = True
        pause = False
        while running and not life.is_max_generations_exceed and life.is_changing:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYUP and event.key == K_SPACE:
                    pause = not pause
                elif event.type == MOUSEBUTTONUP and pause == True:
                    j, i = pygame.mouse.get_pos()
                    i = i // self.cell_size
                    j = j // self.cell_size
                    if life.curr_generation[i][j] == 1:
                        life.curr_generation[i][j] = 0
                    else:
                        life.curr_generation[i][j] = 1
           
            self.draw_grid()
            self.draw_lines()
            if pause == False:
                life.step()

            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

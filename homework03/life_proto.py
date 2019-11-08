import pygame
import random

from pygame.locals import *
from typing import List, Tuple


Cell = Tuple[int, int]
Cells = List[int]
Grid = List[Cells]


class GameOfLife:

    def __init__(self, width: int = 640, height: int = 480, cell_size: int = 10, speed: int = 10) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed

    def draw_lines(self) -> None:
        """ Отрисовать сетку """
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                    (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                    (0, y), (self.width, y))

    def run(self) -> None:
        """ Запустить игру """
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))

        # Создание списка клеток
        self.grid = self.create_grid(randomize=True)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_grid()
            self.draw_lines()

            # Отрисовка списка клеток
            # Выполнение одного шага игры (обновление состояния ячеек)
            self.get_next_generation()

            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def create_grid(self, randomize: bool = False) -> Grid:
        """
        Создание списка клеток.
        Клетка считается живой, если ее значение равно 1, в противном случае клетка
        считается мертвой, то есть, ее значение равно 0.
        Parameters
        ----------
        randomize : bool
            Если значение истина, то создается матрица, где каждая клетка может
            быть равновероятно живой или мертвой, иначе все клетки создаются мертвыми.
        Returns
        ----------
        out : Grid
            Матрица клеток размером `cell_height` х `cell_width`.
        """
        self.grid = []
        temp = []
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                if not randomize:
                    temp.append(0)
                else:
                    temp.append(random.randint(0, 1))
                if j == self.cell_width - 1:
                    self.grid.append(temp)
                    temp = []
        return self.grid

    def draw_grid(self) -> None:
        """
        Отрисовка списка клеток с закрашиванием их в соответствующе цвета.
        """
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                if self.grid[i][j] == 1:
                    pygame.draw.rect(self.screen, pygame.Color('Green'), (j*self.cell_size, i*self.cell_size, self.cell_size, self.cell_size))
                else:
                    pygame.draw.rect(self.screen, pygame.Color('White'), (j*self.cell_size, i*self.cell_size, self.cell_size, self.cell_size))

    def get_neighbours(self, cell: Cell) -> Cells:
        """
        Вернуть список соседних клеток для клетки `cell`.
        Соседними считаются клетки по горизонтали, вертикали и диагоналям,
        то есть, во всех направлениях.
        Parameters
        ----------
        cell : Cell
            Клетка, для которой необходимо получить список соседей. Клетка
            представлена кортежем, содержащим ее координаты на игровом поле.
        Returns
        ----------
        out : Cells
            Список соседних клеток.
        """
        neighbours = []
        row, col = cell
        if row-1 >= 0:
            if col-1 >= 0:
                neighbours.append(self.grid[row-1][col-1])
            if col+1 <= self.cell_width-1:
                neighbours.append(self.grid[row-1][col+1])
            neighbours.append(self.grid[row-1][col])
        if row+1 <= self.cell_height-1:
            if col-1 >= 0:
                neighbours.append(self.grid[row+1][col-1])
            if col+1 <= self.cell_width-1:
                neighbours.append(self.grid[row+1][col+1])
            neighbours.append(self.grid[row+1][col])
        if col-1 >= 0:
            neighbours.append(self.grid[row][col-1])
        if col+1 <= self.cell_width-1:
            neighbours.append(self.grid[row][col+1])
        return neighbours

    def get_next_generation(self) -> Grid:
        """
        Получить следующее поколение клеток.
        Returns
        ----------
        out : Grid
            Новое поколение клеток.
        """
        new_grid = []
        temp = []
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                amount = sum(self.get_neighbours((i, j)))
                if self.grid[i][j] == 0:
                    if amount == 3:
                        temp.append(1)
                    else:
                        temp.append(0)
                else:
                    if amount == 2 or amount == 3:
                        temp.append(1)
                    else:
                        temp.append(0)
                if j == self.cell_width-1:
                    new_grid.append(temp)
                    temp = []
        self.grid = new_grid
        return self.grid

if __name__ == '__main__':
    game = GameOfLife(320, 240, 20)
    game.run()
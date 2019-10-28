import pygame
from pygame.locals import *
import random


class GameOfLife:

    def __init__(self, width=640, height=480, cell_size=10, speed=10):
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

    def draw_grid(self):
        """ Отрисовать сетку """
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                    (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                    (0, y), (self.width, y))

    def run(self):
        """ Запустить игру """
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))

        # Создание списка клеток
        self.clist = self.cell_list(randomize=True)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

            # Отрисовка списка клеток
            self.draw_cell_list()
            # Выполнение одного шага игры (обновление состояния ячеек)
            self.clist = self.update_cell_list()

            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def cell_list(self, randomize=True):
        """ Создание списка клеток.

        :param randomize: Если True, то создается список клеток, где
        каждая клетка равновероятно может быть живой (1) или мертвой (0).
        :return: Список клеток, представленный в виде матрицы
        """
        self.clist = []
        temp = []
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                if not randomize:
                    temp.append(0)
                else:
                    temp.append(random.randint(0, 1))
                if j == self.cell_width - 1:
                    self.clist.append(temp)
                    temp = []
        return self.clist

    def draw_cell_list(self, clist):
        """ Отображение списка клеток

        :param rects: Список клеток для отрисовки, представленный в виде матрицы
        """
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                if clist[i][j] == 1:
                    pygame.draw.rect(self.screen, pygame.color('Green'), (j, i, 64, 48))
                else:
                    pygame.draw.rect(self.screen, pygame.color('Black'), (j, i, 64, 48))

    def get_neighbours(self, cell):
        """ Вернуть список соседей для указанной ячейки

        :param cell: Позиция ячейки в сетке, задается кортежем вида (row, col)
        :return: Одномерный список ячеек, смежных к ячейке cell
        """
        neighbours = []
        row, col = cell
        if row-1 >= 0:
            if col-1 >= 0:
                neighbours.append(self.clist[row-1][col-1])
            if col+1 <= self.cell_width-1:
                neighbours.append(self.clist[row-1][col+1])
            neighbours.append(self.clist[row-1][col])
        if row+1 <= self.cell_height-1:
            if col-1 >= 0:
                neighbours.append(self.clist[row+1][col-1])
            if col+1 <= self.cell_width-1:
                neighbours.append(self.clist[row+1][col+1])
            neighbours.append(self.clist[row+1][col])
        if col-1 >= 0:
            neighbours.append(self.clist[row][col-1])
        if col+1 <= self.cell_width-1:
            neighbours.append(self.clist[row][col+1])
        return neighbours

    def update_cell_list(self, cell_list):
        """ Выполнить один шаг игры.

        Обновление всех ячеек происходит одновременно. Функция возвращает
        новое игровое поле.

        :param cell_list: Игровое поле, представленное в виде матрицы
        :return: Обновленное игровое поле
        """
        new_clist = []
        temp = []
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                amount = sum(self.get_neighbours((i, j)))
                if cell_list[i][j] == 0:
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
                    new_clist.append(temp)
                    temp = []
        self.clist = cell_list
        self.clist = new_clist
        return self.clist

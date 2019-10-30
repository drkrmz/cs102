import pathlib
import random
import json

from typing import List, Optional, Tuple


Cell = Tuple[int, int]
Cells = List[int]
Grid = List[Cells]


class GameOfLife:

    def __init__(
        self,
        size: Tuple[int, int],
        randomize: bool = True,
        max_generations: Optional[float] = float('inf')
    ) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.n_generation = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        self.curr_generation = []
        temp = []
        for i in range(self.rows):
            for j in range(self.cols):
                if not randomize:
                    temp.append(0)
                else:
                    temp.append(random.randint(0, 1))
                if j == self.cols - 1:
                    self.curr_generation.append(temp)
                    temp = []
        return self.curr_generation

    def get_neighbours(self, cell: Cell) -> Cells:
        neighbours = []
        row, col = cell
        if row-1 >= 0:
            if col-1 >= 0:
                neighbours.append(self.curr_generation[row-1][col-1])
            if col+1 <= self.cols-1:
                neighbours.append(self.curr_generation[row-1][col+1])
            neighbours.append(self.curr_generation[row-1][col])
        if row+1 <= self.rows-1:
            if col-1 >= 0:
                neighbours.append(self.curr_generation[row+1][col-1])
            if col+1 <= self.cols-1:
                neighbours.append(self.curr_generation[row+1][col+1])
            neighbours.append(self.curr_generation[row+1][col])
        if col-1 >= 0:
            neighbours.append(self.curr_generation[row][col-1])
        if col+1 <= self.cols-1:
            neighbours.append(self.curr_generation[row][col+1])
        return neighbours

    def get_next_generation(self) -> Grid:
        new_grid = []
        temp = []
        for i in range(self.rows):
            for j in range(self.cols):
                amount = sum(self.get_neighbours((i, j)))
                if self.curr_generation[i][j] == 0:
                    if amount == 3:
                        temp.append(1)
                    else:
                        temp.append(0)
                else:
                    if amount == 2 or amount == 3:
                        temp.append(1)
                    else:
                        temp.append(0)
                if j == self.cols-1:
                    new_grid.append(temp)
                    temp = []
        self.curr_generation = new_grid
        return self.curr_generation

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        self.prev_generation = self.curr_generation
        self.get_next_generation()
        self.n_generation += 1

    @property
    def is_max_generations_exceed(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        if self.n_generation < self.max_generations:
            return False
        return True

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        if self.curr_generation == self.prev_generation:
            return False
        return True

    @staticmethod
    def from_file(filename: pathlib.Path) -> 'GameOfLife':
        """
        Прочитать состояние клеток из указанного файла.
        """
        with open(filename, 'r') as f:
            json.load(f)

    def save(self, filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        with open(filename, 'w') as f:
            json.dump(self.curr_generation, f)

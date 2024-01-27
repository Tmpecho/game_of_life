import copy
import random
from dataclasses import dataclass
from typing import List

CELL_LIFE_PROBABILITY: int = 8
EMPTY_CELL: str = " "
FULL_CELL: str = "#"


@dataclass
class Cell:
    row: int
    column: int


def create_random_cell() -> str:
    return FULL_CELL if random.randint(1, CELL_LIFE_PROBABILITY) == 1 else EMPTY_CELL


class Grid:
    def __init__(self, grid_height: int = 40, grid_width: int = 40) -> None:
        self.grid_height: int = grid_height
        self.grid_width: int = grid_width
        self.grid: List[List[str]] = self._create_random_grid

    @property
    def _create_random_grid(self) -> list:
        return [[create_random_cell() for _ in range(self.grid_width)] for _ in range(self.grid_height)]

    def _cell_in_grid(self, cell: Cell) -> bool:
        cell_is_outside_row: bool = cell.row < 0 or cell.row >= self.grid_height
        cell_is_outside_column: bool = cell.column < 0 or cell.column >= self.grid_width

        if cell_is_outside_row or cell_is_outside_column:
            return False
        return True

    def _valid_neighbour(self, grid: List[List[str]], cell: Cell, head_cell: Cell) -> bool:
        if not self._cell_in_grid(cell):
            return False

        if cell == head_cell:
            return False

        return grid[cell.row][cell.column] == FULL_CELL

    def _count_neighbours(self, grid: List[List[str]], head_cell: Cell) -> int:
        return [
            self._valid_neighbour(grid, Cell(row, column), head_cell)
            for row in [head_cell.row - 1, head_cell.row, head_cell.row + 1]
            for column in [head_cell.column - 1, head_cell.column, head_cell.column + 1]
        ].count(True)

    def _update_full_cell(self, cell: Cell, neighbours_count: int) -> None:
        if neighbours_count < 2 or neighbours_count > 3:
            self.grid[cell.row][cell.column] = EMPTY_CELL

    def _update_empty_cell(self, cell: Cell, neighbours_count: int) -> None:
        if neighbours_count == 3:
            self.grid[cell.row][cell.column] = FULL_CELL

    def _update_cell(self, temp_grid: List[List[str]], cell: Cell) -> None:
        neighbours_count: int = self._count_neighbours(temp_grid, cell)

        if temp_grid[cell.row][cell.column] == FULL_CELL:
            self._update_full_cell(cell, neighbours_count)
        else:
            self._update_empty_cell(cell, neighbours_count)

    def update_grid(self) -> list:
        # We have to use deepcopy here, because if we just assign self.grid to temporary_grid,
        # then we will be modifying self.grid as we iterate over it.
        temporary_grid: List[List[str]] = copy.deepcopy(self.grid)

        for row in range(self.grid_height):
            for column in range(self.grid_width):
                self._update_cell(temporary_grid, Cell(row, column))

        return self.grid
import copy

import pytest

from ..grid import Grid, GridUpdater, Cell, EMPTY_CELL, FULL_CELL


@pytest.fixture
def grid():
    return Grid(3, 3)


def test_update_full_cell(grid):
    grid_updater = GridUpdater(grid)
    grid.cell_matrix[0][0] = FULL_CELL
    grid_updater._update_full_cell(Cell(0, 0), 4)
    assert grid.cell_matrix[0][0] == EMPTY_CELL


def test_update_empty_cell(grid):
    grid_updater = GridUpdater(grid)
    grid.cell_matrix[0][0] = EMPTY_CELL
    grid_updater._update_empty_cell(Cell(0, 0), 3)
    assert grid.cell_matrix[0][0] == FULL_CELL


def test_update_cell(grid):
    grid_updater = GridUpdater(grid)
    temp_grid = copy.deepcopy(grid.cell_matrix)
    grid_updater._update_cell(temp_grid, Cell(0, 0))
    assert grid.cell_matrix[0][0] in [EMPTY_CELL, FULL_CELL]


def test_update_grid(grid):
    grid.cell_matrix = [
        [EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
        [FULL_CELL, FULL_CELL, FULL_CELL],
        [EMPTY_CELL, EMPTY_CELL, EMPTY_CELL]
    ]

    expected_grid = [
        [EMPTY_CELL, FULL_CELL, EMPTY_CELL],
        [EMPTY_CELL, FULL_CELL, EMPTY_CELL],
        [EMPTY_CELL, FULL_CELL, EMPTY_CELL]
    ]

    GridUpdater.update_grid(grid)
    assert grid.cell_matrix == expected_grid


def test_update_empty_grid(grid):
    grid.cell_matrix = [
        [EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
        [EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
        [EMPTY_CELL, EMPTY_CELL, EMPTY_CELL]
    ]
    GridUpdater.update_grid(grid)
    assert all(cell == EMPTY_CELL for row in grid.cell_matrix for cell in row)


def test_update_full_grid(grid):
    grid.cell_matrix = [
        [FULL_CELL, FULL_CELL, FULL_CELL],
        [FULL_CELL, FULL_CELL, FULL_CELL],
        [FULL_CELL, FULL_CELL, FULL_CELL]
    ]
    expected_grid = [
        [FULL_CELL, EMPTY_CELL, FULL_CELL],
        [EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
        [FULL_CELL, EMPTY_CELL, FULL_CELL]
    ]
    GridUpdater.update_grid(grid)
    assert grid.cell_matrix == expected_grid

import copy

from ..grid import Grid, GridUpdater, Cell, EMPTY_CELL, FULL_CELL


def test_valid_neighbour():
    grid = Grid(3, 3)
    grid_updater = GridUpdater(grid)
    grid.grid = [
        [FULL_CELL, FULL_CELL, EMPTY_CELL],
        [FULL_CELL, FULL_CELL, EMPTY_CELL],
        [FULL_CELL, EMPTY_CELL, FULL_CELL]
    ]
    assert grid_updater._valid_neighbour(grid.grid, Cell(0, 0), Cell(0, 0)) == False
    assert grid_updater._valid_neighbour(grid.grid, Cell(grid.grid_height, grid.grid_width), Cell(0, 0)) == False


def test_count_neighbours():
    grid = Grid(3, 3)
    grid_updater = GridUpdater(grid)
    grid.grid = [
        [EMPTY_CELL, FULL_CELL, EMPTY_CELL],
        [FULL_CELL, FULL_CELL, FULL_CELL],
        [EMPTY_CELL, FULL_CELL, EMPTY_CELL]
    ]
    assert isinstance(grid_updater._count_neighbours(grid.grid, Cell(0, 0)), int)
    assert grid_updater._count_neighbours(grid.grid, Cell(0, 0)) == 3
    assert grid_updater._count_neighbours(grid.grid, Cell(1, 1)) == 4
    assert grid_updater._count_neighbours(grid.grid, Cell(0, 1)) == 3


def test_update_full_cell():
    grid = Grid()
    grid_updater = GridUpdater(grid)
    grid.grid[0][0] = FULL_CELL
    grid_updater._update_full_cell(Cell(0, 0), 4)
    assert grid.grid[0][0] == EMPTY_CELL


def test_update_empty_cell():
    grid = Grid()
    grid_updater = GridUpdater(grid)
    grid.grid[0][0] = EMPTY_CELL
    grid_updater._update_empty_cell(Cell(0, 0), 3)
    assert grid.grid[0][0] == FULL_CELL


def test_update_cell():
    grid = Grid()
    grid_updater = GridUpdater(grid)
    temp_grid = copy.deepcopy(grid.grid)
    grid_updater._update_cell(temp_grid, Cell(0, 0))
    assert grid.grid[0][0] in [EMPTY_CELL, FULL_CELL]


def test_update_grid():
    grid = Grid(3, 3)
    grid.grid = [
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
    assert grid.grid == expected_grid

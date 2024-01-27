import copy

from ..grid import Grid, Cell, EMPTY_CELL, FULL_CELL


def test_in_grid():
    grid = Grid()
    assert grid._cell_in_grid(Cell(0, 0)) == True
    assert grid._cell_in_grid(Cell(grid.grid_height, grid.grid_width)) == False


def test_valid_neighbour():
    grid = Grid(3, 3)
    grid.grid = [
        [FULL_CELL, FULL_CELL, EMPTY_CELL],
        [FULL_CELL, FULL_CELL, EMPTY_CELL],
        [FULL_CELL, EMPTY_CELL, FULL_CELL]
    ]
    assert grid._valid_neighbour(grid.grid, Cell(0, 0), Cell(0, 0)) == False
    assert grid._valid_neighbour(grid.grid, Cell(grid.grid_height, grid.grid_width), Cell(0, 0)) == False

    # test that for the middle cell, the head cell is not counted as a neighbour, but the rest are
    assert grid._valid_neighbour(grid.grid, Cell(1, 1), Cell(1, 1)) == False
    assert grid._valid_neighbour(grid.grid, Cell(0, 0), Cell(1, 1)) == True
    assert grid._valid_neighbour(grid.grid, Cell(0, 1), Cell(1, 1)) == True
    assert grid._valid_neighbour(grid.grid, Cell(0, 2), Cell(1, 1)) == False
    assert grid._valid_neighbour(grid.grid, Cell(1, 0), Cell(1, 1)) == True
    assert grid._valid_neighbour(grid.grid, Cell(1, 2), Cell(1, 1)) == False
    assert grid._valid_neighbour(grid.grid, Cell(2, 0), Cell(1, 1)) == True
    assert grid._valid_neighbour(grid.grid, Cell(2, 1), Cell(1, 1)) == False
    assert grid._valid_neighbour(grid.grid, Cell(2, 2), Cell(1, 1)) == True


def test_count_neighbours():
    grid = Grid(3, 3)
    grid.grid = [
        [EMPTY_CELL, FULL_CELL, EMPTY_CELL],
        [FULL_CELL, FULL_CELL, FULL_CELL],
        [EMPTY_CELL, FULL_CELL, EMPTY_CELL]
    ]
    assert isinstance(grid._count_neighbours(grid.grid, Cell(0, 0)), int)
    assert grid._count_neighbours(grid.grid, Cell(0, 0)) == 3
    assert grid._count_neighbours(grid.grid, Cell(1, 1)) == 4
    assert grid._count_neighbours(grid.grid, Cell(0, 1)) == 3


def test_update_full_cell():
    grid = Grid()
    grid.grid[0][0] = FULL_CELL
    grid._update_full_cell(Cell(0, 0), 4)
    assert grid.grid[0][0] == EMPTY_CELL


def test_update_empty_cell():
    grid = Grid()
    grid.grid[0][0] = EMPTY_CELL
    grid._update_empty_cell(Cell(0, 0), 3)
    assert grid.grid[0][0] == FULL_CELL


def test_update_cell():
    grid = Grid()
    temp_grid = copy.deepcopy(grid.grid)
    grid._update_cell(temp_grid, Cell(0, 0))
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

    grid.update_grid()
    assert grid.grid == expected_grid


def test_create_random_grid():
    grid = Grid(3, 3)
    assert len(grid._create_random_grid) == grid.grid_height
    assert len(grid._create_random_grid[0]) == grid.grid_width
    assert grid._create_random_grid[0][0] in [EMPTY_CELL, FULL_CELL]
    assert grid._create_random_grid[1][1] in [EMPTY_CELL, FULL_CELL]
    assert grid._create_random_grid[2][2] in [EMPTY_CELL, FULL_CELL]

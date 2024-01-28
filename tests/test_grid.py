from ..grid import Grid, Cell, EMPTY_CELL, FULL_CELL


def test_in_grid():
    grid = Grid()
    assert grid.cell_in_grid(Cell(0, 0)) == True
    assert grid.cell_in_grid(Cell(grid.grid_height, grid.grid_width)) == False


def test_create_random_grid():
    grid = Grid(3, 3)
    assert len(grid._create_random_grid) == grid.grid_height
    assert len(grid._create_random_grid[0]) == grid.grid_width
    assert grid._create_random_grid[0][0] in [EMPTY_CELL, FULL_CELL]
    assert grid._create_random_grid[1][1] in [EMPTY_CELL, FULL_CELL]
    assert grid._create_random_grid[2][2] in [EMPTY_CELL, FULL_CELL]

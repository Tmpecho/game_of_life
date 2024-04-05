import pytest

from ..grid import Grid, Cell, EMPTY_CELL, FULL_CELL, CellAnalyzer


@pytest.fixture
def grid():
    return Grid(3, 3)


def test_in_grid(grid):
    cell_analyzer = CellAnalyzer(grid)
    assert cell_analyzer._cell_in_grid(Cell(0, 0)) == True
    assert cell_analyzer._cell_in_grid(Cell(grid.grid_height, grid.grid_width)) == False


def test_create_random_grid(grid):
    assert len(grid._create_random_grid) == grid.grid_height
    assert len(grid._create_random_grid[0]) == grid.grid_width
    assert grid._create_random_grid[0][0] in [EMPTY_CELL, FULL_CELL]
    assert grid._create_random_grid[1][1] in [EMPTY_CELL, FULL_CELL]
    assert grid._create_random_grid[2][2] in [EMPTY_CELL, FULL_CELL]


def test_grid_initialization():
    grid = Grid(5, 5)
    assert len(grid.cell_matrix) == 5
    assert len(grid.cell_matrix[0]) == 5
    assert all(cell in [EMPTY_CELL, FULL_CELL] for row in grid.cell_matrix for cell in row)


def test_create_random_cell():
    cells = [Grid._create_random_cell() for _ in range(100)]
    assert all(cell in [EMPTY_CELL, FULL_CELL] for cell in cells)


def test_grid_size():
    grid = Grid(5, 5)
    assert len(grid.cell_matrix) == 5
    assert all(len(row) == 5 for row in grid.cell_matrix)


def test_cell_life_probability():
    cells = [Grid._create_random_cell() for _ in range(1000)]
    assert 100 <= cells.count(FULL_CELL) <= 200

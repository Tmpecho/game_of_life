import pytest

from ..grid import Grid, Cell, EMPTY_CELL, FULL_CELL, CellAnalyzer


@pytest.fixture
def grid():
    return Grid(3, 3)


def test_valid_neighbour(grid):
    cell_analyzer = CellAnalyzer(grid)
    grid.cell_matrix = [
        [FULL_CELL, FULL_CELL, EMPTY_CELL],
        [FULL_CELL, FULL_CELL, EMPTY_CELL],
        [FULL_CELL, EMPTY_CELL, FULL_CELL]
    ]
    assert cell_analyzer._is_valid_neighbour(grid.cell_matrix, Cell(0, 0), Cell(0, 0)) == False
    assert cell_analyzer._is_valid_neighbour(grid.cell_matrix, Cell(grid.grid_height, grid.grid_width), Cell(0, 0)) == False


def test_count_neighbours(grid):
    cell_analyzer = CellAnalyzer(grid)
    grid.cell_matrix = [
        [EMPTY_CELL, FULL_CELL, EMPTY_CELL],
        [FULL_CELL, FULL_CELL, FULL_CELL],
        [EMPTY_CELL, FULL_CELL, EMPTY_CELL]
    ]
    assert isinstance(cell_analyzer.count_neighbours(grid.cell_matrix, Cell(0, 0)), int)
    assert cell_analyzer.count_neighbours(grid.cell_matrix, Cell(0, 0)) == 3
    assert cell_analyzer.count_neighbours(grid.cell_matrix, Cell(1, 1)) == 4
    assert cell_analyzer.count_neighbours(grid.cell_matrix, Cell(0, 1)) == 3


def test_cell_in_grid(grid):
    cell_analyzer = CellAnalyzer(grid)
    assert cell_analyzer._cell_in_grid(Cell(0, 0)) == True
    assert cell_analyzer._cell_in_grid(Cell(grid.grid_height, grid.grid_width)) == False

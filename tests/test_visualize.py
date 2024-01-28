from ..grid import Grid, FULL_CELL
from ..visualize import count_all_cells, print_generation_information


def test_count_all_cells():
    grid = Grid()
    assert isinstance(count_all_cells(grid), int)
    assert count_all_cells(grid) == sum(cell == FULL_CELL for row in grid.grid for cell in row)


def test_print_generation_information(capsys):
    grid = Grid(3, 3)
    print_generation_information(grid, 0)
    captured = str(capsys.readouterr().out)
    assert "generation number: 0" in captured
    assert "population number:" in captured
    assert "--" * grid.grid_width in captured

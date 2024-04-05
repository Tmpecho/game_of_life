from grid import Grid, FULL_CELL


def count_all_cells(grid: Grid) -> int:
    return [cell == FULL_CELL for row in grid.cell_matrix for cell in row].count(True)


def print_grid_to_console(grid, generation_number: int) -> None:
    for row in grid.cell_matrix:
        print(" ".join(row))

    print_generation_information(grid, generation_number)


def print_generation_information(grid, generation_number: int) -> None:
    print("generation number:", generation_number)
    print("population number:", count_all_cells(grid))
    print("--" * grid.grid_width)

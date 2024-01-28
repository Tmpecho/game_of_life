import argparse
import os
import time

from grid import Grid, GridUpdater
from visualize import print_grid

UPDATE_SPEED_SECONDS: float = 0.1


def main(grid_height: int, grid_width: int) -> None:
    generation_number: int = 0
    grid: Grid = Grid(grid_height, grid_width)

    while True:
        print_grid(grid, generation_number)

        time.sleep(UPDATE_SPEED_SECONDS)
        os.system("clear")
        GridUpdater.update_grid(grid)

        generation_number += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Set custom grid size.')
    parser.add_argument('grid_height', type=int, nargs='?', default=40, help='Height of the grid')
    parser.add_argument('grid_width', type=int, nargs='?', default=40, help='Width of the grid')
    args = parser.parse_args()

    main(args.grid_height, args.grid_width)

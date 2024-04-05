import argparse
import os
import time

from grid import Grid, GridUpdater
from visualize import print_grid_to_console

UPDATE_SPEED_SECONDS: float = 0.1


def main(grid_height: int, grid_width: int) -> None:
    generation_number: int = 0
    grid: Grid = Grid(grid_height, grid_width)

    while True:
        print_grid_to_console(grid, generation_number)
        GridUpdater.update_grid(grid)

        time.sleep(UPDATE_SPEED_SECONDS)
        os.system("clear")

        generation_number += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Set custom grid size.')
    parser.add_argument('grid_height', type=int, nargs='?',
                        default=40, help='Height of the grid')
    parser.add_argument('grid_width', type=int, nargs='?',
                        default=40, help='Width of the grid')
    args = parser.parse_args()

    if args.grid_height <= 0 or args.grid_width <= 0:
        print("Error: Both grid height and width must be greater than 0.")
        exit(1)

    main(args.grid_height, args.grid_width)

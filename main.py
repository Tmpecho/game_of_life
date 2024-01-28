import time
import os

from grid import Grid, GridUpdater
from visualize import print_grid

UPDATE_SPEED_SECONDS: float = 0.1


def main() -> None:
    generation_number: int = 0
    grid: Grid = Grid(40, 60)

    while True:
        print_grid(grid, generation_number)

        time.sleep(UPDATE_SPEED_SECONDS)
        os.system("clear")
        GridUpdater.update_grid(grid)

        generation_number += 1


if __name__ == "__main__":
    main()

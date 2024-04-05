# Game of Life

This is an implementation of [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life), a cellular automaton where simple rules evolve complex behavior.

## Description

The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input.

This implementation of the Game of Life is written in Python. It includes classes for managing the game grid and cells, updating the grid based on the game rules, and visualizing the game state in the console.

## Installation

To install the game, clone the repository and run the `main.py` script.

```bash
git clone https://github.com/Tmpecho/game_of_life.git
cd your-repo
python main.py
```

## Usage
You can specify the grid size when running the script:
```bash
python main.py [grid_height] [grid_width]
```
If no size is specified, the default grid size is 40x40.
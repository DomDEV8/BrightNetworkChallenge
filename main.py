import numpy as np


def main():
    grid = create_grid(10)
    # Set Starting point as 8
    grid[0, 0] = 8
    phase1(grid)


def create_grid(n):
    new_grid = {}
    for i in range(n):
        for j in range(n):
            new_grid[i, j] = 0
    return new_grid


def phase1(grid):
    phase1_grid = grid
    # Put random obsticles
    phase1_grid[9, 7] = 1
    phase1_grid[8, 7] = 1
    phase1_grid[6, 7] = 1
    phase1_grid[6, 8] = 1

    # Set Delivery point as 9
    phase1_grid[9, 9] = 9
    print(phase1_grid)


if __name__ == "__main__":
    main()

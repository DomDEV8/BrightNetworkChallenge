import numpy as np


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


    def addChildren(self, value):
        self.children.append(Node(value))
        return self

    def DFS(self, grid):
        for child in self.children:
            child.DFS(grid)
        return grid

def create_grid1(n):
    new_grid = {}
    for i in range(n):
        for j in range(n):
            new_grid[i, j] = 0
    # Put random obsticles
    new_grid[9, 7] = 1
    new_grid[8, 7] = 1
    new_grid[6, 7] = 1
    new_grid[6, 8] = 1

    # Set Delivery point as 9
    new_grid[9, 9] = 9
    return new_grid


if __name__ == "__main__":
    graph = Node()
    grid = create_grid1(10)
    graph.DFS([], grid)

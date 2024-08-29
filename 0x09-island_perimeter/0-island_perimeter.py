#!/usr/bin/python3
""" compute perimeter o island represented by matrix"""


def island_perimeter(grid):
    """
        >> island_perimeter(grid)
    """

    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (grid[i][j] == 1):
                perimeter += 1
    return perimeter * 2 + 2

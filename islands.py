""" Given a grid (an MxN 2D array), count the 'islands' where an island is any
set of adjacent filled squares, where the set is surrounded on each side by an
empty square or the edge of the grid. Adjacency is defined by shared edges,
not shared corners (i.e., diagonal adjacency is excluded).

A single filled square with no adjacent filled squares is an island.
A completely filled grid contains 1 island.
A completely empty grid contains 0 islands.

>>> four_grid = [[" ", " ", " ", "x", "x", "x"],
...              ["x", " ", " ", " ", " ", " "],
...              [" ", " ", "x", "x", "x", " "],
...              ["x", "x", " ", "x", "x", " "],
...              ["x", " ", " ", "x", " ", " "]]
>>> count_islands(four_grid)
4

>>> zero_grid = [[" ", " "],
...              [" ", " "],
...              [" ", " "]]
>>> count_islands(zero_grid)
0

>>> one_grid = [["x", "x", "x"],
...             ["x", "x", "x"]]
>>> count_islands(one_grid)
1

>>> single_grid = [["x"]]
>>> count_islands(single_grid)
1

>>> just_x = [["x"],
...           ["x"],
...           ["x"],
...           ["x"]]
>>> count_islands(just_x)
1

>>> just_y = [["x", "x", "x", "x"]]
>>> count_islands(just_y)
1

>>> empty_grid = [[]]
>>> count_islands(empty_grid)
0

"""

def count_islands(grid):
    """ From input 2D array, count islands of adjacent "filled" cells
    :param grid: an M x N 2D array
    :return: integer number of islands
    """

    # store size of input 2D array
    M = len(grid)
    N = len(grid[0])
    # character used to indicate land in array
    land_indicator = 'x'

    # initialize place to store all identified land
    known_land = set()
    island_count = 0

    # iterate through whole array. for each cell with land, if not part of known
    # island, add all parts of that island to known land, and increment counter
    for i in range(M):
        for j in range(N):
            if grid[i][j] == land_indicator and (i, j) not in known_land:
                known_land.add((i, j))
                rest = find_rest_of_island(i, j, grid)
                known_land.update(rest)
                island_count += 1

    return island_count


def find_rest_of_island(x, y, grid, land=None):
    """ starting from a cell, add all adjacent land cells to land
    :param x: x-coordinate of starting cell
    :param y: y-coordinate of starting cell
    :param grid: 2D array
    :param land: set of all known land cells
    :return: land

    Excepting edge cells, check all adjacent cells for new land.
    If land found, recurse to find remaining land.
    """

    max_x = len(grid) - 1
    max_y = len(grid[0]) - 1
    seen = land or set()

    # character used to indicate land in array
    land_indicator = 'x'

    # check cell above when not at top
    if x > 0:
        if grid[x-1][y] == land_indicator and (x-1, y) not in seen:
            seen.add((x-1, y))
            find_rest_of_island(x-1, y, grid, seen)
    # check cell below when not at bottom
    if x < max_x:
        if grid[x+1][y] == land_indicator and (x+1, y) not in seen:
            seen.add((x+1, y))
            find_rest_of_island(x+1, y, grid, seen)
    # check cell at left when not at left edge
    if y > 0:
        if grid[x][y-1] == land_indicator and (x, y-1) not in seen:
            seen.add((x, y-1))
            find_rest_of_island(x, y-1, grid, seen)
    # check cell at right when not at right edge
    if y < max_y:
        if grid[x][y+1] == land_indicator and (x, y+1) not in seen:
            seen.add((x, y+1))
            find_rest_of_island(x, y+1, grid, seen)

    return seen


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n All tests passed.\n"
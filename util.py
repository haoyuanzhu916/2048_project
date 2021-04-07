from typing import List

from Grid import Grid
from random import randint, choices
from math import sqrt,log2

directionVectors = (UP_VEC, DOWN_VEC, LEFT_VEC, RIGHT_VEC) = ((-1, 0), (1, 0), (0, -1), (0, 1))


def getANewGrid(grid: Grid, dir) -> Grid:
    '''
    :param grid: A grid
    :param dir: A move
    :return: a random result of move
    '''
    if grid.isTerminal():
        # return the original grid if the game is terminal
        return grid.clone()
    ret = grid.clone()
    ret.move(dir)
    cells = ret.getAvailableCells()
    cell = cells[randint(0, len(cells) - 1)]
    ret.setCellValue(cell, 2)
    return ret


def getAllPossibleGrid(grid: Grid, dir) -> List[Grid]:
    '''
    :param grid: A grid
    :param dir: A move
    :return: a list of all possible result of move
    '''
    if grid.isTerminal():
        # return the original grid if the game is terminal
        return [grid.clone()]
    ret = grid.clone()
    ret.move(dir)
    if not grid.canMove([dir]):
        raise ValueError('Invalid Move')
    cells = ret.getAvailableCells()
    grids = []
    for cell in cells:
        ret2 = ret.clone()
        ret2.setCellValue(cell, 2)
        grids.append(ret2)
    return grids


def getKNewGrid(grid: Grid, dir, k=4):
    '''
    random sample k resulting grids with replacement
    '''
    grids = getAllPossibleGrid(grid, dir)
    return choices(grids, k=k)

def estimate(grid: Grid):
    '''
    :param grid:
    :type grid:
    :return:
    :rtype:
    '''
    #return freeCellsHeuristic(grid)
    return edgeHeuristic(grid) + freeCellsHeuristic(grid) + smoothnessHeuristic(grid)

def freeCellsHeuristic(grid : Grid):
    '''
    :param grid: estimated Grid
    :return: free cells(empty cell) Count
    :rtype: int
    '''
    return len(grid.getAvailableCells())

def smoothnessHeuristic(grid:Grid):
    size = grid.size
    value = 0
    for i in range(size):
        for j in range(size):
            cellValue = float('inf')
            if i > 0: cellValue = min(cellValue, abs(grid.mat[i][j] - grid.mat[i - 1][j]))
            if i < size - 1: cellValue = min(cellValue, abs(grid.mat[i][j] - grid.mat[i + 1][j]))
            if j > 0: cellValue = min(cellValue, abs(grid.mat[i][j] - grid.mat[i][j -1]))
            if j < size - 1: cellValue = min(cellValue, abs(grid.mat[i][j] - grid.mat[i][j+1]))
            if 4096 > cellValue > 0:
                value += log2(cellValue)
    return -(value)

def edgeHeuristic(grid:Grid):
    '''
    We like big tiles on the edge
    '''
    size = grid.size
    value = 0
    for i in range(size):
        for j in range(size):
            if (i == 0 or i == size) and (j == 0 or j == size-1):
                cellValue = 2 * log2(max(1, grid.mat[i][j]))
            elif i == 0 or i == size-1 or j == 0 or j == size-1:
                cellValue = log2(max(1,grid.mat[i][j]))
            else:
                cellValue = -log2(max(1, grid.mat[i][j]))
            value += cellValue
    return value

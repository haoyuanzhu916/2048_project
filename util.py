from typing import List

from Grid import Grid
from random import randint, choices


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
    return freeCellsHeuristic(grid)

def freeCellsHeuristic(grid : Grid):
    '''
    :param grid: estimated Grid
    :return: free cells(empty cell) Count
    :rtype: int
    '''
    return len(grid.getAvailableCells())
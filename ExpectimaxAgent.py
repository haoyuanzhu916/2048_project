from Agent import Agent
from Grid import Grid
from util import *
from random import choice,shuffle
from math import sqrt, log
from Display import *

class expectimaxAgent(Agent):
    def __init__(self, depth=3):
        self.depth = depth

    def getMove(self, grid: Grid):
        if grid.isWin() or grid.isLose():
            _ = input()
        currentMax = float("-inf")
        currentMove = None
        for m in grid.getAvailableMoves():
            if self.maximizer(0, grid, m)[0] > currentMax:
                currentMax = self.maximizer(0, grid, m)[0]
                currentMove = self.maximizer(0, grid, m)[1]
        return currentMove


    def maximizer(self, d, grid, dir):
        if grid.isLose() or grid.isWin() or d == self.depth:
            return [estimate(grid), dir]
        else:
            moves = grid.getAvailableMoves()
            if not moves:
                return [estimate(grid), dir]
            else:
                values = []
                for m in moves:
                    newGrids = getAllPossibleGrid(grid, m)
                    numGirds = len(newGrids)
                    v = 0
                    for newgrid in newGrids:
                        v += self.maximizer(d + 1, newgrid, m)[0] / numGirds
                    values.append([m, v])
                curMax = float("-inf")
                curMove = None
                for i in range(len(values)):
                    if values[i][1] > curMax:
                        curMove = values[i][0]
                        curMax = values[i][1]
                if curMove is None:
                    print("no move")
                return [curMax, curMove]


def estimate(grid: Grid):
    '''
    :param grid:
    :type grid:
    :return:
    :rtype:
    '''
    # return freeCellsHeuristic(grid)
    if grid.isWin():
        return 1000
    if grid.isLose():
        return -1000
    return (maxValueHeuristic(grid) + freeCellsHeuristic(grid) + monotonicityHeuristic(grid) // 2)




if __name__ == '__main__':
    g = Grid()
    g.mat[0][0] = 2
    g.mat[1][0] = 2
    g.mat[3][0] = 4
    dis = BeatifulDisplay()
    dis.display(g)

    agent = expectimaxAgent()
    move = agent.getMove(g)
    print(move)
    _ = input()


from Grid import Grid
from util import *
from random import randint, shuffle
import time

class Agent:
    def getMove(self, grid: Grid):
        pass

class randomAgent(Agent):
    def getMove(self, grid: Grid):
        #time.sleep(0.1)
        moves = grid.getAvailableMoves()
        return moves[randint(0,len(moves)-1)]


class greedyAgent(Agent):
    def getScore(self, grid, move):

        score = 0
        rets = getAllPossibleGrid(grid, move)
        for ret in rets:
            if ret.isLose():
                score -= 100
                continue
            if ret.isWin():
                score += 1000
                continue
            score += len(ret.getAvailableCells())
        return score / len(rets)

    def getMove(self, grid: Grid):
        #time.sleep(0.1)
        moves = grid.getAvailableMoves()
        shuffle(moves)
        maxScore = float('-inf')
        maxMove = None
        for move in moves:
            gridCopy = grid.clone()
            score = self.getScore(gridCopy, move)
            if score > maxScore:
                maxScore, maxMove = score, move
        return maxMove
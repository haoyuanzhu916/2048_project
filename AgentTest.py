from Agent import *
from Game import Game
from Display import BeatifulDisplay


class AgentTest:
    def __init__(self, testAgent=greedyAgent(), testTurns=100, verbose=0):
        self.testAgent = testAgent
        self.testTurns = testTurns
        self.verbose = verbose

        self.scores = []
        self.winCount = 0

    def printStat(self):
        print('max score = {:.0f}, min score = {:.0f}, avg score = {:.0f}, winning rate = {:.2%}'.format(
            max(self.scores), min(self.scores), sum(self.scores) / self.testTurns, self.winCount / self.testTurns))


    def main(self):
        for i in range(self.testTurns):
            game = Game()
            game.setAgent(self.testAgent)
            if self.verbose == 0:
                game.setDisplay(BeatifulDisplay(), -1)
            else:
                game.setDisplay(BeatifulDisplay(), 50)
            isWin, score = game.main()
            self.scores.append(score)
            if isWin:
                self.winCount += 1

            if i > 0 and (i + 1) % 10 == 0:
                print('{}/{} tests done'.format((i + 1), self.testTurns))
        self.printStat()


if __name__ == '__main__':
    test = AgentTest()
    test.main()

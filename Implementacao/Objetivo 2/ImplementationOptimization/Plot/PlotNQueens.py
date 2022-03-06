import matplotlib.pyplot as plt
from lib.OptimizationLibrary.Plot.Plot import Plot


class PlotNQueens(Plot):

    def __init__(self, state, board):
        self.__state = state
        self.__board = board

    def plot_state(self):
        for i in range(len(self.__board)):
            self.__board[i][self.__state[i]] = 1

        plt.matshow(self.__board)
        plt.show()

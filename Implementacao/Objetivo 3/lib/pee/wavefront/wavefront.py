import math
import sys
import pandas
import numpy as np
import matplotlib.pyplot as plt
from lib.utils.plot_table import plot_table


class WaveFront:

    def __init__(self, operators):
        self.__values = []
        self.__operators = operators

    def __get_adjacents(self, state):
        states = []
        for operator in self.__operators:
            s = operator.apply(state)
            if s != None:
                states.append(s)
        print("adjacentes",state,states)
        return states

    def __distance(self, state, suc_state):
        x = math.pow(state.get_x() - suc_state.get_x(), 2)
        y = math.pow(state.get_y() - suc_state.get_y(), 2)
        val = math.sqrt(x + y)
        return val

    def run_algoritm(self, goal, max_value=100, gama=.7):

        values = {}
        fringe = []

        values[goal] = max_value
        fringe.append(goal)

        while fringe:
            s = fringe.pop(0)
            for new_s in self.__get_adjacents(s):
                v = values[s] * math.pow(gama, self.__distance(s, new_s))
                if new_s in values:
                    if v > values[new_s]:
                        values[new_s] = v
                        fringe.append(new_s)
                elif v > sys.float_info.min:
                    values[new_s] = v
                    fringe.append(new_s)
        self.__values = values
        return self.__values

    def plot(self):
        board = np.zeros(10 * 10).reshape(10, 10)
        for a, b in self.__values.items():
            board[a.get_x(), a.get_y()] = b

        data = pandas.DataFrame(board)
        plot_table(data)
        plt.show()

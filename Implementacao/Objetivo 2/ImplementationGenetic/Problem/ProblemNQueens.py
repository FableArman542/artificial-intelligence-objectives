import numpy as np
from lib.GeneticLibrary.Problem import Problem


class ProblemNQueens(Problem.Problem):

    def __init__(self, board):
        self.__board = board

    def fitness_function(self, state):
        return 1/(self.__get_cost_of_state(state)+1)

    def __get_cost_of_state(self, state):
        perpendicular = self.__check_perpendicular(state)
        diagonal = self.__check_diagonal(state)
        return perpendicular + diagonal

    def get_random_state(self, state):
        new_state = state.copy()

        for i in range(len(new_state)):
            new_state[i] = np.random.randint(0, len(self.__board))

        return new_state

    def __check_perpendicular(self, state):
        already_counted = []
        cost = 0
        for i in range(len(state)):
            if i < len(state) - 1:
                if state[i] not in already_counted:
                    for j in range(i + 1, len(state)):
                        if state[i] == state[j]:
                            cost += 1
                    already_counted.append(state[i])
        return cost

    def __check_diagonal(self, state):
        return self.__check_diagonal_positive(state) + self.__check_diagonal_negative(state)

    def __check_diagonal_negative(self, state):
        cost = 0
        dont_cares = []
        for i in range(len(state)):
            if i < len(state) - 1:
                value = state[i] - 1
                if i not in dont_cares:
                    for j in range(i + 1, len(state)):
                        if state[j] == value:
                            cost += 1
                            dont_cares.append(j)
                        value -= 1
        return cost

    def __check_diagonal_positive(self, state):
        cost = 0
        dont_cares = []
        for i in range(len(state)):
            if i < len(state) - 1:
                value = state[i] + 1
                if i not in dont_cares:
                    for j in range(i + 1, len(state)):
                        if state[j] == value:
                            cost += 1
                            dont_cares.append(j)
                        value += 1
        return cost
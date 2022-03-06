import numpy as np
from lib.OptimizationLibrary.Operator.operator import Operator


class OperatorMoveQueen(Operator):
    def apply_operator(self, state):
        digits = np.arange(len(state)).tolist()
        neighbours = []
        for i in range(len(state)):
            possible_numbers = digits.copy()
            possible_numbers.remove(state[i])
            for j in range(len(possible_numbers)):
                new_state = state.copy()
                new_state[i] = possible_numbers[j]
                neighbours.append(new_state)

        return neighbours


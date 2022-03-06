from lib.OptimizationLibrary.Operator.operator import Operator


class OperatorSwitchAdjacent(Operator):
    def apply_operator(self, state):
        neighbours = []
        counter = 0
        _state = state.copy()
        _state.pop()

        for first, second in zip(_state, _state[1::]):
            new_state = _state.copy()
            new_state[counter] = second
            new_state[counter + 1] = first
            neighbours.append(new_state)
            counter += 1

        return neighbours
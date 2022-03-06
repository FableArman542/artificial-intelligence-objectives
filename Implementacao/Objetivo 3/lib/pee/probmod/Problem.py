

class Problem:

    def __init__(self, initial_state, operators):
        self.__initial_state = initial_state
        self.__operators = operators

    def get_initial_state(self):
        return self.__initial_state

    def get_operators(self):
        return self.__operators

    def is_objective(self, state):
        raise NotImplementedError("Abstract")

    def heuristic(self, state):
        raise NotImplementedError("Abstract")

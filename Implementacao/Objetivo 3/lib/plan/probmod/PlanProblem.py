import math
from lib.pee.probmod.Problem import Problem


class PlanProblem(Problem):

    def __init__(self, initial_state, last_state, operators):
        super().__init__(initial_state, operators)
        self.__last_state = last_state

    def is_objective(self, state):
        return state == self.__last_state

    def heuristic(self, state):
        result = math.sqrt(((self.__last_state.get_x()-state.get_x())**2)+((self.__last_state.get_y()-state.get_y())**2))
        return result

    def get_last_state(self):
        return self.__last_state

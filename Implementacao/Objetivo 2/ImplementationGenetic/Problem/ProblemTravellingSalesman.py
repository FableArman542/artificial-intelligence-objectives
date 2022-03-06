import numpy as np
from lib.GeneticLibrary.Problem import Problem


class ProblemTravellingSalesman(Problem.Problem):

    def __init__(self, costs_table, cities):
        self.__costs_table = costs_table
        self.__cities = cities
    
    def fitness_function(self, state):
        return 1/self.__get_cost_of_state(state)

    def __get_cost_of_state(self, state):
        cost = 0
        first_iteration = True
        for first, second in zip(state, state[1:]):
            cost += self.__costs_table[first][self.__cities[second]]
            if first_iteration:
                cost += self.__costs_table[first][self.__cities[second]]
                first_iteration = False

        return cost

    def get_random_state(self, state):
        returns_to_start = False
        new_state = state.copy()
        solution = []

        for i in range(len(state)):
            random_location = new_state[np.random.randint(0, len(new_state))]
            solution.append(random_location)
            new_state.remove(random_location)

        if returns_to_start == True: solution.append(solution[0])
        return solution
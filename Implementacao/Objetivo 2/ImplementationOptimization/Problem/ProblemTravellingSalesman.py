import numpy as np
from lib.OptimizationLibrary.Problem import Problem


class ProblemTravellingSalesman(Problem.Problem):

    def __init__(self, operator, costs_table, cities):
        self.__costs_table = costs_table
        self.__cities = cities
        self.__operator = operator
    
    def get_cost_of_state(self, state):
        cost = 0
        for first, second in zip(state, state[1:]):
            cost += self.__costs_table[first][self.__cities[second]]
        return cost
    
    def get_random_state(self, state):
        returns_to_start=True
        new_state = state.copy()
        solution = []

        for i in range(len(state)):
            random_location = new_state[np.random.randint(0, len(new_state))]
            solution.append(random_location)
            new_state.remove(random_location)
        
        if returns_to_start == True: solution.append(solution[0])
        return solution
    
    def get_all_neighbours(self, state):
        return self.__operator.apply_operator(state)

    def get_random_neighbour(self, neighbours):
        state = super().get_random_neighbour(neighbours)
        state.append(state[0])

        return state

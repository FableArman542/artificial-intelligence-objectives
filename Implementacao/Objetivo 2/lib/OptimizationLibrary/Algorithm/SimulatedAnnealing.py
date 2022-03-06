import numpy as np

from lib.OptimizationLibrary.Algorithm.Algorithm import Algorithm
from lib.OptimizationLibrary.Algorithm.Result import Result


class SimulatedAnnealing(Algorithm):
    def __init__(self, state, problem, initial_temperature):
        self.__current_state = state
        self.__problem = problem
        self.__initial_temperature = initial_temperature
        self.__current_cost = self.__problem.get_cost_of_state(self.__current_state)
    
    def run_algorithm(self, max_iter):
        self.__current_state = self.__problem.get_random_state(self.__current_state)
        self.__current_cost = self.__problem.get_cost_of_state(self.__current_state)

        T = self.__initial_temperature
        factor = .99

        for i in range(max_iter):
            T = T*factor

            neighbours = self.__problem.get_all_neighbours(self.__current_state)
            new_state = self.__problem.get_random_neighbour(neighbours)

            cost = self.__problem.get_cost_of_state(new_state)

            last_iteration = i
            if cost <= self.__current_cost:
                self.__current_cost = cost
                self.__current_state = new_state
            else:
                r = np.random.uniform()
                probability = np.exp((self.__current_cost - cost) / T)
                if r < probability:
                    self.__current_cost = cost
                    self.__current_state = new_state

        result = Result(self.__current_state, self.__current_cost, last_iteration)

        return result

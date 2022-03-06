from lib.OptimizationLibrary.Algorithm.Algorithm import Algorithm
from lib.OptimizationLibrary.Algorithm.Result import Result


class HillClimbing(Algorithm):
    def __init__(self, state, problem, method='normal'):
        self.__current_state = state
        self.__problem = problem
        self.__current_cost = self.__problem.get_cost_of_state(self.__current_state)
        self.__method = method

    def __get_better_random_state(self, neighbours, max_iter=1000):
        i = 0
        while i < max_iter:
            best_state = self.__problem.get_random_neighbour(neighbours)

            best_cost = self.__problem.get_cost_of_state(best_state)
            if best_cost < self.__current_cost:
                return best_state, best_cost
            i += 1

        print("--- Best random state not found. Returning the current state.")
        return self.__current_state, self.__current_cost

    def run_algorithm(self, max_iter):
        # print("- Salesman Configuration \n", state)
        self.__current_state = self.__problem.get_random_state(self.__current_state)
        self.__current_cost = self.__problem.get_cost_of_state(self.__current_state)

        neighbours = self.__problem.get_all_neighbours(self.__current_state)
        if self.__method == 'normal':
            best_state, best_cost = self.__problem.choose_best_state(neighbours)
        elif self.__method == 'stochastic':
            best_state, best_cost = self.__get_better_random_state(neighbours)

        # print("--- Initial Cost:", self.__current_cost)
        # print("--- Initial Solution:", self.__current_state)
        # print("--- Initial BestCostFound:", best_cost)
        # print("--- Initial BestSolutionFound:", best_state)

        iteration = 0
        while best_cost < self.__current_cost:
            if iteration > max_iter:
                break

            self.__current_state = best_state
            self.__current_cost = best_cost

            neighbours = self.__problem.get_all_neighbours(self.__current_state)

            if self.__method == 'normal':
                best_state, best_cost = self.__problem.choose_best_state(neighbours)
            elif self.__method == 'stochastic':
                best_state, best_cost = self.__get_better_random_state(neighbours)

            # print("Iteration: " + str(iteration) + " | Cost = " + str(best_cost))# + " | State = " + str(self.__current_state))
            iteration += 1

        result = Result(self.__current_state, self.__current_cost, iteration)

        return result

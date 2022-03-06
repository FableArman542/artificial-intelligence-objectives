

class Result:
    def __init__(self, state, cost, iterations):
        self.__state = state
        self.__cost = cost
        self.__iterations = iterations

    def get_iterations(self):
        return self.__iterations

    def get_state(self):
        return self.__state

    def get_cost(self):
        return self.__cost

    def __str__(self):
        return "\n-> Result\nState = " + str(self.__state) + "\nCost = " + str(self.__cost) + "\nIterations = " + str(self.__iterations)

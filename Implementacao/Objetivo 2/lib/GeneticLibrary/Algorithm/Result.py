

class Result:
    def __init__(self, state, fitness, iterations):
        self.__state = state
        self.__fitness = fitness
        self.__iterations = iterations

    def get_state(self):
        return self.__state

    def set_state(self, state):
        self.__state = state

    def get_fitness(self):
        return self.__fitness

    def __str__(self):
        return "\n-> Result\nState = " + str(self.__state) + "\nFitness = " + str(self.__fitness) + "\nIterations = " + str(self.__iterations)

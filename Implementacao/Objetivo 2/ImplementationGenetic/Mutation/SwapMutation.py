import numpy as np
from lib.GeneticLibrary.Mutation.Mutation import Mutation


class SwapMutation(Mutation):
    def apply(self, chromosome):
        index1 = np.random.randint(len(chromosome))
        index2 = None
        while True:
            index2 = np.random.randint(len(chromosome))
            if index2 != index1: break

        temp = chromosome[index1]
        chromosome[index1] = chromosome[index2]
        chromosome[index2] = temp

        return chromosome
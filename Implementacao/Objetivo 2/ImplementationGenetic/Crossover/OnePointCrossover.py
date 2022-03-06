import numpy as np
from lib.GeneticLibrary.Crossover.Crossover import Crossover


class OnePointCrossover(Crossover):
    def apply(self, chromosome_1, chromosome_2):

        cut_point = -1
        while True:
            cut_point = np.random.randint(1, len(chromosome_1))
            if cut_point < len(chromosome_1) - 1: break

        chromosome_1_first = chromosome_1[:cut_point]
        chromosome_1_second = chromosome_1[cut_point:]

        chromosome_2_first = chromosome_2[:cut_point]
        chromosome_2_second = chromosome_2[cut_point:]
        # print("1",chromosome_1_first, chromosome_1_second)
        # print("2",chromosome_2_first, chromosome_2_second)

        chromosome_1d = np.hstack((chromosome_1_first, chromosome_2_second))
        chromosome_2d = np.hstack((chromosome_2_first, chromosome_1_second))

        return chromosome_1d, chromosome_2d


initial_state = [0, 2, 2, 2, 4, 5, 6, 7]
initial_state1 = [0, 5, 2, 2, 2, 5, 6, 1]
ajuda = OnePointCrossover()
ajuda.apply(initial_state, initial_state1)

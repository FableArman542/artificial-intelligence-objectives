import numpy as np
from lib.GeneticLibrary.Selection.Selection import Selection


class RouletteSelection(Selection):
    def apply(self, chromosomes, fitness_values, number_of_selection=2):
        sum_of_fitness = np.sum(fitness_values)
        probabilities = [f / sum_of_fitness for f in fitness_values]

        chromosomes = [chromosomes[np.random.choice(len(chromosomes), p=probabilities)] for i in range(number_of_selection)]

        return chromosomes


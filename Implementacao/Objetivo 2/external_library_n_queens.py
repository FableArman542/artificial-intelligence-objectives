import random
import numpy as np
from pyeasyga import pyeasyga
from ImplementationGenetic.Problem.ProblemNQueens import ProblemNQueens
from Data.TravellingSalesmanTables import costs_table, cities, geo_coordinates



# setup seed data
seed_data = [0, 1, 2, 3, 4, 5, 6, 7, 8]
n = len(seed_data)
# initialise the GA
ga = pyeasyga.GeneticAlgorithm(seed_data,
                               population_size=10,
                               generations=100,
                               crossover_probability=1,
                               mutation_probability=0.05,
                               elitism=True,
                               maximise_fitness=True)


# define and set function to create a candidate solution representation
def create_individual(data):
    individual = data[:]
    random.shuffle(individual)
    return individual


ga.create_individual = create_individual


# define and set the GA's crossover operation
def crossover(parent_1, parent_2):
    crossover_index = random.randrange(1, len(parent_1))
    child_1a = parent_1[:crossover_index]
    child_1b = [i for i in parent_2 if i not in child_1a]
    child_1 = child_1a + child_1b

    child_2a = parent_2[crossover_index:]
    child_2b = [i for i in parent_1 if i not in child_2a]
    child_2 = child_2a + child_2b

    return child_1, child_2


ga.crossover_function = crossover


# define and set the GA's mutation operation
def mutate(individual):
    index1 = np.random.randint(len(individual))
    index2 = None
    while True:
        index2 = np.random.randint(len(individual))
        if index2 != index1: break

    temp = individual[index1]
    individual[index1] = individual[index2]
    individual[index2] = temp


ga.mutate_function = mutate

board = np.zeros(n * n).reshape(n, n)
problem = ProblemNQueens(board)


# define and set the GA's selection operation
def selection(population):
    # print("data", population)
    fitness_values = []
    for individual in population:
        sol = individual.genes
        fitness_values.append(problem.fitness_function(sol))

    sum_of_fitness = np.sum(fitness_values)
    probabilities = [f / sum_of_fitness for f in fitness_values]

    return population[np.random.choice(len(population), p=probabilities)]


ga.selection_function = selection


# define a fitness function
def fitness(individual, data):
    return problem.fitness_function(individual)


ga.fitness_function = fitness
ga.run()

# print the GA's best solution; a solution is valid only if there are no collisions
print(ga.best_individual())

from ImplementationGenetic.Plot.PlotNQueens import PlotNQueens

plot = PlotNQueens(ga.best_individual()[1], board)
plot.plot_state()

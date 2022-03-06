import random
import numpy as np
from pyeasyga import pyeasyga

from ImplementationGenetic.Plot.PlotTravellingSalesman import PlotTravellingSalesman
from ImplementationGenetic.Problem.ProblemTravellingSalesman import ProblemTravellingSalesman
from Data.TravellingSalesmanTables import costs_table, cities, geo_coordinates

# setup seed data
seed_data = [0, 1, 2, 6, 7, 3, 4, 5, 8, 9, 10, 12, 11]

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
    percurso1 = parent_1
    percurso2 = parent_2

    cut_point1 = -1
    while True:
        cut_point1 = np.random.randint(1, len(percurso1))
        if cut_point1 < len(percurso1) - 1: break

    cut_point2 = np.random.randint(cut_point1 + 1, len(percurso1))

    percurso1 = np.asarray(percurso1)
    percurso2 = np.asarray(percurso2)

    cut_percurso1 = percurso1[cut_point1:cut_point2 + 1]
    cut_percurso2 = percurso2[cut_point1:cut_point2 + 1]

    next_percurso1 = percurso1[cut_point2 + 1::]
    next_percurso2 = percurso2[cut_point2 + 1::]

    before_percurso1 = percurso1[:cut_point1]
    before_percurso2 = percurso2[:cut_point1]

    p1 = np.hstack((next_percurso1, before_percurso1, cut_percurso1))

    p2 = np.hstack((next_percurso2, before_percurso2, cut_percurso2))

    p1 = p1.tolist()
    for a in cut_percurso2:
        if a in p1: p1.remove(a)

    p2 = p2.tolist()

    for a in cut_percurso1:
        if a in p2: p2.remove(a)
    p1 = np.asarray(p1)
    p2 = np.asarray(p2)

    percurso1_start = []
    deleted = "error"
    for i in range(len(next_percurso1)):
        percurso1_start.append(p1[i])
        deleted = i

    if deleted != "error":
        percurso1_end = p1[deleted + 1:]
    else:
        percurso1_end = p1

    percurso2_start = []
    deleted = "error"
    for i in range(len(next_percurso2)):
        percurso2_start.append(p2[i])
        deleted = i

    if deleted != "error":
        percurso2_end = p2[deleted + 1:]
    else:
        percurso2_end = p2

    percurso1d = np.hstack((percurso1_end, cut_percurso2, percurso1_start))
    percurso2d = np.hstack((percurso2_end, cut_percurso1, percurso2_start))

    return percurso1d, percurso2d


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

problem = ProblemTravellingSalesman(costs_table, cities)


# define and set the GA's selection operation
def selection(population):
    # print("data", population)
    fitness_values = []
    for individual in population:
        sol = individual.genes
        sol1 = convert_solution(sol)
        fitness_values.append(problem.fitness_function(sol1))

    sum_of_fitness = np.sum(fitness_values)
    probabilities = [f / sum_of_fitness for f in fitness_values]

    return population[np.random.choice(len(population), p=probabilities)]


ga.selection_function = selection


# define a fitness function
def fitness(individual, data):
    sol = convert_solution(individual)
    return problem.fitness_function(sol)


def convert_solution(solution):
    lista = []
    for gene in solution:
        lista.append(list(cities)[int(gene)])
    lista.append(lista[0])
    return lista


ga.fitness_function = fitness
ga.run()

# print the GA's best solution; a solution is valid only if there are no collisions
print(ga.best_individual())
print(convert_solution(ga.best_individual()[1]))

plot = PlotTravellingSalesman(convert_solution(ga.best_individual()[1]), geo_coordinates)
plot.plot_state()

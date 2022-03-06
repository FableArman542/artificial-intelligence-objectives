import numpy as np
from ImplementationGenetic.Problem.ProblemTravellingSalesman import ProblemTravellingSalesman
from ImplementationGenetic.Problem.ProblemNQueens import ProblemNQueens
from lib.GeneticLibrary.Algorithm.GeneticAlgorithm import GeneticAlgorithm
from ImplementationGenetic.Selection.RouletteSelection import RouletteSelection
from ImplementationGenetic.Crossover.MultiPointCrossover import MultiPointCrossover
from ImplementationGenetic.Crossover.OnePointCrossover import OnePointCrossover
from ImplementationGenetic.Mutation.SwapMutation import SwapMutation
from ImplementationGenetic.Plot.PlotTravellingSalesman import PlotTravellingSalesman
from ImplementationGenetic.Plot.PlotNQueens import PlotNQueens

from Data.TravellingSalesmanTables import costs_table, cities, geo_coordinates


def travelling_salesman_genetic():
    initial_state = [
        "New York",
        "Los Angeles",
        "Chicago",
        "Seattle",
        "Boston",
        "Minneapolis",
        "Denver",
        "Dallas",
        "San Francisco",
        "St. Louis",
        "Houston",
        "Salt Lake City",
        "Phoenix"
    ]

    problem = ProblemTravellingSalesman(costs_table, cities)

    selection = RouletteSelection()
    crossover = MultiPointCrossover()
    mutation = SwapMutation()

    genetic = GeneticAlgorithm(state=initial_state, problem=problem, selection=selection, crossover=crossover, mutation=mutation, k_chromosomes=200.)

    result = genetic.run_algorithm(max_number_of_generations=100, probability_of_mutation=0.4)
    result_state = result.get_state()
    result_state.append(result.get_state()[0])
    result.set_state(result_state)
    print(result)

    plot = PlotTravellingSalesman(result.get_state(), geo_coordinates)
    plot.plot_state()


def n_queens():
    initial_state = [0, 2, 2, 2, 4, 5, 6, 7]
    n = len(initial_state)
    board = np.zeros(n * n).reshape(n, n)

    problem = ProblemNQueens(board)

    selection = RouletteSelection()
    crossover = OnePointCrossover()
    mutation = SwapMutation()

    genetic = GeneticAlgorithm(state=initial_state, problem=problem, selection=selection, crossover=crossover, mutation=mutation, k_chromosomes=200.,stop_criteria="reach_1")

    result = genetic.run_algorithm(max_number_of_generations=1000, probability_of_mutation=0.4)

    print(result)

    plot = PlotNQueens(result.get_state(), board)
    plot.plot_state()


travelling_salesman_genetic()
n_queens()

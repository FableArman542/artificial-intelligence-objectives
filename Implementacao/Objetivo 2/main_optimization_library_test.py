import numpy as np

from lib.OptimizationLibrary.Algorithm.HillClimbing import HillClimbing
from ImplementationOptimization.Problem.ProblemTravellingSalesman import ProblemTravellingSalesman
from ImplementationOptimization.Problem.ProblemNQueens import ProblemNQueens

from ImplementationOptimization.Operator.OperatorSwitchAdjacent import OperatorSwitchAdjacent
from ImplementationOptimization.Operator.OperatorMoveQueen import OperatorMoveQueen

from ImplementationOptimization.Plot.PlotNQueens import PlotNQueens
from ImplementationOptimization.Plot.PlotTravellingSalesman import PlotTravellingSalesman

from Data.TravellingSalesmanTables import costs_table, cities, geo_coordinates
from lib.OptimizationLibrary.Algorithm.SimulatedAnnealing import SimulatedAnnealing


def travelling_salesman(method="hill_climbing"):
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
    adjacent_operator = OperatorSwitchAdjacent()
    problem = ProblemTravellingSalesman(adjacent_operator, costs_table, cities)

    result = None

    if method == "hill_climbing":
        hill_climbing = HillClimbing(initial_state, problem, method="stochastic")
        result = hill_climbing.run_algorithm(1000)
    else:
        simulated_annealing = SimulatedAnnealing(initial_state, problem, initial_temperature=30)
        result = simulated_annealing.run_algorithm(1000)

    print(result)

    plotting = PlotTravellingSalesman(result.get_state(), geo_coordinates)
    plotting.plot_state()


def n_queens(method="hill_climbing"):
    initial_state = [0, 2, 2, 2, 4, 5, 6, 7]
    n = len(initial_state)
    board = np.zeros(n*n).reshape(n, n)

    move_queen_operator = OperatorMoveQueen()
    problem = ProblemNQueens(move_queen_operator, board)

    result = None

    if method == "hill_climbing":
        hill_climbing = HillClimbing(initial_state, problem, method="stochastic")
        result = hill_climbing.run_algorithm(1000)
    else:
        simulated_annealing = SimulatedAnnealing(initial_state, problem, initial_temperature=30)
        result = simulated_annealing.run_algorithm(1000)

    print(result)

    plotting = PlotNQueens(result.get_state(), board)
    plotting.plot_state()


n_queens(method="hill_climbing")
travelling_salesman(method="hill_climbing")

n_queens(method="simulated_annealing")
travelling_salesman(method="simulated_annealing")

import numpy as np
import sys
import copy
import matplotlib.pyplot as plt
from lib.plan.Planner import Planner
from lib.pee.bestfirst.RTAASearch import RTAASearch
from lib.plan.probmod.PlanProblem import PlanProblem
from lib.pee.searchengine.Node import Node
from lib.pee.probmod.Solution import Solution
from matplotlib.table import Table
from lib.utils.plot_table import plot_table
import pandas


class PlanRTAA(Planner):

    def __init__(self, lookahead):
        self.__search_engine = RTAASearch()
        self.__plan = None
        self.__lookahead = lookahead

    def plan(self, world_model, initial_state, objective):
        solutions = []

        operators = world_model.get_operators()
        current_state = copy.deepcopy(initial_state)
        final_nodes = []
        policy = {}
        values = []
        while current_state != objective:

            # A star Search
            print("-> Start:", current_state, "Goal:", objective, end=" ")
            problem = PlanProblem(current_state, objective, operators)
            solution = self.__search_engine.solve(problem=problem, max_depth=self.__lookahead)
            closed = solution.get_closed_nodes()
            new_state = solution.get_final_node().get_state()
            print("| Intermediate point=", new_state)

            # If failure return
            if not solution:
                return None

            # Go through closed nodes and update heuristic for each one
            for v, d in closed.items():
                self.__search_engine.h[v] = self.__search_engine.f(solution.get_final_node()) - d.get_cost()
                # print(v, self.__search_engine.h[v])

            # self.plot([], heuristics, None, world_model)

            # Navigate in the grid following minimum f-value
            current_state = self.__search_engine.navigate(movements=15, current_state=current_state, new_state=new_state, operators=operators, policy=policy)

            final_nodes.append(current_state)
            values.append(self.__search_engine.h)

        plan = self.__create_plan(initial_state, objective, policy)

        final_solution = Solution()
        final_solution.set_path([plan])

        final_solution.set_final_node(final_nodes)
        final_solution.set_closed_nodes(values)

        self.__plan = final_solution

        return solutions

    def __create_plan(self, initial_state, goal, policy):
        s = initial_state
        plano = []
        while s != goal and s in policy:
            plano.append(Node(s, policy[s]))
            s = policy[s].apply(s)
        return plano

    def finish_plan(self):
        self.__plan = None

    def get_operator(self):
        if self.__plan is None or len(self.__plan.get_path()) == 0:
            return None

        if self.__plan.get_path()[0] is not None and len(self.__plan.get_path()[0]) > 0:
            node = self.__plan.get_path()[0].pop(0)
            return node.get_operator()

        return None

    def pending_plan(self):
        return self.__plan

    def plot(self, steps, heuristics, goal, world_model, closed=[]):
        board = np.zeros(world_model.get_width() * world_model.get_height()).reshape(world_model.get_width(),
                                                                                     world_model.get_height())

        for c in steps:
            board[c.get_state().get_x(), c.get_state().get_y()] = heuristics[c.get_state()]
        for cc in closed:
            board[cc.get_x(), cc.get_y()] = 900
        for a, b in heuristics.items():
            board[a.get_x(), a.get_y()] = b
        # if goal:
        #     board[goal.get_x(), goal.get_y()] = 1

        data = pandas.DataFrame(board)
        plot_table(data)
        plt.show()

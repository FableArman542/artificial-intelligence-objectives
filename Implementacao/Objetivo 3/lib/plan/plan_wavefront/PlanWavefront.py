import copy
import numpy as np
from lib.plan.Planner import Planner
from lib.pee.wavefront.wavefront import WaveFront
from lib.pee.searchengine.Node import Node
from lib.pee.probmod.Solution import Solution


class PlanWavefront(Planner):

    def __init__(self):
        self.__plan = None

    def __select_action(self, state, operators, values):
        a = []
        for operator in operators:
            new_state = operator.apply(state)
            if new_state is not None and new_state:
                cost = operator.cost(state, new_state)

                if new_state in values and new_state:
                    value = values[new_state]
                    a.append([operator, value])
        a = np.asarray(a)
        print("a",a, "state",state)
        index = a[:, 1].tolist().index(max(a[:, 1]))

        a = a.tolist()

        return a[index][0]

    def plan(self, world_model, initial_state, objective):
        wavefront = WaveFront(world_model.get_operators())
        values = wavefront.run_algoritm(world_model.get_objective())
        # wavefront.plot()
        print("values", values)
        state = copy.deepcopy(initial_state)

        solution = Solution()

        path = []
        while state != objective:
            action = self.__select_action(state, world_model.get_operators(), values)
            new_state = action.apply(state)
            path.append(Node(state, action))
            state = new_state

        solution.set_path([path])
        solution.set_closed_nodes([values])

        self.__plan = solution

    def finish_plan(self):
        self.__plan = None

    def pending_plan(self):
        return self.__plan

    def get_operator(self):
        if len(self.__plan.get_path()) == 0:
            return None

        if self.__plan.get_path()[0] is not None and len(self.__plan.get_path()[0]) > 0:

            node = self.__plan.get_path()[0].pop(0)

            return node.get_operator()

        return None

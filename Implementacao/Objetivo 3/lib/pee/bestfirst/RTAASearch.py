import numpy as np
from lib.pee.bestfirst.BestFirstSearch import BestFirstSearch


class RTAASearch(BestFirstSearch):

    def __init__(self):
        super().__init__()
        self.h = {}

    def f(self, node):
        heuristic = self.problem.heuristic(node.get_state())
        return node.get_cost() + self.h.get(node.get_state(), heuristic)

    def __select_action(self, u, operators):
        actions = []
        for operator in operators:
            new_state = operator.apply(u)
            if new_state is not None:
                f = operator.cost(u, new_state) + self.h.get(new_state, float('inf'))
                actions.append([operator, f, new_state])

        actions = np.asarray(actions)
        if len(actions) == 0:
            print("ERROR: unachievable goal!")
            return None

        index = actions[:, 1].tolist().index(min(actions[:, 1]))
        actions = actions.tolist()
        return actions[index][0]

    def navigate(self, movements, current_state, new_state, operators, policy):
        while current_state != new_state and movements > 0:
            action = self.__select_action(current_state, operators)
            if action is None:
                return None
            state = action.apply(current_state)

            policy[current_state] = action
            current_state = state
            movements -= 1
        return current_state

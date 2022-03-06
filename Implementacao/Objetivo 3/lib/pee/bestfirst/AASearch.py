from lib.pee.bestfirst.BestFirstSearch import BestFirstSearch


class AASearch(BestFirstSearch):

    def f(self, node):
        return node.get_cost() + self.problem.heuristic(node.get_state())

from lib.pee.bestfirst.BestFirstSearch import BestFirstSearch


class GreedySearch(BestFirstSearch):

    def f(self, node):
        return self.problem.heuristic(node.get_state())

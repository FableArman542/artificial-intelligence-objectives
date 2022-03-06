import sys
from lib.pee.searchengine.Node import Node
from lib.pee.probmod.Solution import Solution


class SearchEngine:

    def __init__(self):
        self.problem = None
        self.__search_memory = self._start_memory()

    def _start_memory(self):
        raise NotImplementedError("Abstract")

    def get_search_memory(self):
        return self.__search_memory

    def solve(self, problem, max_depth=sys.maxsize):
        self.problem = problem
        self.__search_memory.clean()

        initial_node = Node(problem.get_initial_state())
        self.__search_memory.insert(initial_node)

        while self.__search_memory.empty_border() is False:
            node = self.__search_memory.remove()
            if problem.is_objective(node.get_state()):
                return self.__generate_solution(node)
            elif node.get_depth() < max_depth:
                self.__expand(node)
            elif node.get_depth() >= max_depth:
                return self.__generate_solution(node)

        return None

    def __expand(self, node):
        state = node.get_state()
        operators = self.problem.get_operators()
        for operator in operators:
            suc_state = operator.apply(state)
            if suc_state is not None:
                suc_node = Node(suc_state, operator, node)
                self.__search_memory.insert(suc_node)

    def __generate_solution(self, final_node):
        # path = []
        solution = Solution()
        node = final_node
        while node is not None:
            # path.insert(0, node)
            solution.insert_in_solution(node)
            predecessor = node.get_predecessor()
            node = predecessor
        solution.set_closed_nodes(self.__search_memory.get_closed())
        solution.set_final_node(final_node)

        return solution

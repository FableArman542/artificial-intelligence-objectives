

class Node:

    def __init__(self, state, operator=None, predecessor=None):
        self.__state = state
        self.__operator = operator
        self.__predecessor = predecessor
        if predecessor is None:
            self.__depth = 0
            self.__cost = 0
        else:
            self.__depth = self.__predecessor.get_depth() + 1
            self.__cost = self.__predecessor.get_cost() + self.__operator.cost(predecessor.get_state(), state)

    def get_state(self):
        return self.__state

    def get_operator(self):
        return self.__operator

    def get_predecessor(self):
        return self.__predecessor

    def get_depth(self):
        return self.__depth

    def get_cost(self):
        return self.__cost

    def __str__(self):
        return str(self.__state)

    def __eq__(self, other):
        return self.get_state() == other.get_state()

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.__cost < other.get_cost()

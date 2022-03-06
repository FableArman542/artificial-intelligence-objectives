from lib.reinforcement_learning.learning_engine.memory.LearnMemory import LearnMemory


class SparseMemory(LearnMemory):

    def __init__(self, default_value=0.0):
        self.__default_value = default_value
        self.__memory = {}

    def Q(self, s, a):
        return self.__memory.get((s, a), self.__default_value)

    def update(self, s, a, q):
        self.__memory[(s, a)] = q

    def get_memory(self):
        return self.__memory

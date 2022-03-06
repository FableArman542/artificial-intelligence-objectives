from lib.reinforcement_learning.Learning import Learning
from lib.reinforcement_learning.learning_engine.memory.SparseMemory import SparseMemory
from lib.reinforcement_learning.learning_engine.action.EGreedy import EGreedy
from lib.reinforcement_learning.learning_engine.learning.dynaq.DynaQ import DynaQ


class LearningEngine(Learning):

    def __init__(self, actions):
        self.__actions = actions
        self.__learn_memory = SparseMemory()
        self.__sel_action = EGreedy(self.__learn_memory, self.__actions, 0.9)
        self.__learning_ref = DynaQ(self.__learn_memory, self.__sel_action, 0.5, 0.9, 100)

    def learn(self, s, a, r, sn, an=None):
        self.__learning_ref.learn(s, a, r, sn, an=None)

    def select_action(self, s):
        return self.__sel_action.select_action(s)

    def get_learn_memory(self):
        return self.__learn_memory

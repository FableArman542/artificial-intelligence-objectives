from random import random
from random import choice
from lib.reinforcement_learning.learning_engine.action.SelAction import SelAction


class EGreedy(SelAction):

    def __init__(self, learn_memory, actions, epsilon):
        self.__learn_memory = learn_memory
        self.__actions = actions
        self.__epsilon = epsilon

    def max_action(self, s):
        return max(self.__actions, key=lambda a: self.__learn_memory.Q(s, a))

    def benefit(self, s):
        return self.max_action(s)

    def explore(self):
        return choice(self.__actions)

    def select_action(self, s):
        action = None
        self.__epsilon = self.__epsilon*0.9
        if random() > self.__epsilon:
            action = self.benefit(s)
        else:
            action = self.explore()
        return action

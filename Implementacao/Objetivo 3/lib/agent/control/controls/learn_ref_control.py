from lib.agent.control.control import Control
from lib.plan.probmod.WorldModel import WorldModel
from lib.reinforcement_learning.learning_engine.LearningEngine import LearningEngine


class LearnRefControl(Control):

    def __init__(self):
        self.__rmax = 100.0
        self.__s = None
        self.__a = None
        self.finished = False
        self.__world_model = WorldModel()
        self.__learn_engine = LearningEngine(self.__world_model.get_operators())

    def process(self, perception, view):
        self.__world_model.update_world(perception)
        sn = perception.state
        an = self.__learn_engine.select_action(sn)

        r = self.__generate_reinforcement(sn)

        if self.__s is not None and self.__a is not None:
            self.__learn_engine.learn(self.__s, self.__a, r, sn)

        view.show_plan(self.__learn_engine.get_learn_memory().get_memory())

        self.__s = sn
        self.__a = an
        return self.__a

    def __generate_reinforcement(self, sn):
        r = -1

        # Objective found
        if self.__world_model.objective_state is None:
            self.finished = True
            return self.__rmax

        cost = 0

        if self.__a is not None:
            cost = self.__a.cost(self.__s, sn)
        else:
            return 0

        if cost == 0:
            r = -1*self.__rmax
        else:
            r = -1*cost

        return r

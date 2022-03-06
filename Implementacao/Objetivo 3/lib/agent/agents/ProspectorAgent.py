import copy

from lib.agent.agent import Agent
from lib.agent.effector.Effector import Effector
from lib.agent.control.controls.learn_ref_control import LearnRefControl
from lib.agent.sensor.Sensor import Sensor


class ProspectorAgent(Agent):

    def __init__(self, control, world):
        self.__control = control
        self.__world = world
        self.__effector = Effector(self.__world)
        self.__sensor = Sensor(self.__world)

        self.__start_state = copy.deepcopy(self.__world.state)
        self.__objective_state = copy.deepcopy(self.__world.objective_state)

    def execute(self, view):
        if self.__control.finished and isinstance(self.__control, LearnRefControl):
            self.__restart()
        perception = self.__precept()
        operator = self.__process(perception, view)

        if self.__control.finished and isinstance(self.__control, LearnRefControl):
            self.__restart()

        self.__act(operator)

    def __precept(self):
        return self.__sensor.precept()

    def __process(self, perception, view):
        return self.__control.process(perception, view)

    def __act(self, operator):
        if operator is not None:
            self.__effector.act(operator)

    def __restart(self):
        self.__world.state = copy.deepcopy(self.__start_state)
        self.__world.objective_state = copy.deepcopy(self.__objective_state)
        self.__control.finished = False

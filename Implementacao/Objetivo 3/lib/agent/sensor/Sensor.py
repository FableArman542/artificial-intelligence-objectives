from lib.agent.sensor.perception.Perception import Perception


class Sensor:

    def __init__(self, world):
        self.__world = world

    def precept(self):
        return Perception(self.__world.width, self.__world.height, self.__world.state, self.__world.objective_state, self.__world.blocks)

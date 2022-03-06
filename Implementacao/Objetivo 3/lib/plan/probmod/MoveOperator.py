import math
from lib.pee.probmod.Operator import Operator


class MoveOperator(Operator):

    def __init__(self, world_model, direction):
        self.__world_model = world_model
        self.__dir = direction

    def apply(self, state):
        next_state = None

        x_coordinates = state.get_x() + self.__dir[0]
        y_coordinates = state.get_y() + self.__dir[1]

        # print("Coordinates", x_coordinates, y_coordinates)
        # print(self.__world_model.height > x_coordinates >= 0, self.__world_model.width > y_coordinates >= 0)
        # print()
        if self.__world_model.height > x_coordinates >= 0 \
                and self.__world_model.width > y_coordinates >= 0:
            # print("hereee")
            next_state = self.__world_model.get_state(x_coordinates, y_coordinates)
        # print("--nextstate", next_state)

        return next_state

    def cost(self, state, suc_state):
        x = math.pow(state.get_x() - suc_state.get_x(), 2)
        y = math.pow(state.get_y() - suc_state.get_y(), 2)
        val = math.sqrt(x + y)
        return val

    def get_direction(self):
        return self.__dir

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.__dir)

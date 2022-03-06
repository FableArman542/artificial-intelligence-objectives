from lib.pee.probmod.State import State


class PlanState(State):

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def __key(self):
        return self.__x, self.__y

    def __hash__(self):
        return hash(self.__key())

    def __str__(self):
        return "("+str(self.get_x())+", " + str(self.get_y()) + ")"

    def __repr__(self):
        return self.__str__()

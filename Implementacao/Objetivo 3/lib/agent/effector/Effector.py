

class Effector:

    def __init__(self, world):
        self.__world = world
        self.__action = None

    def act(self, operator):
        self.__action = operator
        if self.__world.state is not None and self.__world.objective_state is not None:
            # print("(agent):", self.__world.state, operator, end=" ")
            new_state = operator.apply(self.__world.state)
            if new_state is not None:
                self.__world.state = new_state
            # print("|", new_state)
            if self.__world.state == self.__world.objective_state:
                self.__world.objective_state = None

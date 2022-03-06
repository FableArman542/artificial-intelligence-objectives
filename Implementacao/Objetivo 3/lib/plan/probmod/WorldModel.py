from lib.plan.probmod.PlanState import PlanState
from lib.plan.probmod.MoveOperator import MoveOperator


class WorldModel:

    def __init__(self, width=None, height=None, state=None, objective_state=None, blocks=[]):
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, -1], [-1, 1]]
        self.width = width
        self.height = height
        self.state = state
        self.objective_state = objective_state
        self.blocks = blocks
        self.__operators = [MoveOperator(self, d) for d in directions]

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_operators(self):
        return self.__operators

    def get_state(self, x, y):
        for block in self.blocks:
            if block.get_x() == x and block.get_y() == y:
                return None
        if self.objective_state is not None:
            if self.objective_state.get_x() == x and self.objective_state.get_y() == y:
                return PlanState(x, y)

        return PlanState(x, y)

    def update_world(self, perception):
        if perception is not None:
            self.width = perception.width
            self.height = perception.height
            self.state = perception.state
            self.objective_state = perception.objective_state
            self.blocks = perception.blocks

    def state(self):
        return self.state

    def get_objective(self):
        return self.objective_state

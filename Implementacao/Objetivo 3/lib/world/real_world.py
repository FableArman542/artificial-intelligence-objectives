from lib.plan.probmod.MoveOperator import MoveOperator


class RealWorld:

    def __init__(self, width, height, state, objective_state, blocks=[]):
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, -1], [-1, 1]]
        self.width = width
        self.height = height
        self.state = state
        self.objective_state = objective_state
        self.blocks = blocks
        self.operators = [MoveOperator(self, d) for d in directions]
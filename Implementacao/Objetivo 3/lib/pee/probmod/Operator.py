

class Operator:
    def apply(self, state):
        raise NotImplementedError("Interface")

    def cost(self, state, suc_state):
        raise NotImplementedError("Interface")

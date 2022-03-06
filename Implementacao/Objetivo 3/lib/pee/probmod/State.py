

class State:
    def __eq__(self, state):
        return hash(self) == hash(state)

    def __hash__(self):
        raise NotImplementedError("Abstract")
    
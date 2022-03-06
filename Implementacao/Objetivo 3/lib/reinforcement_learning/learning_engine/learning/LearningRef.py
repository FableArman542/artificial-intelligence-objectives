

class LearningRef:

    def __init__(self, learn_memory, sel_action, alpha, gama):
        self._learn_memory = learn_memory
        self._sel_action = sel_action
        self._alpha = alpha
        self._gama = gama

    def learn(self, s, a, r, sn, an=None):
        raise NotImplementedError("Abstract")

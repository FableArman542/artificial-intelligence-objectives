from random import choice


class TRModel:

    def __init__(self):
        self.T = {}
        self.R = {}

    def update(self, s, a, r, sn):
        self.T[(s, a)] = sn
        self.R[(s, a)] = r

    def sample(self):
        s, a = choice(list(self.T))
        sn = self.T[(s, a)]
        r = self.R[(s, a)]
        return s, a, r, sn

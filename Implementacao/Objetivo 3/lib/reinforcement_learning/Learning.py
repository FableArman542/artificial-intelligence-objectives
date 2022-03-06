

class Learning:

    def select_action(self, s):
        raise NotImplementedError("Interface")

    def learn(self, s, a, r, sn, an):
        raise NotImplementedError("Interface")
    
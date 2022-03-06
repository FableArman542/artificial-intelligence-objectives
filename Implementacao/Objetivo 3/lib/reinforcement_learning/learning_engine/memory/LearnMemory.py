

class LearnMemory:

    def update(self, s, a, q):
        raise NotImplementedError("Interface")

    def Q(self, s, a):
        raise NotImplementedError("Interface")

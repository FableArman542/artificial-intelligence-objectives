

class Problem:

    def get_random_state(self, state):
        raise NotImplementedError("interface")

    def fitness_function(self, state):
        raise NotImplementedError("interface")

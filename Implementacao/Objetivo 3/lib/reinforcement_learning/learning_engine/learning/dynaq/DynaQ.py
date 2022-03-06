from lib.reinforcement_learning.learning_engine.learning.qlearning.QLearning import QLearning
from lib.reinforcement_learning.learning_engine.learning.dynaq.TRModel import TRModel


class DynaQ(QLearning):

    def __init__(self, learn_memory, sel_action, alpha, gama, num_sim):
        super(DynaQ, self).__init__(learn_memory, sel_action, alpha, gama)
        self.num_sim = num_sim
        self.model = TRModel()

    def learn(self, s, a, r, sn, an=None):
        super().learn(s, a, r, sn)
        self.model.update(s, a, r, sn)
        self.simulate()

    def simulate(self):
        for i in range(self.num_sim):
            s, a, r, sn = self.model.sample()
            super().learn(s, a, r, sn)

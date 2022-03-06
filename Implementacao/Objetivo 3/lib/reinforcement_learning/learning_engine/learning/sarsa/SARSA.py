from lib.reinforcement_learning.learning_engine.learning.LearningRef import LearningRef


class SARSA(LearningRef):

    def learn(self, s, a, r, sn, an=None):
        qsa = self._learn_memory.Q(s, a)
        qsnan = self._learn_memory.Q(sn, an)
        q = qsa + self._alpha * (r + self._gama * qsnan - qsa)
        self._learn_memory.update(s, a, q)

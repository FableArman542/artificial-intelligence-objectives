from lib.reinforcement_learning.learning_engine.learning.LearningRef import LearningRef


class QLearning(LearningRef):

    def learn(self, s, a, r, sn, an=None):
        an = self._sel_action.max_action(sn)
        qsa = self._learn_memory.Q(s, a)
        qsnan = self._learn_memory.Q(sn, an)
        q = qsa + self._alpha * (r + self._gama * qsnan - qsa)
        self._learn_memory.update(s, a, q)

        # max_key = max(self._learn_memory.get_memory(), key=self._learn_memory.get_memory().get)

        # print(max_key, self._learn_memory.get_memory()[max_key])

import numpy as np
from lib.GeneticLibrary.Crossover.Crossover import Crossover


class MultiPointCrossover(Crossover):
    def apply(self, chromosome_1, chromosome_2):
        percurso1 = chromosome_1
        percurso2 = chromosome_2

        cut_point1 = -1
        while True:
            cut_point1 = np.random.randint(1, len(percurso1))
            if cut_point1 < len(percurso1) - 1: break

        cut_point2 = np.random.randint(cut_point1 + 1, len(percurso1))

        percurso1 = np.asarray(percurso1)
        percurso2 = np.asarray(percurso2)

        cut_percurso1 = percurso1[cut_point1:cut_point2 + 1]
        cut_percurso2 = percurso2[cut_point1:cut_point2 + 1]

        next_percurso1 = percurso1[cut_point2 + 1::]
        next_percurso2 = percurso2[cut_point2 + 1::]

        before_percurso1 = percurso1[:cut_point1]
        before_percurso2 = percurso2[:cut_point1]

        p1 = np.hstack((next_percurso1, before_percurso1, cut_percurso1))

        p2 = np.hstack((next_percurso2, before_percurso2, cut_percurso2))

        p1 = p1.tolist()
        for a in cut_percurso2:
            if a in p1: p1.remove(a)

        p2 = p2.tolist()

        for a in cut_percurso1:
            if a in p2: p2.remove(a)
        p1 = np.asarray(p1)
        p2 = np.asarray(p2)

        percurso1_start = []
        deleted = "error"
        for i in range(len(next_percurso1)):
            percurso1_start.append(p1[i])
            deleted = i

        if deleted != "error":
            percurso1_end = p1[deleted + 1:]
        else:
            percurso1_end = p1

        percurso2_start = []
        deleted = "error"
        for i in range(len(next_percurso2)):
            percurso2_start.append(p2[i])
            deleted = i

        if deleted != "error":
            percurso2_end = p2[deleted + 1:]
        else:
            percurso2_end = p2

        percurso1d = np.hstack((percurso1_end, cut_percurso2, percurso1_start))
        percurso2d = np.hstack((percurso2_end, cut_percurso1, percurso2_start))

        return percurso1d, percurso2d


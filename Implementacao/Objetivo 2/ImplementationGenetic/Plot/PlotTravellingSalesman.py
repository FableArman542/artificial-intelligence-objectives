import numpy as np
import matplotlib.pyplot as plt
from lib.GeneticLibrary.Plot.Plot import Plot


class PlotTravellingSalesman(Plot):

    def __init__(self, state, geo_coordinates):
        self.__state = state
        self.__geo_coordinates = geo_coordinates

    def plot_state(self):
        route = []
        city_labels = []

        index = 0
        first = None
        for city in self.__state:
            route.append([self.__geo_coordinates[city][0], self.__geo_coordinates[city][1]])
            city_labels.append(city)
            if index == 0:
                first = [[self.__geo_coordinates[city][0], self.__geo_coordinates[city][1]], city]
            if index == len(self.__state)-1:
                route.append(first[0])
                city_labels.append(first[1])
            index += 1
        route = np.asarray(route)

        for i, txt in enumerate(city_labels):
            plt.annotate(txt, (route[:, 0][i], route[:, 1][i]))

        plt.scatter(route[:, 0], route[:, 1])
        plt.plot(route[:, 0], route[:, 1])
        plt.show()

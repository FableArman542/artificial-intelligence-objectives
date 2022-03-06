import numpy as np
import matplotlib.pyplot as plt
from lib.OptimizationLibrary.Plot.Plot import Plot


class PlotTravellingSalesman(Plot):

    def __init__(self, state, geo_coordinates):
        self.__state = state
        self.__geo_coordinates = geo_coordinates

    def plot_state(self):
        route = []
        city_labels = []
        for city in self.__state:
            route.append([self.__geo_coordinates[city][0], self.__geo_coordinates[city][1]])
            city_labels.append(city)
        route = np.asarray(route)

        for i, txt in enumerate(city_labels):
            plt.annotate(txt, (route[:, 0][i], route[:, 1][i]))

        plt.scatter(route[:, 0], route[:, 1])
        plt.plot(route[:, 0], route[:, 1])
        plt.show()

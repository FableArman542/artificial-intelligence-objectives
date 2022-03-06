import copy
import sys
import numpy as np
import pygame as pg
from lib.pee.searchengine.Node import Node
from scipy.interpolate import interp1d

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)
RED = (200, 0, 0)
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800
FPS = 50


class Simulation:
    def __init__(self, world, agent):
        self.__world = world
        self.__agent = agent
        self.__plan = None

        self.__screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.__block_size_y = int(WINDOW_WIDTH / self.__world.width)
        self.__block_size_x = int(WINDOW_HEIGHT / self.__world.height)
        self.__y_coordinates = np.arange(0, WINDOW_WIDTH, self.__block_size_y)
        self.__x_coordinates = np.arange(0, WINDOW_HEIGHT, self.__block_size_x)

        self.load_images()


    def run(self):
        pg.init()
        clock = pg.time.Clock()
        running = True


        while running:
            dt = clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            # self.__screen.fill(BLACK)

            self.__draw_grid()

            if self.__plan:
                self.show_plan(self.__plan)

            self.__draw_world()

            self.__agent.execute(self)

            pg.display.update()

    def load_images(self):
        arrow_up = pg.transform.scale(pg.image.load('lib/display/resources/arrows/arrow_up.png'),
                                      (self.__block_size_y, self.__block_size_x))
        arrow_down = pg.transform.scale(pg.image.load('lib/display/resources/arrows/arrow_down.png'),
                                        (self.__block_size_y, self.__block_size_x))
        arrow_left = pg.transform.scale(pg.image.load('lib/display/resources/arrows/arrow_left.png'),
                                        (self.__block_size_y, self.__block_size_x))
        arrow_right = pg.transform.scale(pg.image.load('lib/display/resources/arrows/arrow_right.png'),
                                         (self.__block_size_y, self.__block_size_x))
        arrow_right_up = pg.transform.scale(pg.image.load('lib/display/resources/arrows/arrow_right_up.png'),
                                            (self.__block_size_y, self.__block_size_x))
        arrow_right_down = pg.transform.scale(pg.image.load('lib/display/resources/arrows/arrow_right_down.png'),
                                              (self.__block_size_y, self.__block_size_x))
        arrow_left_up = pg.transform.scale(pg.image.load('lib/display/resources/arrows/arrow_left_up.png'),
                                           (self.__block_size_y, self.__block_size_x))
        arrow_left_down = pg.transform.scale(pg.image.load('lib/display/resources/arrows/arrow_left_down.png'),
                                             (self.__block_size_y, self.__block_size_x))
        self.__objective = pg.transform.scale(pg.image.load('lib/display/resources/objective.png'),
                                              (self.__block_size_y, self.__block_size_x))
        self.__agent_image = pg.transform.scale(pg.image.load('lib/display/resources/agent.png'),
                                                (self.__block_size_y, self.__block_size_x))
        self.__obstacle = pg.transform.scale(pg.image.load('lib/display/resources/block.jpg'),
                                             (self.__block_size_y, self.__block_size_x))

        self.__directions = [[1, 0],
                             [-1, 0],
                             [0, 1],
                             [0, -1],
                             [1, 1],
                             [-1, 1],
                             [1, -1],
                             [-1, -1]]

        self.__arrows = [arrow_down,
                         arrow_up,
                         arrow_right,
                         arrow_left,
                         arrow_right_down,
                         arrow_right_up,
                         arrow_left_down,
                         arrow_left_up]

    def __draw_grid(self):
        for x in self.__x_coordinates:
            for y in self.__y_coordinates:
                agente = self.__world.state
                if self.__y_coordinates[agente.get_y()] != y and self.__x_coordinates[agente.get_x()] != x:
                    rect = pg.Rect(y, x, self.__block_size_y, self.__block_size_x)
                    pg.draw.rect(self.__screen, (25, 25, 25), rect)
                    pg.draw.rect(self.__screen, BLACK, rect, 1)

    def __draw_world(self):
        # Draw Objective State
        objective = self.__world.objective_state
        if objective is not None:
            self.__screen.blit(self.__objective, (self.__y_coordinates[objective.get_y()],
                                                  self.__x_coordinates[objective.get_x()]))

        # Draw the agent
        agent_state = self.__world.state
        self.__screen.blit(self.__agent_image, (self.__y_coordinates[agent_state.get_y()],
                                                self.__x_coordinates[agent_state.get_x()]))

        # Draw obstacles
        obstacles = self.__world.blocks
        for obstacle in obstacles:
            self.__screen.blit(self.__obstacle, (self.__y_coordinates[obstacle.get_y()],
                                                 self.__x_coordinates[obstacle.get_x()]))

    def show_plan(self, plan):
        self.__plan = copy.deepcopy(plan)

        # Reinforcement Learning draw arrows
        try:
            states = {}
            values = {}
            for s, val in self.__plan.items():
                state = s[0]
                action = s[1]
                value = states.get(state, None)
                if value is None:
                    states[state] = (action, val)
                    values[state] = val
                else:
                    if val > value[1]:
                        states[state] = (action, val)
                        values[state] = val

            maximum = values[max(values, key=values.get)]
            minimum = values[min(values, key=values.get)]
            for s, av in states.items():
                counter = 0

                for i in range(len(self.__directions)):
                    t = av[0].get_direction()
                    if self.__directions[i] == t:
                        counter = i
                        break
                if s != self.__world.state and s != self.__world.objective_state:
                    rect = pg.Rect(self.__y_coordinates[s.get_y()], self.__x_coordinates[s.get_x()],
                                   self.__block_size_y, self.__block_size_x)
                    value = self.__map_values_to_rgb(maximum, minimum, av[1])
                    if av[1] > 0:
                        color = (0, value, 0)
                    else:
                        color = (value, 0, 0)
                    pg.draw.rect(self.__screen, color, rect)

                    self.__screen.blit(self.__arrows[counter], (self.__y_coordinates[s.get_y()],
                                                                self.__x_coordinates[s.get_x()]))
        except:
            print("", end="")
            # print("Not reeinforcement")

        # Draw utility
        try:
            if self.__plan.get_closed_nodes() is not None:
                d = {}
                for b in self.__plan.get_closed_nodes():
                    d.update(b)

                maximum = d[max(d, key=d.get)]
                minimum = d[min(d, key=d.get)]

                for a in self.__plan.get_closed_nodes():
                    for s, v in a.items():
                        rect = pg.Rect(self.__y_coordinates[s.get_y()], self.__x_coordinates[s.get_x()],
                                       self.__block_size_y, self.__block_size_x)
                        value = self.__map_values_to_rgb(maximum, minimum, v)

                        color = (0, value, 0)
                        pg.draw.rect(self.__screen, color, rect)
        except Exception as e:
            # print(e)
            print("",end="")

        # Draw Arrows
        try:
            index = 0
            for p in self.__plan.get_path():
                for node in p:
                    if node.get_operator() is not None:
                        direction = node.get_operator().get_direction()
                        counter = 0
                        for i in range(len(self.__directions)):
                            if self.__directions[i] == direction:
                                counter = i
                                break
                        self.__screen.blit(self.__arrows[counter], (self.__y_coordinates[node.get_state().get_y()],
                                                                    self.__x_coordinates[node.get_state().get_x()]))
                    if node == p[0] and index != 0:
                        rect = pg.Rect(self.__y_coordinates[node.get_state().get_y()],
                                       self.__x_coordinates[node.get_state().get_x()], self.__block_size_y - 1,
                                       self.__block_size_x - 1)
                        pg.draw.rect(self.__screen, WHITE, rect, 3)
                index += 1
        except:
            print("",end="")
            # print("No closed Nodes")

        # Draw Final Nodes
        try:
            for state in self.__plan.get_final_node():
                rect = pg.Rect(self.__y_coordinates[state.get_y()],
                               self.__x_coordinates[state.get_x()], self.__block_size_y - 1,
                               self.__block_size_x - 1)
                pg.draw.rect(self.__screen, WHITE, rect, 3)

        except:
            print("",end="")
            # print("No closed Nodes")

        return None

    def __map_values_to_rgb(self, maximum, minimum, value):
        to_add = 10
        if minimum < 0:
            to_add = -minimum + to_add

        to_multiply = 255 / (maximum + to_add)

        return (value + to_add) * to_multiply

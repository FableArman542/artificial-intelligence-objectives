import numpy as np
from lib.GeneticLibrary.Algorithm.Result import Result


class GeneticAlgorithm:

    def __init__(self, state, problem, selection, crossover, mutation, k_chromosomes, stop_criteria=None):
        self.__current_state = state
        self.__problem = problem

        self.__selection = selection
        self.__crossover = crossover
        self.__mutation = mutation

        if stop_criteria is not None:
            try:
                self.__stop_criteria = stop_criteria.split("_")
                self.__stop_criteria[1] = float(self.__stop_criteria[1])
            except:
                print("Stop Criteria has to be a string with format \"reach_number.\"")
        else:
            self.__stop_criteria = None

        self.__k_chromosomes = k_chromosomes

        self.__chromosomes = []
        self.__fitness_values = []

    def __generate_chromosomes(self):
        chromosomes = []
        fitness = []
        for i in range(int(self.__k_chromosomes)):
            chromosome = self.__problem.get_random_state(self.__current_state)
            chromosomes.append(chromosome)
            fitness.append(self.__problem.fitness_function(chromosome))

        return chromosomes, fitness

    def __check_stop_criteria(self):
        if len(self.__stop_criteria) != 2:
            print("Stop Criteria has only two arguments, \"str_keyword\" and \"float_number[0,1]\"")
            return False
        if self.__stop_criteria[0] != "reach":
            print("Stop Criteria first argument has only the following possibilities:", ["reach"])
            return False
        if type(self.__stop_criteria[1]) != float:
            print("Stop Criteria second argument has to be a float number, not", type(self.__stop_criteria[1]))
            return False
        return True

    def run_algorithm(self, max_number_of_generations=100, probability_of_mutation=.05):
        # Generate chromosome * k_chromosomes
        self.__chromosomes, self.__fitness_values = self.__generate_chromosomes()
        best_of_generation = self.__chromosomes[np.argmax(self.__fitness_values)]

        for i in range(max_number_of_generations):
            # Each generation is composed by 10 chromosomes
            new_population = []

            # Roulette Selection
            selected_chromosomes = self.__selection.apply(self.__chromosomes, self.__fitness_values,
                                                          number_of_selection=int(self.__k_chromosomes))

            children = []
            # Generate through cross over 2 by 2
            for first, second in zip(selected_chromosomes, selected_chromosomes[1:]):
                parent1 = first
                parent2 = second

                child1, child2 = self.__crossover.apply(parent1, parent2)
                children.append(child1)
                children.append(child2)

            # Generate through mutation
            m = [True, False]
            for child in children:
                to_mutate = np.random.choice(m, p=[probability_of_mutation, 1 - probability_of_mutation])
                if to_mutate:
                    child = self.__mutation.apply(child)
                new_population.append(child)

            self.__chromosomes = new_population
            self.__fitness_values = [self.__problem.fitness_function(chromosome) for chromosome in self.__chromosomes]

            latest_iteration = i
            best_of_generation = self.__chromosomes[np.argmax(self.__fitness_values)].tolist()

            # Finish Criteria
            if self.__stop_criteria is not None:
                stop_accepted = self.__check_stop_criteria()
                if stop_accepted and self.__stop_criteria[0] == "reach":
                    max_value = np.max(self.__fitness_values)
                    if max_value == self.__stop_criteria[1]:
                        break
                elif stop_accepted is False:
                    self.__stop_criteria = None

        return Result(best_of_generation, np.max(self.__fitness_values), latest_iteration)

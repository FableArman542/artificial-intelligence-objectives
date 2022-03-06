import numpy as np


class Problem:
    def get_cost_of_state(self, state):
        raise NotImplementedError("abstract")

    def get_random_state(self, state):
        raise NotImplementedError("abstract")

    def get_all_neighbours(self, state):
        raise NotImplementedError("abstract")
    
    def choose_best_state(self, neighbours):
        best_route_cost = self.get_cost_of_state(neighbours[0])
        best_state = neighbours[0]
        for neighbour in neighbours:
            current_cost = self.get_cost_of_state(neighbour)
            if current_cost < best_route_cost:
                best_route_cost = current_cost
                best_state = neighbour
        
        best_state.append(best_state[0])
        
        return best_state, best_route_cost
        
    def get_random_neighbour(self, neighbours):
        random_index = np.random.randint(0, len(neighbours))
        state = neighbours[random_index]
        
        return state

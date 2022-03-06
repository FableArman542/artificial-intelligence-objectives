

class SearchMemory():

    def __init__(self):
        self.clean()

    def clean(self):
        self._border = []
        self._closed = {}
        self._exploited = {}

    def insert(self, node):
        current_state = node.get_state()
        previous_node = self._exploited.get(current_state)

        if previous_node is None or node.get_cost() < previous_node.get_cost():
            self._insert_in_border(node)
            self.__insert_in_exploited(current_state, node)

    def remove(self):
        node = self._remove_from_border()
        self.__insert_in_closed(node)
        return node

    def empty_border(self):
        return len(self._border) == 0

    def _insert_in_border(self, node):
        self._border.append(node)
    
    def __insert_in_exploited(self, state, node):
        self._exploited[state] = node

    def __insert_in_closed(self, node):
        self._closed[node.get_state()] = node
    
    def _remove_from_border(self):
        return self._border.pop(0)

    def get_exploited(self):
        return self._exploited

    def get_closed(self):
        return self._closed

    def get_border(self):
        return self._border

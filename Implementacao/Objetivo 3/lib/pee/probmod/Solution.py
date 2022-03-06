

class Solution:
    def __init__(self):
        self.__path = []
        self.__closed_nodes = None
        self.__final_node = None

    def insert_last_in_solution(self, node):
        self.__path.append(node)

    def insert_in_solution(self, node):
        self.__path.insert(0, node)

    def set_closed_nodes(self, closed):
        self.__closed_nodes = closed

    def set_final_node(self, final_node):
        self.__final_node = final_node

    def get_closed_nodes(self):
        return self.__closed_nodes

    def get_final_node(self):
        return self.__final_node

    def get_path(self):
        return self.__path

    def set_path(self, path):
        self.__path = path

    def __str__(self):
        return str(self.__path)

from heapq import heappush, heappop
from lib.pee.searchengine.memory.SearchMemory import SearchMemory


class PriorityMemory(SearchMemory):

    def __init__(self, priority):
        super().__init__()
        self.__priority = priority

    def _insert_in_border(self, node):
        p = self.__priority(node)
        heappush(self._border, (p, node))

    def _remove_from_border(self):
        _, node = heappop(self._border)
        return node

from lib.pee.searchengine.SearchEngine import SearchEngine
from lib.pee.searchengine.memory.PriorityMemory import PriorityMemory


class BestFirstSearch(SearchEngine):

    def _start_memory(self):
        return PriorityMemory(self.f)

    def f(self, node):
        raise NotImplementedError("Abstract")

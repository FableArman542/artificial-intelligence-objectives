from lib.pee.searchengine.SearchEngine import SearchEngine
from lib.pee.searchengine.memory.FIFOMemory import FIFOMemory


class BreadthFirstSearch(SearchEngine):

    def _start_memory(self):
        return FIFOMemory()

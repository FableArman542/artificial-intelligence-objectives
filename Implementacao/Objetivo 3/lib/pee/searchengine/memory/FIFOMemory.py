from lib.pee.searchengine.memory.SearchMemory import SearchMemory


class FIFOMemory(SearchMemory):

    def _insert_in_border(self, node):
        self._border.append(node)

    def _remove_from_border(self):
        return self._border.pop(0)

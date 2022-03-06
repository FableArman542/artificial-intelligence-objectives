from lib.pee.searchengine.SearchEngine import SearchEngine


class SearchBestFirst(SearchEngine):

    def f(self, node):
        raise NotImplementedError("Abstract")
    
from .search_data import Search as _Search

_search_instance = _Search()

search = _search_instance

__all__ = [ 'search']


import abc

from . import collection as _collection


class _Value(object):
    __slots__ = ()

    def __init__(self, *, collection=None, **kwargs):
        if collection is None:
            collection = _collection.global_collection
        collection.add(kwargs, self)

    @abc.abstractmethod
    def _get_size(self):
        pass

import abc
import logging

from . import collection as _collection
from .py2_compat import MemoryView


log = logging.getLogger(__name__)


class _Value(object):
    __slots__ = ('_memoryview',)

    def __init__(self, *args, **kwargs):
        if args:
            raise TypeError("No positional arguments expected")
        collection = kwargs.pop('collection', None)
        if collection is None:
            collection = _collection.global_collection
        collection.add(kwargs, self)

        log.debug("New %s:%x with params %r",
                  self.__class__.__name__, id(self), kwargs)

        # Create temporary view, this is useful if you enter some branch of
        # code in unusual code path such as ipython shell or management
        # commands. Counters are not useful in this case but should not crash,
        # so you don't need a lot of `if` statements
        vtype, _ = self._get_type()
        size = self._get_size()
        self._memoryview = MemoryView(bytearray(size)).cast(vtype)

    @abc.abstractmethod
    def _get_size(self):
        pass

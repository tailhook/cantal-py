from .core import _Value


class Counter(_Value):
    __slots__ = ()

    def __iadd__(self, value):
        self._memoryview[0] += value
        return self

    def incr(self, value=1):
        self._memoryview[0] += value

    def _get_size(self):
        return 8

    def _get_type(self):
        return ('L', 'counter 8')

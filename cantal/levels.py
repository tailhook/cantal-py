from .core import _Value


class Float(_Value):
    __slots__ = ()

    def incr(self, value=1):
        self._memoryview[0] = value

    __iadd__ = incr

    def _get_size(self):
        return 8

    def _get_type(self):
        return ('d', 'level 8 float')

    def set(self, value):
        self._memoryview[0] = value

    def __setitem__(self, key, value):
        assert key == 0, "Only single value is expected"
        self._memoryview[key] = value


class Integer(_Value):
    __slots__ = ()

    def _get_size(self):
        return 8

    def _get_type(self):
        return ('l', 'level 8 signed')

    def set(self, value):
        self._memoryview[0] = value

    def get(self):
        return self._memoryview[0]

    def incr(self, value=1):
        self._memoryview[0] += value

    def decr(self, value=1):
        self._memoryview[0] -= value

    def __setitem__(self, key, value):
        assert key == 0, "Only single value is expected"
        self._memoryview[key] = value

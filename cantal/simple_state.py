import time
import struct
import warnings
from contextlib import contextmanager

from .core import _Value
from .const import CACHE_LINE_SIZE


_timestr = struct.Struct('L')


class State(_Value):
    __slots__ = ('_memoryview', 'size')
    HEADER_SIZE = _timestr.size
    assert HEADER_SIZE == 8, 'We use constants in enter/exit/context'

    def __init__(self, size=CACHE_LINE_SIZE-HEADER_SIZE, **kwargs):
        sz = size + self.HEADER_SIZE
        if sz & (sz - 1) or sz % CACHE_LINE_SIZE:
            warnings.warning(
                "Size of state counter should be multiple of {} or smaller"
                "power of two sans header size ({}), perfect size is {}"
                .format(CACHE_LINE_SIZE, self.HEADER_SIZE,
                        CACHE_LINE_SIZE - self.HEADER_SIZE))
        self.size = size
        super(State, self).__init__(**kwargs)

    def _get_size(self):
        return self.HEADER_SIZE + self.size

    def _get_type(self):
        return ('B', 'state {}'.format(self.size + self.HEADER_SIZE))

    @contextmanager
    def enter(self, value):
        encoded = value.encode('utf-8')
        le = len(encoded)
        tail = le - self.size
        if tail < 0:
            encoded += b'\x00'
            le += 1
        elif tail > 0:
            encoded = encoded[:self.size]
        le += 8
        chunk = _timestr.pack(int(time.time()*1000)) + encoded
        self._memoryview[0:le] = chunk

    @contextmanager
    def context(self, value):
        self.enter(value)
        yield self
        self._memoryview[0:8] = b'\x00\x00\x00\x00\x00\x00\x00\x00'

    def exit(self):
        self._memoryview[0:8] = b'\x00\x00\x00\x00\x00\x00\x00\x00'

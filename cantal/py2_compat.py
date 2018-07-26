import sys
import struct

if sys.version_info >= (3, 4, 0):
    MemoryView = memoryview
else:

    import ctypes

    TYPEMAP = {
        'B': ctypes.c_char,
        'q': ctypes.c_long,
        'Q': ctypes.c_ulonglong,
        'd': ctypes.c_double,
    }

    class _MemoryView(object):
        __slots__ = ('_mmap', '_slice')

        def __init__(self, _mmap, _slice=None):
            self._mmap = _mmap
            self._slice = _slice

        def __getitem__(self, item):
            assert isinstance(item, slice), "Only slicing is supported"
            assert self._slice is None, "Only single level of slicing required"
            return MemoryView(self._mmap, item)

        def cast(self, typ):
            slc = self._slice
            if slc is None:
                slc = slice(None)  # full slice
            start, stop, step = slc.indices(len(self._mmap))
            assert step == 1, 'Only step 1 supported'
            bytesize = struct.calcsize(typ)
            _typ = TYPEMAP[typ] * ((stop - start) // bytesize)
            return _typ.from_buffer(self._mmap, start)

    MemoryView = _MemoryView

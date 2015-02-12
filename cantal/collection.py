import os
import mmap
import json
import atexit
from itertools import groupby


class DuplicateValueException(RuntimeError):
    """Raised when all parameters to value are duplicated"""


def _get_size(pair):
    return pair[1]._get_size()


def _counter_order(pair):
    return (pair[1]._get_size(), pair[0])


class Collection(object):
    """A collection of statistics parameters

    It's just a singleton, which is hold in this module, but we use it
    as a regular class for unittests
    """

    def __init__(self):
        self._all_values = {}

    def add(self, dimensions, value):
        name = json.dumps(dimensions)
        if name in self._all_values:
            raise DuplicateValueException(
                "Counter {} is already defined".format(name))
        self._all_values[name] = value

    def start(self, basepath):
        values = list(self._all_values.items())
        del self._all_values

        values.sort(key=_counter_order)

        offset = 0
        scheme = []
        offsets = {}
        for size, pairs in groupby(values, key=_get_size):
            if size & (size-1) == 0:  # power of two; let's optimize
                if offset % size:
                    pad = size - offset % size
                    offset += pad
                    scheme.append('pad {}'.format(pad))
            elif size % 8 == 0:
                # unless value is small or
                # it's size is crappy we must align to 8
                if offset % 8:
                    pad = size - offset % 8
                    offset += pad
                    scheme.append('pad {}'.format(pad))
            for name, value in pairs:
                offsets[value] = offset
                offset += size
                _, typ = value._get_type()
                scheme.append(typ + ': ' + name)

        size = offset

        path = basepath + '.values'
        tmppath = basepath + '.tmp'
        metapath = basepath + '.meta'

        if os.path.exists(metapath):
            os.unlink(metapath)
        if os.path.exists(path):
            os.unlink(path)
        if os.path.exists(tmppath):
            os.unlink(tmppath)

        with open(tmppath, 'w+b') as f:
            # We could use truncate, but it doesn't enlarge file in
            # cross-platform fasion. Fortunately our data is small and usually
            # in RAM anyway
            f.write(b'\x00' * offset)
            f.flush()
            mem = memoryview(mmap.mmap(f.fileno(), offset))

        os.rename(tmppath, path)

        with open(tmppath, 'wt') as f:
            f.write('\n'.join(scheme))

        os.rename(tmppath, metapath)

        for value, offset in offsets.items():
            vtype, _ = value._get_type()
            size = value._get_size()
            value._memoryview = mem[offset:offset+size].cast(vtype)

        return ActiveCollection(basepath)


class ActiveCollection(object):

    def __init__(self, path):
        self._path = path

    def add(self, dimensions, value):
        raise RuntimeError(
            "Counters can't be added after collection.start()")

    def start(self, path):
        raise RuntimeError("The start() method already called")

    def close(self):
        os.unlink(self._path + '.meta')
        os.unlink(self._path + '.values')


global_collection = Collection()


def start(path=None):
    global global_collection
    if path is None:
        path = os.environ.pop("CANTAL_PATH", None)
    if path is None:
        if 'XDG_RUNTIME_DIR' in os.environ:
            path = '{}/cantal.{}'.format(
                os.path.join(os.environ['XDG_RUNTIME_DIR']),
                os.getpid())
        else:
            path = '/tmp/cantal.{}.{}'.format(
                os.getuid(),
                os.getpid())

    global_collection = global_collection.start(path)
    atexit.register(global_collection.close)

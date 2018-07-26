from typing import Union
from ctypes import c_char, c_long, c_ulonglong, c_double
import mmap


class MemoryView:
    def __init__(self, _mmap: mmap.mmap, _slice: slice) -> None: pass
    def __getitem__(self, item: slice) -> MemoryView: pass
    def cast(self, typ: str) -> Union[c_char, c_long, c_ulonglong, c_double]:
        pass

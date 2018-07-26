from typing import Tuple

from .core import _Value


class Float(_Value):
    __slots__ = ()

    def incr(self, value: float = 1) -> None: pass
    def _get_size(self) -> int: pass
    def _get_type(self) -> Tuple[str, str]: pass
    def set(self, value: float) -> None: pass
    def __setitem__(self, key: int, value: float) -> None: pass


class Integer(_Value):
    def _get_size(self) -> int: pass
    def _get_type(self) -> Tuple[str, str]: pass
    def set(self, value: int) -> None: pass
    def get(self) -> int: pass
    def incr(self, value:int = 1) -> None: pass
    def decr(self, value:int = 1) -> None: pass
    def __setitem__(self, key: int, value: int) -> None: pass

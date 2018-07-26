from .core import _Value
from typing import Tuple


class Counter(_Value):
    def __iadd__(self, value: int) -> int: pass
    def incr(self, value:int=1) -> None: pass
    def _get_size(self) -> int: pass
    def _get_type(self) -> Tuple[str, str]: pass

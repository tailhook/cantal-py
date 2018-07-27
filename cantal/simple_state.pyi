from typing import Dict, Tuple, Iterator
from contextlib import contextmanager

from .core import _Value


class State(_Value):
    def __init__(self, size: int, **kwargs: str) -> None:
        pass

    def _get_size(self) -> int: pass
    def _get_type(self) -> Tuple[str, str]: pass

    def enter(self, value:str) -> None: pass

    @contextmanager
    def context(self, value:str) -> Iterator[State]:
        pass

    def exit(self) -> None: pass

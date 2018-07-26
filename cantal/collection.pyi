from typing import Dict, Union
from .core import _Value


global_collection: Union[Collection, ActiveCollection]


class DuplicateValueException(RuntimeError):
    pass


class Collection(object):
    def __init__(self) -> None: pass
    def add(self, dimensions: Dict[str, str], value: _Value) -> None: pass
    def start(self, basepath: str) -> ActiveCollection: pass


class ActiveCollection(object):

    def __init__(self, path: str) -> None: pass

    def add(self, dimensions: Dict[str, str], value: _Value) -> None:
        pass

    def start(self, path: str) -> None: pass

    def close(self) -> None: pass


def start() -> None:
    pass

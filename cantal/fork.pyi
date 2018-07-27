from contextlib import contextmanager
from typing import Dict, Iterator


class Branch(object):

    def __init__(self,
        suffix: str, state:str, parent: Fork, **kwargs: str,
    ) -> None:
        pass

    def enter(self) -> None: pass


class Fork(object):

    def __init__(self,
        branches: Iterator[str], state: str, **kwargs: str,
    ) -> None:
        pass

    @contextmanager
    def context(self) -> Iterator[None]: pass

    def enter_branch(self, branch: str) -> None: pass

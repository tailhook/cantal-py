import abc
from typing import Dict


class _Value(object):

    def __init__(self, **kwargs: Dict[str, str]) -> None: pass

    @abc.abstractmethod
    def _get_size(self) -> int:
        pass

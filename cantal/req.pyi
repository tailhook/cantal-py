from contextlib import contextmanager
from typing import Dict, Tuple, Iterator


class RequestTracker(object):
    def __init__(self, group_name: str, **kwargs: Dict[str, str]) -> None:
        pass

    @contextmanager
    def request(self) -> Iterator[None]:
        pass

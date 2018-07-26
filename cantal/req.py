import time
from contextlib import contextmanager

from .counters import Counter
from .levels import Integer


class RequestTracker(object):
    def __init__(self, group_name, **kwargs):
        self.requests = Counter(group=group_name,
                                metric="requests", **kwargs)
        self.duration = Counter(group=group_name,
                                metric="total_duration", **kwargs)
        self.errors = Counter(group=group_name,
                              metric="errors", **kwargs)
        self.in_progress = Integer(group=group_name,
                                   metric="in_progress", **kwargs)

    @contextmanager
    def request(self):
        start = time.time()
        self.in_progress.incr()
        try:
            yield
        except Exception:
            self.errors.incr()
            raise
        finally:
            dur = time.time() - start
            self.in_progress.decr()
            self.requests.incr()
            self.duration.incr(int(dur * 1000))

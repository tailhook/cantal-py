from cantal import Collection, Counter, Integer, State
from unittest import TestCase


class NoCrashWithoutStart(TestCase):

    def setUp(self):
        self.collection = Collection()

    def test_counter(self):
        cnt = Counter(collection=self.collection, hello="world")
        cnt.incr(1)

    def test_integer(self):
        val = Integer(collection=self.collection, hello="world")
        val.incr(1)

    def test_state(self):
        val = State(collection=self.collection, hello="world")
        val.enter('Nice work!')
        val.exit()

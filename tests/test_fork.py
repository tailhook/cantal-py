from .test_stats import TestBase


class TestFork(TestBase):
    maxDiff = 1000

    def test_fork(self):
        state = self.fork(["working", "sleeping"], state="job")
        self.start()
        self.assertMeta("""
            counter 8: {"metric": "count", "state": "job.sleeping"}
            counter 8: {"metric": "count", "state": "job.working"}
            counter 8: {"metric": "duration", "state": "job.sleeping"}
            counter 8: {"metric": "duration", "state": "job.working"}
            counter 8: {"metric": "err", "state": "job"}
            pad 24
            state 64: {"state": "job"}
        """)
        self.assertRead(b'\x00'*8, 0, 8)
        with state.context():
            self.assertRead(b'_' + b'\x00'*55, 32+32+8)
            state.working.enter()
            self.assertRead(b'working' + b'\x00'*49, 32+32+8)
            state.sleeping.enter()
            self.assertRead(b'sleeping' + b'\x00'*48, 32+32+8)
            state.working.enter()
            self.assertRead(b'working' + b'\x00'*49, 32+32+8)
            state.working.enter()
            self.assertRead(b'working' + b'\x00'*49, 32+32+8)
        self.assertRead(b'\x01\x00\x00\x00\x00\x00\x00\x00', 0, 8)
        self.assertRead(b'\x03\x00\x00\x00\x00\x00\x00\x00', 8, 8)

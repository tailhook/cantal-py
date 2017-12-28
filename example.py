import os
import time
import cantal

wakeups = cantal.Counter(group='main_loop', metric='wakeups')
sleep_time = cantal.Float(group='main_loop', metric='last_sleep')
num_fds = cantal.Integer(group='main_loop', metric='num_fds')
state = cantal.State(group='main_loop', metric='main_state')


def main():
    cantal.start()
    while True:

        with state.context('sleeping'):
            start = time.time()
            time.sleep(0.2)
            wakeups.incr(1)
            sleep_time.set(time.time() - start)

        with state.context('checking_fds'):
            num_fds.set(len(os.listdir('/proc/self/fd')))
            time.sleep(0.1)  # just so we notice state


if __name__ == '__main__':
    main()

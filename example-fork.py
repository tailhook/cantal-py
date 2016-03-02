import os
import time, random
import cantal

track_state = cantal.Fork(['app', 'redis', 'sql'], state="example-fork.main")

def main():
    cantal.start()
    while True:

       with track_state.context():

           track_state.redis.enter()
           # rdata = redis.get('something')
           time.sleep(0.002*random.random())

           track_state.sql.enter()
           # sdata = postgres.query("SELECT ...")
           time.sleep(0.005 + random.random()*0.01)

           track_state.app.enter()
           # render_template(..)
           time.sleep(0.05 * random.random())

       time.sleep(0.1)


if __name__ == '__main__':
    main()

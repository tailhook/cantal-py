.. highlight:: python
.. default-role:: python


========
Tutorial
========


Cantal is a metrics collection system. It integrates with your application
by providing some metrics. Here is a bare (but fully working) example:


.. code-block:: python
    :emphasize-lines: 3, 6, 10
    :linenos:

    import cantal

    ticks = cantal.Counter(name='ticks')

    def main():
        cantal.start()

        while True:
            sleep(0.1)
            ticks.incr(1)

    if __name__ == '__main__':
        main

The key things:

1. You declare metrics
2. Then you call ``start()``
3. Afterwards you may freely adjust values of the metrics

Cantal only works if it has ``CANTAL_PATH`` provided in the environment, in
other case all counters are just no op.

Rules of thumb:

1. Create all metrics at module import time
2. Import all modules before calling ``main()`` or whatever init function
2. Writing metric is very cheap, so you don't need to aggregate them in user
   code
3. Creating metrics dynamically (after ``start()``) is not supported, but you
   can create metrics in a loop or similar


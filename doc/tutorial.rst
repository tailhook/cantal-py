.. highlight:: python
.. default-domain:: python


========
Tutorial
========


Cantal is a metrics collection system. It integrates with your application
by providing some metrics. Here is a bare (but fully working) example:


.. code-block:: python
    :emphasize-lines: 3, 6, 10
    :linenos:

    import cantal

    ticks = cantal.Counter(group="main_loop", metric="ticks")

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

Rules of thumb:

1. Create all metrics at module import time
2. Import all modules before calling ``main()`` or whatever init function
3. Writing metric is very cheap, so you don't need to aggregate them in user
   code
4. Creating metrics dynamically (after ``start()``) is not supported, but you
   can create metrics in a loop or similar

See :ref:`metrics` for more info.


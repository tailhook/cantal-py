=========
Cantal-Py
=========

:Status: Beta
:Documentation: https://cantal-py.readthedocs.io/
:Parent Project: https://github.com/tailhook/cantal

Cantal is an expermimental heartbeating, monitoring and statistics solution.
This is a python library for sending statistics data to cantal.

Example
=======

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


License
=======

Licensed under either of

* Apache License, Version 2.0,
  (./LICENSE-APACHE or http://www.apache.org/licenses/LICENSE-2.0)
* MIT license (./LICENSE-MIT or http://opensource.org/licenses/MIT)
  at your option.

Contribution
------------

Unless you explicitly state otherwise, any contribution intentionally
submitted for inclusion in the work by you, as defined in the Apache-2.0
license, shall be dual licensed as above, without any additional terms or
conditions.


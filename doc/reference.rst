.. highlight:: python
.. default-domain:: py

=========
Reference
=========


Basic Metrics
=============

All metrics have a constructor which receives arbitrary keyword arguments.
The values must be strings, and they are arbitrary key-value pairs to identify
the metric in monitoring. Multiple keyword pairs are used to group metrics
over multiple processes by different dimensions.

.. class:: Counter

   The 64bit integer counter. Counter always grows. (However, it may wrap
   on overflow). In monitoring it's usually used for displaying per-second
   rates of some values. For example:

   * Count of requests (=> requests per second)
   * Duration of all requests (=> average request latency)
   * Number of accepted connections
   * Number of connection attempts to a DB

   .. method:: incr(value=1)

      Increment the counter.

      .. hint:: The operation is very cheap, so you don't need to aggregate
         multiple increments on your own.

.. class:: Integer

   The 64bit signed integer value. It represents something that is useful
   on it's own (unlike :obj:`Counter`), without getting derivation of.
   Examples:

   * Number of requests being processed
   * Size of queue
   * Number of connections in the connection pool (total, free, used)

   .. method:: set(value)

      Update value of the metric

   .. method:: incr(value=1)

      Increment value of metric

      .. hint:: Updating the value is very cheap. You don't have to duplicate
         the value somewhere. For example, you may increment the counter on
         the start of the request and decrement afterwards. You may use
         `get()` method to get the value if you need to use it for applciation
         needs.

   .. method:: decr(value=1)

      Decrement value of metric. Equivalent of ``incr(-value)``

   .. method:: get()

      Get value last written (or adjusted according to the counters)

.. class:: Float

   This is similar to :obj:`Integer` but represents floating point value.

   .. method:: set(value)

      Update value of the metric

.. class:: State

   The class represents some internal state of the application. This stores
   some string state value and timestamp when it was last changed.

   :param size: maximum size of the state data. Note that this number of bytes
       is reserved, so it shouldn't be too big. Truncation of data is perfectly
       okay. This should be `64*n - 8` for best performance.

   Usege examples:

   * Which resource the process is currently waits for
   * Currently executing SQL query
   * The start/process/shutting down application lifecycle

   See :obj:`Fork` for more comprehensive state handling built on top of
   :obj:`State`.


   .. method:: context(value)

      A context manager which sets state name to ``value`` and clears state
      on exit.

   .. method:: enter(value)

      Enter the state with ``value``. This also marks the timestamp when
      state is started. Better use context manager for most cases

   .. method:: exit()

      Clear the state


Compound Utilities
==================

.. class:: RequestTracker

   The class embeds multiple counters so it's easy to track both incoming
   and outgoing requests.

   Example:

   .. code-block:: python
        :emphasize-lines: 5,7,10

        http = RequestTracker('http')
        sql = RequestTracker('http.sql')

        def application(environ, start_response):
            with http.request():
                do_something()
                with sql.request():
                    value = sql_query()
                if value == None:
                    http.errors.incr()
                    start_response('500 Internal Server Error', [])
                    return [b"Error"]
                do_something_else()
                start_response('200 OK', [])
                return [value.encode('utf-8')]

   The counter group embeds the following primitive metrics:

    * ``requests`` -- the :class:`Counter` of requests
    * ``total_duration`` (aliased as ``duration`` in python attribute)
      -- :class:`Counter` for total duration of all requests (in milliseconds),
      this is later used to calculate average response time
    * ``errors`` -- :class:`Counter` for number of errors
    * ``in_progress`` -- :class:`Integer` of current requests in progress

   You are free to use ``req_tracker.errors.incr()`` for all your custom
   errors which are not exceptions (i.e. non-200 HTTP response). Exceptions
   are tracked automatically.

   This works for both synchronous and asynchronous processes. In synchonous
   ones the ``in_progress`` is likely to be ``0`` or ``1`` (but when summing
   over cluster you'll get some bigger values).

   .. method:: request()

      Returns context manager that tracks requests.

      The ``requests`` and ``total_duration`` are incremented *after* request.

      The ``errors`` is automatically incremented if exception happened
      inside the context manager.


.. class:: Fork

   The class to handle multiple states of the application. In the frontend
   it allows to draw chart of where application spends most of the time, and
   which states are reached more often.

   Example::

       track_request = Fork(['app', 'redis', 'sql'],
                            state="myapp.request_processing")

       def process_request(req):
           with track_request.context():

               track_request.redis.enter()
               rdata = redis.get('something')

               track_request.sql.enter()
               sdata = postgres.query("SELECT ...")

               track_request.app.enter()
               return render_template(rdata, sdata)


   .. method:: context()

      Enter the fork root state. The default state is named `_` (single
      underscore). It's meant to enter some branch soon afterwards.


.. class:: Branch

   Represents branch of a :obj:`Fork`. You shouldn't create it on it's own
   but use the attribute of a fork.

   .. method:: enter()

      Enter the branch as part of this :obj:`Fork`.


Collection Classes
==================

Usually you don't need to instantiate collection classes. They are handled
internally.

.. class:: Collection

   A collection of metrics when it's being populated with metrics.

.. class:: ActiveCollection

   A collection of metrics when tracks metrics and can't have more metrics
   added.


Exceptions
==========

.. class:: DuplicateValueException

   Raised when you define two metrics with all the same key-value pairs.


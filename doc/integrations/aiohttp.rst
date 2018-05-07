Aiohttp
=======


Incoming(Server) Connections
----------------------------

Here is an example how to track number of incoming connections in HTTP server:

.. code-block:: python


    CONNECTIONS = cantal.Integer(group='http.server', metric='connections')

    def adopt_aiohttp_server(Server):
       conn_made = Server.connection_made
       conn_lost = Server.connection_lost

       def connection_made(*a, **kw):
           CONNECTIONS.incr()
           return conn_made(*a, **kw)

       def connection_lost(*a, **kw):
           CONNECTIONS.decr()
           return conn_lost(*a, **kw)
       Server.connection_made = connection_made
       Server.connection_lost = connection_lost

    from aiohttp.web_server import Server
    adopt_aiohttp_server(Server)

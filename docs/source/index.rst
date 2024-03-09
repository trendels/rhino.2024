rhino
=====

*rhino* is a microframework for building RESTful web services.


Getting Started
---------------

Here are the minimal steps needed to get you to a running "hello world!" example.

First create a new virtual environment, and install *rhino* and *gunicorn* (a
WSGI server we will use to run our application).

.. code-block:: shell

   $ python3 -m venv venv
   $ source venv/bin/activate
   $ pip install rhino gunicorn

Then, create a file named ``helloworld.py`` with this content:

.. literalinclude:: ../examples/helloworld.py
   :language: python

Start the application like this:

.. code-block:: shell

   $ gunicorn --bind=127.0.0.1:9000 helloworld:app

Then visit http://127.0.0.1:9000/ in your web browser, and you should see the
text "Hello, world!".


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   api.rst

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

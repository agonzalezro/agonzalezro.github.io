Graphite, Carbon and Diamond
============================

:date: 2012-11-6 19:30
:tags: graphite, carbon, diamond, monitoring, python, pygrunn

Two days ago was my, sadly, last PyGrunn monthly meeting. Thanks to `Bram`_ now
we know a little bit more about how to monitoring with Python applications.

Below you will find the notes that I take to the people that couldn't assist to
the talk. But they are only that, some notes, don't expect to find a really cool
story on them. I am pretty sure that `the original slides made by Bram`_ will help
you.

.. _bram: http://www.linkedin.com/profile/view?id=17961952&locale=en_US&trk=tyah
.. _`the original slides made by Bram`: /graphite.slides/graphite.html


Why graphite?
-------------

* Dev friendly
* Ops friendly
* Growth friendly: very scalable

Some important companies are using it: Instragram, Etsy, Github, `Kalooga
<http://www.kalooga.com>`_ (this is the company where Bram is working :).

It's a project created by `Orbitz.com <orbitz.com>`_.


Ecosystem
---------

Graphite
    The tool that makes the graphs.
Carbon
    Colects the statistics.
Whisper
    Metrics `RRD (Round Robin database)`.
Diamond
    It's the metrics collector, they are others: CollectD, Munin, Ganglia... Of
    course, you can develop yours.


How do you gate the data in?
----------------------------

#. Create an HTTP connection to the server.
#. Each line will be a data point.

If you want namespaces you can always use dots `.`. Example: `pygrunn.load
[load] [now]`.


Improvements
------------

Why don't use statsd? It's a layer for Graphite that you can use to keep your
application running and send the data to statsd. If it can write it ok, if not,
you have a problem.

The original implementation of StatsD is in Node.js but there are another
projects that do it with C (StatsD-c) or python (Bucky) or [write your prefered
language here].


Uses
----

* Open a `dev` file and write directly to it.
* Open HTTP connection.
* Use a statsd decorator.
* ...


Plots
-----

You can plot data with:

* JSON
* CSV
* HTML
* XML
* ...


API
---

You can do funny things as:

* Check the registered users over past day in json data
* Keep track of your 404 errors
* ...


Where is the data store?
------------------------

They are stored in files, in case that you run out of space this data will be
stored on the Carbon cache until something happen to it.a


Functions
---------

You can filter results, for example mostDeviant (take a look to the slides to
see the screenshots that show the use).


What's also nice?
-----------------

Sentry
    Error caching middleware that you can run with your WSGI application to
    check the Exceptions and the stacktraces.

Shinken
    It's also written in python and it's compatible with Nagios. It could be a
    good complement to Graphite to show some alerts when the thing are really
    wrong.

New Relic
    It's a Web Application Performance Management (`APM (Application
    Performance Management`).

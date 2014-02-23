date: 2013-02-12 00:30
tags: python, migration, python3k

TechTalk: from python 2.x to python 3
=====================================

Introduction
------------

This are some notes that I took while the talk that I saw today, the
original title of the talk that I had the chance to see today was:
"Switch to Python 3... Now... Inmediately" by the [professor Russel
Winder](http://www.russel.org.uk).

More or less all that you will find here is a transaction, just ordered
in my style and perhaps with some notes by myself.

Python 2.x remains being the default python. Too many people and
organizations are afraid of the change.

Python software foundation should declare python 3 the default python
immediately.

### Problems

-   some big companies are telling people to don't use it.
-   some crucial projects are not using Python 3 yet.

### Companies and people

-   from the point of view of Russel, the problem are those companies
    that doesn't want to migrate, and not the fact that the code needs
    to be migrate.
-   at least they should have version 2 and 3 compatible on the
    codebase.

### Migration

-   `2to3` tool is not useful at all. Just one shot transform tool.
-   the manual the better? From my POV (Álex) you can never let a
    machine this kind of work and it usually will be a biblical
    proportion job for large codebases. And more important... usually
    without tests :D

Justifications
--------------

Python 2 is a dead end and python 3 is the developing future.

This piece of code is compatible with both versions, why don't use them?

````` python
print(x)
exec(x)
`````

Problem: `print(x)` support multiple parameter in python 3, so, let's
import the function from future to have the same behaviour in python
2.x:

````` python
from __future__ import print_function
`````

Let's make it bigger:

````` python
from __future__ import (
    division,
    absolute_import,
    print_function,
    unicode_literals
)
`````

With this we will avoid problems with floats on divisions, add . to the
imports, import the python3 version of print and work always with
unicode.

Another problem is the list-comprehensions which will change a little
bit, instead create list, they will create sets.

### Some other problems

python 2 is strict, but python 3 is kinda lazy.

````` python
map(lambda x: x * x, filter(lambda x: x % 10 == 0, range(100))
`````

Will produce an iterator in python 3, in python 2 is a data structure.

This is one of the biggest issues into the migration, other functions
with same problems will be, for example: `items`, `keys`, `values`,
`iteritems`, `iterkeys` & `itervalues` which in python 3 will become:
`items`, `keys` & `values`.

If you want a data structure instead a iterator, you should make it
manually:

````` python
range(10)  # python 2.x
tuple(range(10)  # python 3
`````

### Concurrency

At least IronPython and Jython do not have a
[GIL](http://wiki.python.org/moin/GlobalInterpreterLock) as CPython and
PyPy do.

There is an experiment to mode GIL out of PyPy.

Actors
:   communicate processes with messages.

Dataflow
:   operators connected by channels with activity triggered by arrival
    of data on the channels.

CSP
:   we have [PyCSP](http://code.google.com/p/pycsp/) and
    [PythonCSP](https://github.com/python-concurrency/python-csp).

### Data parallelism

Transform a sequence to another sequence where all individual actions
happen at the same time. Python has not a lot of utilities for that,
since Go or D do.

### Futures are the future

concurrent.futures
:   python 3.2 package to abstract over threads and processes to give an
    asynchronous function call and future system.

Under challengue
----------------

-   Go is taking over from Python, because it's native and it has a
    solid concurrency models (CSP).
-   D is on the market too.
-   Native programs are almost always quicker than python.

Funny points
------------

-   One rule of the guy is to use one month a year just `ed` no `vim` or
    `emacs` rubbish.
-   C has a rubbish syntax in comparison with Python. You will touch
    your head if you check some C++ code: why!?

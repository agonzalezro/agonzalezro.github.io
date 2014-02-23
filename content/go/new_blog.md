date: 2014-02-23
tags: go, golang, polo, pelican, static

Hi all from my new blog engine!
===============================

After a really, really long time I am finally updating my old blog. Time ago I
tried to update it but I've realised that a lot of JS of the site was
completely broken & instead spend some time fixing it I've decided to start it
from scratch with my own blog site generator:
[Polo](http://github.com/agonzalezro/polo).

I know that from a point of view of a software engineer, start something from
scratch when you have something that was already working, perhaps is not the
best of the ideas, but ehy! My blog, my rules :) And it's kinda tradition that
I develop a blog CMS every time that I learn a new language, with the only
difference that this time it's going to be an static one.

Past
----

Why I've started my own? I was thinking a lot about this question and I only
found 2 points:

- As I said, I wanted to learn some Golang development, so, I made it with Go.
- I think that the template inheritance in [Pelican](http://getpelican.com) (my
  old site generator, and a really really good piece of software) were a little
  over complex for my needs.

Present
-------

As I said, my own blog generator was Pelican so I tried to keep Polo as much
compatible as possible with it:

- the default slugs are the same that Pelican generates to avoid 404s after the
  migration.
- the markdown metadata is exactly the same too.

Future
------

There is few capabilities that I would like to implement ASAP:

- pagination.
- generate html indexes for the tags.
- a proper design that doesn't make it look extremely awful.
- add the templates as part of the binary package.

The generator is in a really early state which means that it can be some
errors. I was moving all my old posts too and I didn't manually try all of
them, so, it's possible that the content on some of them -specially images- is
broken too. Please, contact me if you find something.

I am open to suggestions, feel free of [create an
issue](https://github.com/agonzalezro/polo/issues) and take a look to the ones
that are already open. Or just contact me on twitter:
[@agonzalezro](http://twitter.com/agonzalezro).

date: 2014-08-30
tags: polo, server, go

polo has his own static server
==============================

I've added a small but useful functionality to the [polo static site
generator](http://github.com/agonzalezro/polo) that I am using here. Now, after
you generate your content from your files, you are going to be able to run a
small http server to see the content easily.

This post is more to show you how to use polo and the new functionality than
anything else.

Let's imagine that you have your markdown contents on `~/blog`, if you don't
have any example, you can [use my blog
markdowns](http://github.com/agonzalezro/agonzalezro.github.io).

First thing that you need to do is install polo:

    $ go install github.com/agonzalezro/polo

Second & final thing:

    $ polo -daemon

And now, you are going to be able to see your rendered content on
http://localhost:8080. If you want to configure the port, just use the `-port`
flag.

Easy peasy. So, use it!

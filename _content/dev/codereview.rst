codereview from the POV of a noob
=================================

:date: 2013-01-29 19:16
:tags: codereview, python

Hi g(irl|uy)s! I would like to start with a disclaimer:

*I am not (and I don't pretend to be) a craftmanship trooper (they like to be
called like that isn't?), senior engineer with more years of experience that
the technology has, guru, blablabla...*

*I just want to show my opinion about this process (which I really like!). But
more important that share my opinion, is to know what is yours, so, please,
comment!*

Today we had an interesting conversation at work about how we make and how we
should make our codereviews. My point of view is that there are three different
things to check:

1. **Code syntax.** It's a part that should be 100% automagically done. I
   usually work with python and I let this work to `Flake8`_ on vim, but it's
   always good to have a `git` hook.

2. **Reusability and maintainability.** I am afraid that this is the worst part
   to check, it's a manual process and it is really subjective. Some people can
   think that use `itertools` with 2 lambda functions is pretty clear and
   comprehensible, other people can think that this code is the result of a
   dirty mind developer.

3. **Functionality.** Automated test! All the test that you can, and of course,
   they worst the time that you will spent developing them. There are things
   that can not be easily tested but in that case let's suppose that you were
   clever enough to test them manually and in the case that is possible you
   can show it to anybody else (this really helps!).

As I said the point 1 can be (and should be) automated! It's really easy to do,
the same way that `Flake8`_ exists for python, I am pretty sure that you will
have one for your favourite language. It's really painful get back a pull
request just for some spaces that are not in place.

For the point 3, yep, let me jump the second for now. Unit testing, integration
testing, functional testing... whatever you want, but try to automate it. This
+ a CI server will make your live really "easy"!

And finally, about the second point. Each developer have their way to do the
things, but usually there are some points that can be fixed and sometimes
because we don't know, other times just because we are lazy but we post code
like this:

.. code-block:: python

    def f(a, b, c):
        if (a < 1 and
            request.user and
            request.user.is_authenticated() and request.user.has_perm('write')
        ):
            return HttpResponse(json.dumps('{authorized: True, 'a': a}))
        if a >= 1
            return HttpResponse(json.dumps('{authorized: True, 'a': a}))

This is just an example, but you should agree with me that it's really easy to
improve. This is what, in my opinion should be more checked in the reviews.

This was just an example (please, remember that :D), but could be improved with
something like this:

.. code-block:: python

    def proper_function_name(proper_variable_name):
        """This is an amazing function that will do just a thing.

        :param proper_variable_name: what I am?

        :returns: An HttpResponse object with the following JSON content:

            {'authorized': bool,
             'proper_variable_name: int}

        """
        is_authorized = (
            request.user and
            request.user.is_authenticated() and
            request.user.has_perm('write-resource')
        )

        return HttpResponse(
            json.dumps({
                'authorized': is_authorized,
                'proper_variable_name': proper_variable_name
            })
        )

Those were the improvements (again, remember that it's just an example):

1. Give a proper name to the function. Don't be afraid, everybody has
   autocompletion! :D
2. Give a proper name to the vars.
3. DOCUMENT! In this example, ready for Sphinx.
4. Simplify the if statements, actually, after take a look you made it
   dissapear.
5. One return.

So, what's your opinion? What do you think that is more important in a
codereview.

.. _flake8: http://pypi.python.org/pypi/flake8

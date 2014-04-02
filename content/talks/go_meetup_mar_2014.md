date: 2014-04-02
tags: go, best, practices

12 Go Best Practices
====================

Last Monday I had the chance to see [@francesc](https://twitter.com/francesc)
talking on the [Go London User
Group](http://www.meetup.com/Go-London-User-Group). His talk was about best
practices (and advices) when you are programming in Go.

Summarising it a little bit, I would say that some of the cases explained there
are things that you are going to finish doing even without knowing that you are
doing "best practices", but they are other examples that are incredible useful
and clever & I would love to assist to this conference few months ago.

At the beginning of the slides you are going to see an step-by-step refactoring
which could (and should) be applied to any other language out there. You will
realise of the major improvement on the readability of that piece of code.
Francesc said that the refactored version could possibly be a little bit
slower, but you will have in your power a piece of maintainable code.

If I need to choose one of the tricks showed, I would definitely go for the
type switch on the ([slide
#8](http://talks.golang.org/2013/bestpractices.slide#8)). Basically, you can
receive an interface as parameter and do a quick casting to whatever kind of
type that you want:

    ....
    switch x := v.(type) {  // where v is an interface{}
    case string:
        w.Write(int32(len(x)))
        w.Write([]byte(x))
    ...

I would say too that coming from a language like Python, it's really easy to be
temped to overuse that functionality :) What do you think?

Finally, [here you have the
slides](http://talks.golang.org/2013/bestpractices.slide#1) enjoy them as I
did!

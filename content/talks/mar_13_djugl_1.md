date: 2013-03-12 20:00
tags: djugl, march, django, python, metaclass

DJUGL: Advanced python trought Django: Metaclasses
==================================================

This talk was made by Peter Ingles, you can check his twitter here:
[@inglesp](http://twitter.com/inglesp).

What is write above is basically what he said, mixed with some of my
thoughts. The talk was really good, and even using metaclasses almost
daily (`forms.Form`) you don't feel the power of them until somebody
explain it to you (shame on me!).

In all the Peter example we was using Django 1.4.

The typical example as I said before is `forms.Form` from django.

For some reason, Peter was in love with the Ponies, so, he tried to
create some meta stable:

````` python
class A(models.Model):
    class Meta:
        app_label = 'ponies'
        abstract = True

class Stable(models.Models):
    class Meta:
        app_label = 'ponies'
    name = models.CharField()
    stable = models.ForeignKey(Stable)
`````

Create classes dinamycally:
---------------------------

````` python
def init(self, x):
    self.x =x

name = 'ExampleClass'
bases = (object, )
attrs = {
    '__init__': init
}
instance = type(name, bases, attrs)
`````

This is a pretty coold way to create classes at runtime.

type
----

I don't know you, but I was always using `type` just for the type
comparation, but never for create classes...

Some "strange" (puzzling) things about `type` is that `type` is a class
of type type:

````` python
type(type)
<type 'type'>
`````

And we can subclass `type`:

````` python
class A(type):
    pass
`````

Python 3
--------

The syntax to create a metaclass is sightly different:

````` python
class Form(metaclass=Formtype):
    ...
`````

Key takeaways
-------------

-   classes are factories for creating objects.
-   we can create classes dynamically at runtime.
-   metaclasses are factories for creating classes.
-   we can control what happens when we create classes

The slides
----------

You can find the interactive talk of Peter in his github account:
<http://github.com/inglesp/prescons>

Enjoy them!

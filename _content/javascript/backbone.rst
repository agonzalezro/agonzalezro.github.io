backbone.js + underscore: small intro
=====================================

Today, `Oleg <http://twitter.com/olegpidsadnyi/>`_ gave a talk about backbone at
`Paylogic <http://paylogic.nl/>`_. We were using it for a really fancy
application inside our backoffice, it was quite funny develop it and Oleg
decided to share the knowledge.

I used the techtalk to get some notes and, since I am not able to share this
piece of code, I will develop a small example for explain to you some of the
useful things that you can do with it. But, this is only a introductory post,
if you want advance stuff you should go to the `backbone official documentation
<http://backbonejs.org/>`_ & `underscore docs <http://underscorejs.org/>`_.

Backbone is really useful when you make complex GUIs on client side. You can
make your code like in desktop app using events to handle the actions. It's not
need to pass around instances of parents views, let's use only the events. You
have models too, that you can sync (or not) with the server.


Events
------

They are really useful to remove dependencies between elements. For example,
with jQuery if you change a element from another, the first one needs to know
about the second.

TODO: show poolsEditorView here

TODO: add a <ul><li> and check event change on the model. Start with several items and render them with underscore

- `delegateEvents`::

    var PoolEditView = backbone.View.extend({
        tagName: 'tr',
        ...
        events: {
            "dblclick": "edit",
            "click .edit": "edit"

- Binding "this": TODO


Models
------

With .set it will trigger the event change to know when the model had changed.
You can silent it.

Imagine, you are changing a name, if the name has changed on the collection,
the event will be raised, if not, it will not.


Underscore
----------

Work with collections, iterate, take optional context

In the middle of `<% %>` of `<%= %>` if you wanna print.


Extra ball
----------

Use `_.debounce` to don't call the functions thousands of time, example
drag&dropping an element it will be useful. Example when you are scrolling on
Google Maps.

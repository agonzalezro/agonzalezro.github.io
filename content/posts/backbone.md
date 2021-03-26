---
title: "backbone.js + underscore: small intro"
date: 2012-11-01
tags:
  - dev
  - backbone
  - underscore
  - javascript
---

Today, [Oleg](http://twitter.com/olegpidsadnyi/) gave a talk about
backbone at [Paylogic](http://paylogic.nl/). We were using it for a
really fancy application inside our backoffice, it was quite funny write
it and Oleg decided to share the knowledge.

I used the techtalk to take some notes and, since this piece of code
will have no sense out of our backoffice, I've written a small example
that you can find as a [gist](https://gist.github.com/3982819) on my
github. I will use it to explain to you some of the useful things that
you can do with backbone and underscore. Feel free to improve it.

This is only a introductory post, if you want advance stuff you should
go to the [backbone official documentation](http://backbonejs.org/) &
[underscore docs](http://underscorejs.org/).

Why?
----

Backbone is really useful when you make complex GUIs on client side. You
can make your code like in a desktop app using events to handle the
actions. It's not needed to pass around instances of parents views,
let's use only the events for that purpose, and let the child decide.

You have models too, that you can sync (or not) with the server.

Models
------

In backbone you can have local model and sync them with the server or
with local storage (not explained in this intro). In our example we
will:

1.  Create a collection to save our objects (type Item) in.
2.  Create the model Item.
3.  Create 2 object type Item inside this collection.
4.  Render them.

The 3 points can be made only with these lines of code. It's really
simple! (after know how to do it :p):

````` javascript
var Item = Backbone.Model.extend();

var Items = Backbone.Collection.extend({
  model: Item
});

var items = new Items();
items.add([{name: "foo"}, {name: "bar"}]);
`````

**Note**: Setting values in the objects With .set will trigger the event
    change. You can silent it in case that needed, but it's really
    useful, for example, to save it.

**Second note**: backbone is f\*\*\*ing clever! Imagine, you are changing a
    name, if the name has changed on the collection, the event will be raised,
    if not, it will not. This means that if you are editing, but finally
    you change your mind and you didn't made any change, the event will
    not be raised.

Events
------

They are really useful to remove dependencies between elements. For
example, with jQuery if you change a element from another, the first one
needs to know about the second. With backbone you can catch the event
with the child element and do whatever you want with it.

On the example of my [gist](https://gist.github.com/3982819) I show an
alert box with the name of the element. But you could, for example,
change it to an editable input.

This is the code of the example:

````` javascript
var ItemView = Backbone.View.extend({
  ...
  events: {
    "dblclick": "onDoubleClick"
  },
  ...
  onDoubleClick: function(ev) {
    var text = $.trim($(ev.target).text());
    alert("Hey! Why do you click on " + text + "?");
    console.log(ev); //Play with this :)
  }
});
`````

We are binding the `dblclick` event to the function `onDoubleClick`.
This function will receive the event, and the event will have the target
(in this case the `<li/>` that we are clicking.

Underscore
----------

It's really useful to Work with collections. In out example we are using
it to iterate over the items:

````` javascript
render: function() {
  _.each(this.items.models, function(item) {
    var itemview = new ItemView(item);
    $(this.el).append(itemview.render().el);
  }, this);
}
`````

If you read carefully this piece of code you will realize that we are
instantiating a new ItemView for each particular item, so it has its own
container element created on the fly, re-renderable each time when data
is updated and all events are delegated to this element.

The amazing thing that you can do with underscore is use templates (yes,
like jinja or django-templates, but in JS)! And we are doing it:

````` html
<script>
  var ItemView = Backbone.View.extend({
  ...
  template: _.template($("#item-template").html()),
  ...
  render: function() {
     $(this.el).html(this.template(this.item.toJSON()));
     return this;
  },
  ...
</script>
<script type="text/template" id="item-template">
  <%= name %>
</script>
`````

Extra ball
----------

Use `_.debounce` to don't call the functions thousands of times, example
drag&dropping an element it will be useful.

For example in our project we had to sort with drag and drop some
elements of a list, instead send this event in each drag movement, we
made it after 200s being quiet with:

````` javascript
onChange: _.debounce(function(ev) {
    this.pools.save();
}, 200),
`````

Please comment your thoughts about the post. We are all here to learn,
and it's really easy that I made some mistake explaining this.
Furhtermore, I know that my English is not really good, so, I will
apreciate constructive comments about it too :)

Enjoy it!

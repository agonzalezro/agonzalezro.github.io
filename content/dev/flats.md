date: 2014-09-03
tags: flats, london, rent, cartodb, scrape

How to find a flat in London with some help
===========================================

**EDIT:** I've added a little bit more of code to the gist to get the latitude
and longitude of the flat. This way the process of plotting them is more
accurate and incredibly easy. Thanks again [CartoDB](http://cartodb.com)!

At the end of this month I am going to move with a friend. This movement is
going to be something like the 7th one since I am living here (little bit less
than 2 years).

We are a little bit struggling trying to find a place so I decided that we need
a little bit of help:

Do you know [gumtree.com](http://gumtree.com)? That page is extremely good for
renting if you just take care of the content (aka adverts that users upload)
but it's extremely bad at searching: I couldn't filter to know when the flat would be available and I would be able to move in! Seriously?

To fix this I made a small scraper that is going to gather data from few pages
of the search results already filtered by gumtree, check the `QUERY_PARAMS` on
the [following gist](https://gist.github.com/agonzalezro/440e7bf41e77c284d735):

<script src="https://gist.github.com/agonzalezro/440e7bf41e77c284d735.js"></script>

In the other hand, the location needs to be a place close to King's Cross and
close to Mile End. Calculate commute times from one address to another one
doesn't look straightforward and easy to do, so, the best solution (in relation
dev_time/benefit) was showing all those flats in a map, and I made it thanks to
the help of CartoDB. This piece of software is amazing, basically the process
was:

1. drag&drop the CSV to your CartoDB account.
2. ~~click on the dropdown of the "location" row and then on "Georeference".~~
3. ~~in the popup that will be shown to you, you must select ""You have one or
   more columns with the address", and after that you will have a georeferenced
   list of points. The only bad point with this solution is that every month
   you just have 100 geoferential queries available for free :(~~

With that data you can create your own visualisation as I made here:

<iframe width='100%' height='520' frameborder='0' src='//alex.cartodb.com/viz/e3731a92-1c13-11e4-9a2d-0e10bcd91c2b/embed_map?title=true&description=true&search=false&shareable=true&cartodb_logo=true&layer_selector=false&legends=false&scrollwheel=true&fullscreen=true&sublayer_options=1&sql=&sw_lat=51.31344707827587&sw_lon=-0.5657958984375&ne_lat=51.67681321379405&ne_lon=0.318603515625' allowfullscreen webkitallowfullscreen mozallowfullscreen oallowfullscreen msallowfullscreen></iframe>

If you want to say something about this post or you want to offer me a nice
flat in London, feel free of use the comments or find me in twitter:
[@agonzalezro](http://twitter.com/agonzalezro)

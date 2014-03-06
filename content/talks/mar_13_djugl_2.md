date: 2013-03-12 20:30
tags: djugl, march, lanyrd, django, solr, celery, postgresql, redis, mongodb, mysql, varnish, haproxy, s3

DJUGL: Inside Lanyrd architecture
=================================

This talk was just amazing! Andrew Godwin
([@andrewgodwin](http://twitter.com/andrewgodwin) or http://areacode.org) gave
us talk about the internal architecture that they are using at
[lanyrd.com](http://lanyrd.com).

I would say 2 things:

-   Even before that talk I was using lanyrd, it's a really good service
    if you are organizing some kind of event.
-   At [GreenManGaming](http://greenmangaming.com) we are using a very
    similar infrastructure, which I think that means that when 2
    different companies without any relation are sharing so many layers,
    it should be good!

After this lines you will fine almost a C&P of the Andrew slide that you
can find here: https://speakerdeck.com/andrewgodwin/inside-lanyrds-architecture, but
there are some additional notes added by me.

The Origin Story
----------------

They launch in Aug'10 and after half an hour going down because the load
was too high

In Sep'11 they got some inversion that allows them to start with the
curren architecture.

The ecosystem that they need to take care of:

-   conferences
-   profile pages
-   emails
-   dashboard
-   coverage
-   topics
-   guides
-   mobile app
-   ...

And all this with just 6 technical guys! That know this:

-   You don't need a big team to write a complex product.
-   Communication is absolutely key.
-   Using Open Source well is also crucial.

What they run on
----------------

Almost all the site is written in django with some spices:

-   celery for the background tasks.
-   management cron jobs.
-   served by Gunicorn containers.

The main services that you can find on, are this:

### PostreSQL

-   main data store for everythin except upload master & replicated
    around 80G in 5 DBs each server run in RAID1

### Redis

-   Task queue transport for Celery and tweet listeners,
-   Contains user sets for every conference, user and topic.
-   Used for efficient narrowing of queries before Solr is hit,

### Solr

-   Stores conferences, users, sessions and more...
-   Very rich metada on each item.
-   Heavy use of sharding throughout the site.
-   They run Solr in master and replicated slave.

### Varnish

-   First point of call for all requests.
-   Caches most anonymous requests.
-   Enforces read-only mode if enabled.
-   One used an one hot spare at all times.

### HAProxy

-   Sits behind Varnish.
-   Distributes load amongst frontend servers.
-   Re-routes request during deploys.
-   They always have 2 up identically configured.

### S3

-   Stores all uploaded files from users.
-   Uploads forms post directly to S3.
-   Servers all static assets for the site (images, Css, JS).
-   Static assets are versioned with hash to help cache break.

What they have eliminated
-------------------------

It's a shame because I am reading it in several places, but it seems
that after the hype a lot of companies are eliminating MongoDB from
their backends.

### MongoDB

-   Stored analytics, logs and some other data.
-   Lack of schema meant some bad data persisted. poor complex query
    performance.

Nevertheless they think that it's a really useful tool for quick
prototyping.

### MySQL

-   Primary data store for things that where not stored in MongoDB.
-   Very poor complex query performance.
-   No advances field types.
-   Full database locks during schema changes.

The great move of 2012
----------------------

They move from EC2 to Softlayer basically because it's real hardware, if
something fail, just change it). From MySQL to PostgreSQL for the
reasons that he explained before.

### Why?

It seems that lanyrd has a very predictable traffic, they can know
months in advanced what is the expected load.

### How

Both moves required database downtime, couple of tables were really big,
any change on that table means around 20-30min of downtime.

1.  Replicate Solr and Redis across to new servers.
2.  Enter RO mode.
3.  Dump MySQL data.
4.  Convert MySQL dump into PostgreSQL dump.
5.  Load PostgresSQL dump.
6.  Re-point DNS, proxy request from old server.
7.  Exit RO mode.

After all this process they can say that they have been 1 hour and a
half in Read Only mode but without any downtime at all.

From their experience, the advantages of have a content site are that
the RO mode is completely viable. They logged out all the people from
the site and in the mean time Varnish was blocking all the POST request
& cache aggressively.

Always be deploying
-------------------

-   They deploy at least 5 times a day, if not 20.
-   Nearly all code goes into master or short-lived branches.
-   Anything released is feature flagged.
    -   simple named boolean toggles.
    -   settable by user, user tag, or conference.
    -   can change templates, view code, URLs, etc...

Just a quick note: if you had never used this feature you should try
something like [gargoyle](https://github.com/disqus/gargoyle). It's just
amazing to deploy some functionalities to just some of your users. I
don't know what they are using, but if it's not this, it should be
something similar.

Legacy code & decisions
-----------------------

-   It's fine to have some legacy code. It can speed thing ups.
-   A good chunk of their legacy code is gone, some remains (I would say
    like in all the big projects :D).
-   Big schema change get harder and harder.

Awareness (every ppl know what is going on) & always deployable (master
branch always shippable).

Small and nimble
----------------

-   Continue deployment and development style allows easy project
    changing
-   No long approval processes.

Fix it while you can
--------------------

-   The bigger you get, the harder a fix.
-   They moved to PostgreSQL just in time.
-   Big schema changes now take days of coding.

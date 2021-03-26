---
title: Draw (and more) your architecture with Neo4J
date: 2014-08-26
tags:
    - dev
    - neo4j
    - architecture
---

As some of you already know I work at [Green Man
Gaming](http://greenmangaming.com) (mainly at the
[playfire](http://playfire.com) project). We were planning to do some changes
in our architecture but it's extremely hard to have an idea of all our services
and DBs in just a piece of A4 paper. I was trying, trust me, but it was
impossible.

When I started with this task I did it with
[lucidchart](https://www.lucidchart.com), after it got so messy I moved to
[graphviz](http://www.graphviz.org/), but even with the usual good graphs that
I get from graphviz it was impossible to get something readable this time.

So, it happened! I remembered [this post](http://ivan.pedrazas.me/?p=280) made
by my friend Iván and I thought, why not?

Sadly, this post is not going to show any real data from GMG, but if you are
interested it's the moment to apply because we are hiring & we have the graphs
around all the whiteboard in the office! Just grab me an email.

What do I need?
---------------

Basically, you just need Neo4J. You can install it however you want, I've just
run a Docker container with it:

    docker run -d -p 7474:7474 tpires/neo4j

Now, if you access to your docker container at http://localhost:7474 (or using
the host from `boot2docker ip` if you run docker with boot2docker) you will see
the cypher shell which is one of the ways that you can use to interact with
your DB.

What I am going to draw?
------------------------

In my case, and for a POC, I've written the following entities:

- Person
- Technology
- Service

You could write some other entities as for example DBs.

The connections here are kinda clear: a person knows a technology which is
used to write a service that use a DB as backend, so, let's write it!

To create entities the syntax is as follow:

    CREATE (variable:Type{attributes})

And to create Relations (one of the ways):

    CREATE (variable1)-[:RELATION_NAME]->(variable2)

You will understand this better after we start creating our entities.

Create your engineers:

    CREATE
      (dev1:Person{name:"Alex"}),
      (dev2:Person{name:"Maria"}),
      (dev3:Person{name:"Pepe"}),

Before the : you can see that we have defined a variable to refer to this
just-created entities. All the nodes that we are creating here are of type
Person and each of them have a different name.

To create the relationships between Technology and Person, we define the
technology using the same method that we used to create the Person, but we add
the relationships:

    ...
      (python:Technology{name:"Python"}),
      (go:Technology{name:"Go"}),

      (dev1)-[:KNOWS]->(python),
      (dev1)-[:KNOWS]->(go),
      (dev2)-[:KNOWS]->(python),
      (dev3)-[:KNOWS]->(go),

And finally, we add our services:

    ...
      (service1:Service{name:"Service #1"}),
      (service2:Service{name:"Service #2"}),

      (service1)-[:CONNECTS]->(service2),
      (service1)-[:WRITTEN_WITH]->(go),
      (service2)-[:WRITTEN_WITH]->(python)


Querying for drawing
--------------------

Now, you can run all the script and we can see the result. For the first output
we are going just to show everything:

    MATCH (n)-[r]-() RETURN n, r

And you will get this!

![Cypher MATCH #1](/biz/neo4j_architecture/1.png)

So, what's the point of all this? Basically, that you can do queries that will
make the graph smaller for your needs. This example data that we have added is
quite small (just few nodes), in the real graph that I am working on we have
already few dozens. For example, imagine that you just want to see python
related information:

    MATCH (a)-[r]-() WHERE a.name="Python" RETURN a, r

![Cypher MATCH #2](/biz/neo4j_architecture/2.png)

Or you just want to see the people that can work with the Server #1

    MATCH (s:Service)-[r]-()-[r2:KNOWS]-(p:Person)
    WHERE s.name="Service #1" RETURN s, p

![Cypher MATCH #2](/biz/neo4j_architecture/3.png)

One more thing
--------------

For now, this project in my company is just a POC and I have not really clear
what attributes and entities I should draw to make this graph useful for the
present and for the future. If you have previous experiences or you want to
start a brainstorming, write on the comments or [find me at
twitter](http://twitter.com/agonzalezro).

Also, for now I am happy with just creating some screenshots from the data that
Cypher is showing to me, but it would be really nice to find a more
professional way of sharing this graphs. Cypher renders them with D3, so, I
don't fully understand why it doesn't support exporting them in a easy way.
Again, if you know something, just let me know.

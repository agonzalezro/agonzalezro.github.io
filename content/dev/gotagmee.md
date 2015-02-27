date: 2015-2-25
tags: neo4j, meetup.com, go

Graph your meetup.com group with Neo4J and some Go
==================================================

Last days I've been spending sometime in a small project for fun. Sadly I
couldn't do [anything for
production](https://twitter.com/agonzalezro/status/567823851791589376) so I
hacked [gotagmee](https://github.com/agonzalezro/gotagmee) which is a tiny
thingy that will created some goroutines to get all the members in a
[meetup.com](http://meetup.com) group with their interests and store them in a
Neo4J DB as `Member` or `Topic` entities with their respective relations.

I wrote this because I wanted to get the data,  but then I realised that this
piece of code is pretty neat (check the github repo for the original):

`````
membersChan := make(chan db.Member, 1)
go api.Members(membersChan)

db, _ := db.NewDB(*neo4jDB)

for m := range membersChan {
    db.Store(m)
}
`````

Basically I am creating a channel that is going to be used to receive the
members (1 by 1) whenever one of the subroutines scraping the API have one
ready. Perhaps there are better ways to do it, but I really like it :)

Let's go to the important part: **the data**. I've used the code to extract
the data of the meetup that I co-organize here at London, the [Go London User
Group](http://www.meetup.com/Go-London-User-Group) if you are interested, I
could share with you a dump. For this example I was just interested in the
users and topics, but if you want, change it to get more data:
http://www.meetup.com/meetup_api/docs/2/members/

We knew this already, but how many users do we have, easy peasy:

`````
neo4j-sh (?)$ match (n:Member) return count(n);
+----------+
| count(n) |
+----------+
| 671      |
+----------+
1 row
27 ms
`````

But perhaps the number of topic that our users follow is not (was not) as easy
to know:

`````
neo4j-sh (?)$ match (n:Topic) return count(n);
+----------+
| count(n) |
+----------+
| 1204     |
+----------+
1 row
30 ms
`````

I know that I am part of that meeting, what do I "like":

`````
neo4j-sh (?)$ match (n)-[]-(t) where n.name =~ "Alexandre.*" return count(t);
+----------+
| count(t) |
+----------+
| 17       |
+----------+
1 row
255 ms
`````

I think that I didn't impress anybody until here, but one of the ideas behind
graph DBs is easily find connections between entities, for example what do I
have in common with my friend [@ipedrazas](http://twitter.com/ipedrazas)? I
know that he likes beers as me, but I am talking about meetup.com relations,
let's see!

`````
neo4j-sh (?)$ match (n)-[]-(t:Topic)-[]-(m) where n.name =~ "Alexandre.*" and m.name =~ "Ivan Pedrazas" return t.name;
+----------------------+
| t.name               |
+----------------------+
| "Open Source"        |
| "Programming"        |
| "Mobile Development" |
| "golang"             |
+----------------------+
4 rows
91 ms
`````

Nice! But if you want to do it beautiful for your boss, you could as well use Cypher:

<style>img[alt=meetup_neo4j_example] { width: 75%; display: block; margin: auto; }</style>
![meetup_neo4j_example](static/dev/meetup_neo4j_example.png)

Now imagine that I want to target the interest of my group by the things that
they like more, which ones are those?

`````
neo4j-sh (?)$ match ()-[r]->(t:Topic) with t, count(r) as rel return t.name order by rel desc limit 10;
+------------------------+
| t.name                 |
+------------------------+
| "Programming"          |
| "Software Development" |
| "Open Source"          |
| "New Technology"       |
| "Technology"           |
| "Web Development"      |
| "Startup Businesses"   |
| "Big Data"             |
| "Cloud Computing"      |
| "Internet Startups"    |
+------------------------+
10 rows
99 ms
`````

They were kinda clear for this kind of geeky meetup :)

Hope that you enjoyed, and if you have any more question or queries for the data,
ping me here or at [@agonzalezro](http://twitter.com/agonzalezro).

---
title: Dockerizing Pligg with Fig
date: 2014-11-24
tags:
  - devops
  - docker
  - pligg
---

For a pet project I needed [Pligg](http://pligg.com/) which is kinda a social
network site in the style of the old-digg (with karma and this kind of things).

Installing a LAMP system is kinda boring stuff, so, for that and for the sake
of learning I decided to go with [Docker](https://www.docker.com/) &
[Fig](http://www.fig.sh/). Sadly or luckily, every time that I dockerize
something I find a lot of unexpected problems that slow me down, but... you
always learn something!

This post is to explain a little bit the process and the problems that I found
and how I solved them. It's not a how to, it's more a explanation of what I did
and perhaps you can provide a better solution on the comments.

What do I need?
---------------

The site is "simple" so the only required stuff will be a MySQL server and an
Apache2 server. You could run 2 Docker instances manually, or... use the magic
provided by Fig. This is the `fig.yml` file that explains my service:

    web:
      build: .
      links:
       - db
      volumes:
       - /var/log:/var/www/logs
      ports:
       - "80:80"
      environment:
       - MYSQL_PASSWORD
       - MY_BASE_URL
    db:
      image: mysql
      volumes:
       - /var/lib/mysql:/var/lib/mysql
      environment:
       - MYSQL_DATABASE=dbpligg
       - MYSQL_USER=pligguser
       - MYSQL_ROOT_PASSWORD
       - MYSQL_PASSWORD
      ports:
       - "3306:3306"

Basically I am saying that I will have 2 servers: "web" & "db" and specifying
their volumes, environment variables and exported ports.

### Problem?

First thing that we see here: `MY_BASE_URL` & `MYSQL_{,ROOT_}PASSWORD` don't
have any value, this is because Fig is going to got those values from the
current Docker host. I need them for specified some settings file that
originally were written in a normal file (difficult to change while deploying).

Also, `MY_BASE_URL` is a small/ugly trick. It seems that Pligg requires to know
the host were it's running to serve static assets as CSS or JS.

If you take a look to [my repo `config`
folder](https://github.com/agonzalezro/docker-pligg/tree/master/config) you
will see the slightly modified versions of two configuration files for Pligg
that are making use of this environment variables.

### More problems?

For running Pligg we need a minimal DB structure I've found 2 different ways of
creating this data in my data container, but none of them are optimal for me,
mainly because they require an extra step:

- I've created minimal SQL dump with some default values and on the `README.md`
  provide a quick way of ingest this data using the same container:

        $ docker exec dockerpligg_db_1 \
          mysql -u pligguser -p$MYSQL_PASSWORD dbpligg < "`cat pligg.sql`"

- Another way is going through all the installation process accessing to
  http://example.com/install

I think that perhaps creating a script that checks is the DB if empty and if it
is it uses the SQL to dump the DB back would be an option, but seems kinda
dangerous to automate that process in a live environment (anybody said delete
data by a mistaken dump?).

[@eloycoto](http://acalustra.com/) has recommended me to use inheritance of
containers. But I am not happy with that solution either: I would need two
`Dockerfile`s and possibly two `fig.yml` files as well or add some weird magic
to replace one container with the other after the installation.

### Third thing that I don't really like

After the first time that you run the installation you need to manually remove
the install path (this seems quite common in PHP apps?). I am doing that
running a `docker exec` to that container, but I would prefer to manually
remove it with the `Dockerfile`. Why I don't do so? Because if I remove that
folder I am forcing all the users of my configuration to use the dump SQL
method explained above and I don't give them any change.

So...
-----

I suspect that it's normal to have that kind of problems trying to "migrate" an
application that was never used before in a Docker container.

To be honest with Pligg, the only changes that I required were minimal, but I
don't know if that "install" part could be just removed with my own settings
file, I tried that and it was asking me to repeat values that were already set
in the `settings.php`.

I am not happy with the dump/install solution that I've found, but it works™!

I am sure that if you were using Docker or Fig before you will have plenty of
complaints about my article, let me know leaving a comment or just [tweet me
something](http://twitter.com/agonzalezro).

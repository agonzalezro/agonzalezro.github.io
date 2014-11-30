date: 2014-12-1
tags: docker, environment

How I prepared my Mac to make some Docker development
=====================================================

This post is about **how I did it!** not about a standard way or something like
that, if you use any other way I would be happy to hear it on the comments.

I usually use `boot2docker` on my machine to run container, but it looks like
it was misbehaving a little bit when I was trying to create the binary of my
dev branch with:

    $ make binary

Actually, it was just not creating it.

I could also create some cross-compiled binaries but that didn't work either.
It was a really weird situation because I couldn't find the path that it was
saying that it was creating. Not in my machine, not in my boot2docker VM
either. So, after some frustrating time I decided to go with vagrant.

What I wanted?
--------------

- My vim! I couldn't live without that.
- My ssh keys for github and similar without copying them to the vagrant box.

How I did it?
-------------

### vagrant

It was a simple process after you have clear what you really want to do:

    $ cd myawesomebox
    $ vagrant init  # Edit the file if you want more memory or similar
    $ git clone git@github.com:YOUR_USERNAME/docker
    $ vagrant ssh
    $ sudo su -

What we did there? We have created a `Vagrantfile` and we clone the repo in the
same folder. Thanks to that when we are inside the vagrant box (with `vagrant
ssh`) we will be able to access to it on the path `/vagrant` of your box.

The advantage of this approach is that you can access to all the docker code
from your host machine in the path `myawesomebox` so you will not need to copy
any key, any conf or anything like that.

### docker

Now it's time to update your docker server and create your on docker client
(remember that we are logged in as root on that box):

    # cd /vagrant/docker
    # make build&&make binary
    # service docker stop
    # cp bundles/1.3.2-dev/binary/docker-1.3.2-dev /usr/bin/docker
    # service docker start

Where `1.3.2` is the  current version at the time of writing &
`/usr/bin/docker` is your old docker server binary.

Now you are running a new server, but where is the client?! Easy peasy, on the
same place that the server was originally:

    # bundles/1.3.2-dev/binary/docker
    ...

I usually alias it to the letter `d` to access to it quicker without moving
stuff around:

    # alias d="`pwd`/bundles/1.3.2-dev/binary/docker"

What's next?
------------

I would say that develop some nice pull request? Or at least try! It's fun
anyway :)

I went through all this pain while [@eloycoto](http://twitter.com/eloycoto) &
me were developing a [small PR to show vertical `ps`
outputs](https://github.com/docker/docker/pull/9415), so, thanks mate!

If you have any question or you think that my way of doing this stinks, please,
let me know! I would really, really appreciate it.

---
title: IoT hackathon with Intel Edison and Go
date: 2015-06-18
tags:
    - dev
    - edison
    - go
    - iot
    - gobot
    - influxdb
    - grafana
---

I spent last weekend in a hackathon organised by Intel to show their Intel
Edison platform. I can just say that it was awesome, the quality of the
projects, the prizes, the food, the freebies (yes, they gave us an Intel
Edison)...

But this post is not about that, I want to explain my project and how I made
Golang work in an Intel Edison thanks to [gobot](http://gobot.io/).

As you are already aware, Go easily supports cross compiling creating a binary
that you can use in your other devices. In this case, the Intel Edison is (by
default) a Linux distribution with i386 architecture.

What did I do?
--------------

I did a simple project to track the happiness of the assistant to a conference:
they can vote if it was a good one ro not & the Edison is also tracking the
clapping. All this information is stored into a
[InfluxDB](https://influxdb.com/) and I was using
[Grafana](http://grafana.org/) to demo it:

![image](/iot_grafana.png)

Ok, let's start!

First step: setup the wifi
--------------------------

After you connect the Edison you will have a new decive in `/dev/` with the
form: `/dev/tty.usbserial-...`. You can just use screen to connect to it, in my
case:

    screen /dev/tty.usbserial-A903BU3J 115200 -L

Inside the machine:

    configure_edison --wifi

You could as well use `--setup` if you want to change the name, password, etc...

Cool! Now we have the device in out network, let's see the IP with `ifconfig`
and copy/paste it somewhere.

Second step: Code!
------------------

As I said before I was using the gobot framework. This framework easily allows
you to access to the GPIO that I've been using in the Edison (buttons, lights &
sound sensor).

Here is a snippet:

    gbot := gobot.NewGobot()

    edisonAdaptor := edison.NewEdisonAdaptor("edison")
    buttonPositive := gpio.NewButtonDriver(edisonAdaptor, "button_positive", "4")

    ...

    robot := gobot.NewRobot(
        "buttonBot",
        []gobot.Connection{edisonAdaptor},
        []gobot.Device{buttonPositive, buttonNegative, redLed, greenLed, blueLed, soundSensor},
        work,
    )

`work` is a loop where you can heard for the events created by the devices.

If you want to see the full code: https://github.com/agonzalezro/iotroadshow_june_2015/blob/master/main.go

Third step: compile, deploy & run
---------------------------------

Crosscompile it. I was using [gox](https://github.com/mitchellh/gox) but you
can use the default tools for that as well. In my case:

    gox -arch="386" -os="linux"

This will generate a file called `project_linux_386` that is what you will need
to copy to the Edison.

To copy it you just need a simple scp:

    scp project_linux_i386 root@[the_edison_ip]:/home/root/my_program

And to run it you can ssh and manually run it or as I was doing:

    ssh root@[the_edison_ip] /home/root/my_program

I've automated this process in a
[Makefile](https://github.com/agonzalezro/iotroadshow_june_2015/blob/master/Makefile).

Also, feel free to check the
[README.md](https://github.com/agonzalezro/iotroadshow_june_2015/blob/master/README.md)
with a better explanation about what my project was.

Any question? Reach me on twitter as
[@agonzalezro](http://twitter.com/agonzalezro) or just post a comment here.

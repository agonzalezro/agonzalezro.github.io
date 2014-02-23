date: 2011-06-08 18:28
tags: unity, gnome3, desktop, ubuntu, gnome

How-to install GNOME 3 instead of Unity on Ubuntu 11.04
=======================================================

I don't have anything against Unity, but sometimes I want to test, and
this is one of this times.

I don't know the reason (or perhaps I do), but install GNOME 3 on a
ubuntu system isn't as easy as it must be.

First of all we need to add the GNOME 3 repos, so, in a console (Alt+F2
and then write gnome-terminal) you must write:

    sudo add-apt-repository ppa:gnome3-team/gnome3

Then, we must update our system and install the gnome shell:

    sudo apt-get updatesudo apt-get dist-upgradesudo apt-get install gnome-shell

After that, sometimes we have problems with the themes (you can reboot
to test it, but I recommend you to follow this steps), so, we must
remove the accesibility themes and install the new ones (and another
program that we will need after that):

    sudo apt-get remove gnome-accessibility-themessudo apt-get install gnome-themes-standard gnome-tweak-tool

Well... now, you can reboot your system and login with GNOME selected as
session. You will see your new GNOME 3, but, we must tweak it, for this,
you can push Alt+F2 and write:

    gnome-tweak-tool

I recommend you to have this themes configuration (you can change the
icons if you like) and activate the option on the first tab called "Have
file manager handle the desktop":

![image](static/tweak_tool.png%0A%20:width:%2050%%0A%20:align:%20center%0A%20:target:%20static/tweak_tool.png)

Good luck! And if you have any trouble, please, feel free to ask me in
the comments!

PS: [@marioquartz](http://twitter.com/marioquartz) wants to see the
result, so here it is (click to enlarge)!

![image](static/gnome3_desktop.png%0A%20:width:%2050%%0A%20:align:%20center%0A%20:target:%20static/gnome3_desktop.png)

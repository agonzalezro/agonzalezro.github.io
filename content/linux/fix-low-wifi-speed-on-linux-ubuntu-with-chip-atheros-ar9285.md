date: 2011-07-03 13:07
tags: low speed, linux, atheros, wifi, ath9k, ubuntu, ar9285

Fix low wifi speed on Linux (Ubuntu) with chip Atheros AR9285
=============================================================

I was very happer after buy my new computer Dell Vostro v130, but after
install Linux on it I've realized that the download speed via WiFi was
very slow! To solve this I found two "solutions", one of them works, but
the other not (for me).

The solutions that didn't work is more easy, so I will start with it,
you must install `linux-backports-modules-net-natty-generic`, you can do
it via synaptic, ubuntu software center, aptitude, apt... I show you a
screenshot doing it with ubuntu software center:

![image](static/software_center.png)

The second "solution" is deactivate the hardware cryptography of the
module, I don't know if this could cause security problems or instead
use hardware it will use software crypt, anyway, it is the best
solutions that I find until the moment.

To do that, you must create the file `/etc/modprobe.d/ath9k.conf` with
the content: `options ath9k nohwcrypt=1`, you can do it easily with:

    echo "options ath9k nohwcrypt=1" > /etc/modprobe.d/ath9k.conf

If you have any questions, or you find a better solution, please, let me
know.

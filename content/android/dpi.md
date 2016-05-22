date: 2016-06-22
tags: android, dpi, root, op2

Change your phone DPIs without root
===================================

I know that this post doesn't match that much with the typical posts I write here, but it seems needed! Every time I searched how to change the DPIs on my Android phone I was referred to root apps. I don't have my phone rooted (too much hassle) so I prefer not to do it just for this.

Before changing the DPIs, what's exactly a DPI? [From wikipedia](https://en.wikipedia.org/wiki/Dots_per_inch):

> Dots per inch (DPI, or dpi) is a measure of spatial printing or video dot density, in particular the number of individual dots that can be placed in a line within the span of 1 inch (2.54 cm).

Can you translate the previous phrase? It's basically a virtual pixel. The pixel size depends on the screen size, bigger phones will show small icons, smaller phones will do the opposite. With DPIs this problem is fixed because the sizes are relative.

So, how did I end up doing it? Thankfully [I found this post](http://www.androidbeat.com/2015/07/how-to-change-dpi-of-android-device-without-root/) where they explain how to do it with just two commands:

    adb shell wm density 420
    adb reboot

Done!

If you don't have `adb` installed probably your best bet is getting it with [Android Studio](https://developer.android.com/studio/index.html). There are other options if you just want the SDK.

For the record, I have tested this method with a One Plus Two, but I am pretty sure it will work in a lot of different models.

Happy Android'ing!

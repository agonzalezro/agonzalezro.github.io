---
title: How to manage multiple errors in Go
date: 2014-10-17
tags:
   - dev
   - errors
   - go
---

Let me start with a disclaimer, I don't really know if this is a pattern that
must be followed or it's just a weird idea coming out of my head.

The second disclaimer is that I am pretty sure that I am not the only mind that
thought about this, but I didn't see it in use in any place. Why?

Error handling in Go has his advantages and disadvantages, for me, the most
important disadvantage is the "weird" way of checking the error just after the
line that can raise it.

I've experimenting a little bit with it and I found this solution:

<script src="https://gist.github.com/agonzalezro/ccd3c29a24149f7787ea.js"></script>

Basically, with the default approach you would need 2 new lines as follows:

`````
if err != nil {
   ...
}
`````

I find this pattern pretty useful for things like http handlers or so.

Also, you are able to add a `switch` at the end to check the kind of error and
keep your code more "organized".

What do you think? Should I use it in every place I can? Do you do it in a
better way?

date: 2014-07-27
tags: theme, theming, polo, BOOTSTRA.386

polo supports theming now!
==========================

If you have seen my blog before I am pretty sure that you remember that the
current theme is not the one that it used to be. I've created a theming
"engine" for [polo](https://github.com/agonzalezro/polo) and for doing the
showcase of the functionality I've chosen the awesome
[BOOTSTRAP/386](https://github.com/kristopolous/BOOTSTRA.386) theme.

In this post I am going to try to explain how the theming works. First of all I
wanted a really easy way of implementing/overriding/composite themes so I
decided for the following:

1. Using [go-bindata](https://github.com/jteeuwen/go-bindata) (thanks again to
   [@francesc](https://twitter.com/francesc) for the recommendation) I include all
   the default templates (with a basic bootstrap theme) in the polo binary.
2. If the place where you have your content override some of the [default
   templates](https://github.com/agonzalezro/polo/tree/master/templates) as for
   example [I am doing
   here](https://github.com/agonzalezro/agonzalezro.github.io/tree/master/templates)
   it will used those.
3. If you don't have a local template, polo will use the ones included in the
   binary.
3. Profit!

As you can see is really straightforward to create your own theme for polo now.
As I said before I wanted to showcase the theming "engine" with something that
you are going to remember as it can be the `BOOTSTRA.386` theme, but I suspect
that in few days I am going to change it back to something more standard.

PS: I was really missing this blue/grey DOS design: `EDIT`, `QBASIC`,
`DBASE`... so much fun!

PS2: this is the commit where I've changed the blog theme:
[12d73af](https://github.com/agonzalezro/agonzalezro.github.io/commit/12d73af4a6b68182dd4fd67db03df4da5c8aea2f).
If you want to take a look forget about the `*.html` changes and search for the
`templates/` changes. As you can see it is really straightforward.

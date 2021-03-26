---
title: Signing your GitHub work with your Keybase keys
date: 2016-04-06
tags:
    - devops
    - security
    - gpg
    - github
    - git
---

As you may know, yesterday, [GitHub has presented a way to verify your commits](https://github.com/blog/2144-gpg-signature-verification) on their platform. This is not something new, it's part of the git protocol, but now, they will show a fancy "verified" label everytime you push a signed commit. Cool? Yeah, pretty cool.

One of the problems I always had since I know GPG is to keep my keys locally. I am pretty sure that some other people take care of their keys as if they were part of their family, but I didn't feel that need yet. [Keybase](https://keybase.io/) partially solved this problem for me, let's hope it did it for you as well (ask me for an invite if you don't have one yet).

_I want to start this article with a disclaimer, I am not a security professional or anything even closer to it; so, if you think I am saying anything stupid, please, do let me know. Also, if you are a heavy user of Keybase, take my steps carefully because I don't know if you account will continue being usable by Keybase (I would expect so, but a disclaimer is always good)._

**What do we need to do then?** Imagine that you are myself and you don't have `keybase` installed yet, also, you have a Mac:

    brew install keybase

Now go to your Keybase account and download the public and private key, if you don't know how to do it, follow [this tutorial by Tom Atkins](http://www.keybits.net/2016/02/import-keybase-private-key/). Summarising it:

1. Go to your Keybase account.
2. Click on your key fingerprint and copy/paste that on a file.
3. Click on "edit", then "export my private key" and copy/paste that as well in a different file.
4. Now, `gpg --allow-secret-key-import --import keybase-private.key`.
5. And, `gpg --import keybase-public.key`.

You are good to go now.

The problem that you will face trying to use your Keybase account is that your email address will look something like `username@keybase.io` and you can not verify that account on github. For that reasonwe will need to update our key for adding your normal account email and delete the keybase one.

So, let's add your normal account:

```
# alex @ Alexs-MacBook-Pro in ~/Desktop [18:14:34]
$ gpg --edit-key agonzalezro@keybase.io
...
gpg> adduid
Real name: Alexandre González Rodríguez
Email address: agonzalezro@gmail.com
Comment:
You are using the `utf-8' character set.
You selected this USER-ID:
    "Alexandre González Rodríguez <agonzalezro@gmail.com>"

Change (N)ame, (C)omment, (E)mail or (O)kay/(Q)uit? o

You need a passphrase to unlock the secret key for
user: "keybase.io/agonzalezro <agonzalezro@keybase.io>"
4096-bit RSA key, ID 68C84A97, created 2014-03-11


pub  4096R/68C84A97  created: 2014-03-11  expires: 2024-03-08  usage: SCEA
                     trust: unknown       validity: unknown
sub  4096R/74F6172C  created: 2014-03-11  expires: 2024-03-08  usage: SEA
[ unknown] (1)  keybase.io/agonzalezro <agonzalezro@keybase.io>
[ unknown] (2). Alexandre González Rodríguez <agonzalezro@gmail.com>
```

**Update: Chris Miller showed me on the comments that this step is not really needed, so don't delete you key, just write `q` to exit and save the changes.**

And delete the `keybase.io` one:

```
...
gpg> 1

pub  4096R/68C84A97  created: 2014-03-11  expires: 2024-03-08  usage: SCEA
                     trust: unknown       validity: unknown
sub  4096R/74F6172C  created: 2014-03-11  expires: 2024-03-08  usage: SEA
[ unknown] (1). Alexandre González Rodríguez <agonzalezro@gmail.com>
[ unknown] (2)* keybase.io/agonzalezro <agonzalezro@keybase.io>

gpg> deluid
Really remove this user ID? (y/N) y

pub  4096R/68C84A97  created: 2014-03-11  expires: 2024-03-08  usage: SCEA
                     trust: unknown       validity: unknown
sub  4096R/74F6172C  created: 2014-03-11  expires: 2024-03-08  usage: SEA
[ unknown] (1). Alexandre González Rodríguez <agonzalezro@gmail.com>

gpg> q
Save changes? (y/N) y
```

What we did there on the first line was select the account `keybase.io`, please, check the number associated with your `keybase.io` account, don't press `1` just for the sake of it.

You have everything you need now, so you just need to export your key and [import it on github](https://github.com/settings/keys):

```
gpg --armor --export agonzalezro@gmail.com
```

PS: `pbcopy` is your friend here if you are using Mac :)

The only thing you need to do now is sign a commit, do that with `git commit -S` and after pushing you will have this beautiful "label" close to your commit.

[![github verified commit](/github_verified_commit.png)](https://github.com/agonzalezro/agonzalezro.github.io/commits/polo)

I hope that you enjoyed the tutorial, let me know on the comments or on twitter ([@agonzalezro](https://twitter.com/agonzalezro)) if something I do is stupid or if you have found it useful!

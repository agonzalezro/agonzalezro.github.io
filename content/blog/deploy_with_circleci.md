date: 2015-06-18
tags: polo, deploy, circleci

How to automagically generate your polo blog with CircleCI
==========================================================

If you are using [polo](http://github.com/agonzalezro/polo) and you want to generate
the HTML files every time that you push to a branch you can easily do that with
[CircleCI](http://circleci.com).

What are the steps that I need to follow to achieve this?

CircleCI
--------

1. Create a CircleCI account.
2. Add your blog repo.
3. Give CircleCI permissions to write to your repo.

For the third point you need to go to the configuration of your repo (the gear
close to the name of your blog repo) > SSH Keys > Create and add "your user
here" key.

Your repo git
-------------

1. Create a branch called polo (or whatever you prefer).
2. Add there all your content and remove all the html and generated files and
   folder.
3. Add this `circle.yml` file (this is the example I use in this blog):

<script src="http://gist-it.appspot.com/https://github.com/agonzalezro/agonzalezro.github.io/blob/polo/circle.yml"></script>

What this will do? It will download polo, compile your site, remove all the
unneeded files and push the new htmls to the `master` branch of your repo.

Two notes here:

- Please, be aware that step 1 is move all the content to another branch,
  if not it will get deleted. You can restore it later, but better if you don't
  need to do it.
- I am using master to push because I am using it for agonzalezro.github.io, if
  you want to use it for github pages you will need to push to `gh-pages`.

Happy blogging!

---
title: Save hook for major modes
date: 2016-5-5
tags:
  - spacemacs
  - hook
---

One of the things I like the most about Go is its `go fmt` tool. I don't worry about formatting my code while I am writing it because I know that `fmt` is going to be there and it will do the work for me later.

Said that, the Go layer for Spacemacs is the one that is going to run it for you. Sometimes we need to deal with languages that don't have this functionality, in my case, I found this issue working with Elixir & Ruby (happily Python forces you to write well :D).

Since I got really used to the `fmt` tool I wanted a similar solution for those languages and it seems that a simple auto indentation all over the file could do it for me. How did I add this behaviour for those languages? Just adding this to my [`init.el`](https://github.com/syl20bnr/spacemacs/blob/master/doc/DOCUMENTATION.org#alternative-setup):

    (defun indent-some-languages()
      (case major-mode
        ((elixir-mode ruby-mode) (spacemacs/indent-region-or-buffer))))

    (defun dotspacemacs/user-config ()
      ...
      (add-hook 'before-save-hook 'indent-some-languages)
      )

What I am doing there is registering a new hook just before saving the file that will check if I am in Ruby or Elixir mode and in that case call `spacemacs/indent-region-or-buffer` that will indent the whole file for me.

If you are familiarised with Lisp this snippet will probably look pretty simple to you; but trust me, it took me a while to make it work. This is the reason why I thought it could be interesting to share it.

I would love to know your tricks for Spacemacs, share them with me here or at [@agonzalezro](https://twitter.com/agonzalezro).

---
title: Tailing multiple logs with tmux
date: 2014-03-15
tags:
  - devops
  - tmux
---

I had a system that was creating a different log for each worker. Those logs
where in the form: `/var/log/baselog`, `/var/log/baselog.1`,
`/var/log/baselog.2` and so on. I wanted to tail them but they were being
updated simultaneously so the output of the tail was being a mess.

I am a [tmux](http://tmux.sourceforge.net/) user since few months ago (if you
aren't, you should!) so I've decide to open all of them in different tmux
panes. Thanks to having a pane for every log what we will achieve is the
ability to scroll just one of them, maximize it in case that we need it, move
to a new window, save the buffer...

How can you achieve that? Quite simple, just download this script to some
place:

<script src="https://gist.github.com/agonzalezro/9573541.js"></script>

Once you have saved it installed, run it with the base log file:

    sh tail_several_logs.sh /var/log/baselog

The script have some limitations easily fixable:

- You should provide a fullpath.
- The logs should be in the form of baselog.N where N is a number.
- I am pretty sure that the loop can be done better.
- And select the layout in every iteration is not the best of the ideas, but it
  works.

Feel free of do whatever you want with the script. I just hope that it's useful
for somebody else.

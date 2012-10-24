#!/usr/bin/env python

from datetime import date


def get_age():
    # Could be improved but... fuck it! :D
    elapsed_days = date.today() - date(1984, 4, 4)
    return int(elapsed_days / 365.25)


if __name__ == '__main__':
    print ".. |age| replace:: {age}".format(age=get_age())

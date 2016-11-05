#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Rabin-Miller Monte Carlo primality test"""

from random import randint
from optparse import OptionParser

__appname__ = "rabin-miller"
__author__  = "David Beran <beran3@gmail.com>"
__version__ = "0.1"
__license__ = "GNU GPL 3.0 or later"

def C(sample, d, s, n):
    for a in sample:
        x = a ** d % n

        restartLoop = False

        if x is 1 or x is (n - 1):
            continue
        else:
            for r in range(0, s - 1):
                x = x ** 2 % n
                if x is 1:
                    # print('whitness: {}'.format(a))
                    return False
                elif x is (n - 1):
                    restartLoop = True
                    continue

            if not restartLoop:
                # print('whitness: {}'.format(a))
                return False

    return True

if __name__ == '__main__':
    parser = OptionParser(version="%%prog v%s" % __version__,
            usage="%prog [options] NUMBER ...",
            description=__doc__.replace('\r\n', '\n').split('\n--snip--\n')[0])

    parser.add_option("-m", help="number of precision (int)",
                            action="store",
                            type="int",
                            default=4
                        )

    # Allow pre-formatted descriptions
    parser.formatter.format_description = lambda description: description

    opts, args  = parser.parse_args()

    if len(args) != 1:
        parser.error("incorrect number of arguments")
    if opts.m < 1:
        parser.error("precision must be at least 1")

    n = int(args[0])
    # print('n = {}'.format(n))

    # find parameters s and d
    # we know that n = 2^d * s + 1
    s = 0
    d = n - 1
    while (d % 2 is 0):
        d = d >> 1
        s = s + 1

    # print('d = {}\ns = {}\n----------'.format(d, s))

    # vector of m random numbers to check n against for primality
    x = [randint(1, n) for i in range(1, opts.m)]

    if C(sample = x, d = d, s = s, n = n):
        p = 1 / (2 ** opts.m)
        print('{} is a prime with probability {}'.format(n, p))
    else:
        print('{} is NOT a prime'.format(n))

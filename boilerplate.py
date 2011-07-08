#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""[application description here]"""

__appname__ = "[application name here]"
__author__  = "Stephan Sokolow (deitarion/SSokolow)"
__version__ = "0.0pre0"
__license__ = "GNU GPL 3.0 or later"

import logging
log = logging.getLogger(__name__)

# -- Code Here --

if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser(description=__doc__, version="%%prog v%s" % __version__)
    parser.add_option('-v', '--verbose', action="count", dest="verbose",
        default=2, help="Increase the verbosity. Can be used twice for extra effect.")
    parser.add_option('-q', '--verbose', action="count", dest="quiet",
        default=0, help="Decrease the verbosity. Can be used twice for extra effect.")

    opts, args  = parser.parse_args()

    # Set up clean logging to stderr
    log_levels = [logging.CRITICAL, logging.ERROR, logging.WARNING,
                  logging.INFO, logging.DEBUG]
    opts.verbose = min(opts.verbose - opts.quiet, len(log_levels) - 1)
    opts.verbose = max(opts.verbose, 0)
    logging.basicConfig(level=log_levels[opts.verbose],
                        format='%(levelname)s: %(message)s')


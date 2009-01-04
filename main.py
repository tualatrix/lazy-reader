#!/usr/bin/python

import gobject
import pynotify
from icon import Icon

if __name__ == '__main__':
    gobject.threads_init()
    if not pynotify.init("Basics"):
        sys.exit(1)
    Icon().main()

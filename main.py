#!/usr/bin/python

import gtk
import gobject
import pynotify
from icon import Icon
from notify import notify
from reader import reader

def main():
    gtk.gdk.threads_enter()
    reader.start()
    gtk.main()
    gtk.gdk.threads_leave()

if __name__ == '__main__':
    gobject.threads_init()
    if not pynotify.init("Basics"):
        sys.exit(1)
    Icon()
    main()

#!/usr/bin/python
# coding: utf-8

import pygtk
pygtk.require('2.0')
import pynotify
import sys
import gtk
import os
import feedparser

def help_cb(n, action):
    assert action == "help"
    print "You clicked Help"
    n.close()
    gtk.main_quit()

if __name__ == '__main__':
    if not pynotify.init("Basics"):
        sys.exit(1)

#    parser = feedparser.parse('http://fe.cn/feed')
    parser = feedparser.parse('http://feed.feedsky.com/imtx')

    entry = parser.entries[0]
#    title = 'Git for Windows'
#    summary = 'Test'
    title = entry.title
    summary = entry.summary


    n = pynotify.Notification(title, 
            '<b>%s</b> written at <i>%s</i>\n\n%s' % (entry.author, entry.updated, summary))
    n.set_hint('x', 1065)
    n.set_hint('y', 20)
    helper = gtk.Button()
    icon = helper.render_icon(gtk.STOCK_DIALOG_INFO, gtk.ICON_SIZE_DIALOG)
    n.set_icon_from_pixbuf(icon)
    n.add_action("empty", "Read more...", help_cb)

    n.show()

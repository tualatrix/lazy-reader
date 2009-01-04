import threading
import feedparser
from googlereader.reader import GoogleReader
from private import login_info

class Reader(threading.Thread):
    gr = GoogleReader()
    entry = None
    feed = None
    entries = []

    def __init__(self):
        super(Reader, self).__init__()

#    def run(self):
#        print 'start parse feed'
#        parser = feedparser.parse('http://feed.feedsky.com/imtx')
#        self.entry = parser.entries[0]
#        print 'finish parse feed'

    def run(self):
        print 'start parse feed'
        self.gr.identify(**login_info)
        self.gr.login()
        self.feed = self.update_feed()
        self.entries = list(self.feed.get_entries())
        self.entry = self.entries[0]
        print 'finish parse feed'

    def update_feed(self):
        feed = None
        while not feed:
            try:
                feed = self.gr.get_unread()
            except:
                pass

        return feed

    def get_entry(self):
        return self.entry

    def set_read(self, entry):
        ok = False
        while not ok:
            try:
                self.gr.set_read(entry['google_id'])
            except:
                pass
            else:
                ok = True
        self.update_feed()

reader = Reader()

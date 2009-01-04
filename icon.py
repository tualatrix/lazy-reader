import gtk
import random
import gobject
import threading
import egg.trayicon
import datetime
from reader import reader
from notify import notify
from popupmenu import PopupMenu
from utils import strip_tags

class Icon(egg.trayicon.TrayIcon):
    def __init__(self):
        super(Icon, self).__init__('Lazy Reader')

        self.eventbox = gtk.EventBox()
        self.eventbox.connect('button_press_event', self.on_eventbox_clicked)
        self.add(self.eventbox)

        image = gtk.image_new_from_file('pixmaps/lazy-reader.png')
        self.eventbox.add(image)

        self.show_all()

        gobject.timeout_add(self.get_random_interval(), self.on_timeout)

    def get_random_interval(self):
        return random.randrange(90000, 180000, 1000)

    def on_timeout(self):
        self.on_left_clicked()
        gobject.timeout_add(self.get_random_interval(), self.on_timeout)

    def on_left_clicked(self):
        entry = reader.get_entry()
        title = entry['title'] 
        summary = entry['summary']
        if summary is None:
            summary = entry['content']
        updated = entry['updated']
        updated = datetime.date.fromtimestamp(updated).isoformat()
        author = entry['author']

        if notify.closed is True:
            notify.update(title, 
                '<b>%s</b> written at <i>%s</i>\n\n%s' % (author, updated, strip_tags(summary)))
            notify.attach_to_widget(self)

    #        read_more_button = gtk.Button()
    #        icon = read_more_button.render_icon(gtk.STOCK_DIALOG_INFO, gtk.ICON_SIZE_DIALOG)
    #        n.set_icon_from_pixbuf(icon)

            notify.closed = False
            notify.show()
            reader.set_read(entry)
            reader.iter_next()

    def on_eventbox_clicked(self, widget, event):
        if event.button == 1:
            self.on_left_clicked()
        elif event.button == 2:
            print 'clicked the middle'
        elif event.button == 3:
            menu = PopupMenu()
            menu.popup(event)

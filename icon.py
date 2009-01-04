import gtk
import threading
import pynotify
import egg.trayicon
import webbrowser
from reader import reader
from popupmenu import PopupMenu

class Icon(egg.trayicon.TrayIcon):
    def __init__(self):
        super(Icon, self).__init__('Lazy Reader')

        self.eventbox = gtk.EventBox()
        self.eventbox.connect('button_press_event', self.on_eventbox_clicked)
        self.add(self.eventbox)

        image = gtk.image_new_from_file('pixmaps/lazy-reader.png')
        self.eventbox.add(image)

        self.show_all()

    def on_read_more_clicked(self, widget, entry):
        webbrowser.open_new_tab(entry['link'])

    def on_left_clicked(self):
        entry = reader.get_entry()
        title = entry['title'] 
        summary = entry['summary']
        if summary:
            summary = entry['content']
        updated = entry['updated']
        author = entry['author']

        n = pynotify.Notification(title, 
            '<b>%s</b> written at <i>%s</i>\n\n%s' % (author, updated, summary), None, self)

        read_more_button = gtk.Button()
        icon = read_more_button.render_icon(gtk.STOCK_DIALOG_INFO, gtk.ICON_SIZE_DIALOG)
        n.set_icon_from_pixbuf(icon)
        n.add_action("empty", "Read more...", self.on_read_more_clicked)
        n.set_timeout(10000)

        n.show()
        reader.set_read(entry)

    def on_eventbox_clicked(self, widget, event):
        if event.button == 1:
            self.on_left_clicked()
        elif event.button == 2:
            print 'clicked the middle'
        elif event.button == 3:
            menu = PopupMenu()
            menu.popup(event)

    def main(self):
        gtk.gdk.threads_enter()

        reader.start()
        gtk.main()
        gtk.gdk.threads_leave()


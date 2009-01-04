import pynotify
import webbrowser
from reader import reader

class Notify(pynotify.Notification):
    closed = True

    def __init__(self):
        super(Notify, self).__init__('Notify')

#        read_more_button = gtk.Button()
#        icon = read_more_button.render_icon(gtk.STOCK_DIALOG_INFO, gtk.ICON_SIZE_DIALOG)
#        n.set_icon_from_pixbuf(icon)
        self.add_action("addstar", "Add Star", self.on_add_star_clicked)
        self.add_action("home", "Read more...", self.on_read_more_clicked)
        self.add_action("star_and_open", "Both", self.on_add_and_open)
        self.set_timeout(10000)
        self.connect('closed', self.on_notification_closed)

    def on_add_and_open(self, widget, action):
        reader.add_star(reader.get_previous())
        webbrowser.open(reader.get_previous()['link'])

    def on_notification_closed(self, widget):
        self.closed = True

    def on_add_star_clicked(self, widget, action):
        reader.add_star(reader.get_previous())

    def on_read_more_clicked(self, widget, action):
        webbrowser.open(reader.get_previous()['link'])
   
notify = Notify()

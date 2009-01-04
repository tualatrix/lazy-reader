import pynotify
import webbrowser
from reader import reader

class Notify(pynotify.Notification):
    def __init__(self):
        super(Notify, self).__init__('Notify')

#        read_more_button = gtk.Button()
#        icon = read_more_button.render_icon(gtk.STOCK_DIALOG_INFO, gtk.ICON_SIZE_DIALOG)
#        n.set_icon_from_pixbuf(icon)
        self.add_action("home", "Read more...", self.on_read_more_clicked)
        self.set_timeout(10000)

    def on_read_more_clicked(self, widget, action):
        assert action == "home"
        webbrowser.open(reader.get_previous()['link'])
   
notify = Notify()

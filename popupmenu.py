import gtk

class PopupMenu:
    def __init__(self):
        self.base_menu = gtk.Menu()
        self.menubar = gtk.MenuBar()

        menu_item_about = gtk.ImageMenuItem('gtk-about',None)
        menu_item_preferences = gtk.ImageMenuItem('gtk-preferences',None)
        self.base_menu.add(menu_item_preferences)
        self.base_menu.add (gtk.SeparatorMenuItem())
        
        menu_item_quit = gtk.ImageMenuItem('gtk-quit',None)
        menu_item_quit.connect('activate', self.exit)
        self.base_menu.add(menu_item_quit)
        
        self.base_menu.show_all() 
    
    def exit(self,widget):
        gtk.main_quit()

    def popup(self,event):
        self.base_menu.popup(None, None, None, 0, event.time); 

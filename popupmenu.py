import gtk

class PopupMenu:
    def __init__(self):
        self.base_menu = gtk.Menu()
        self.menubar = gtk.MenuBar()

        menu_item_refresh = gtk.ImageMenuItem('gtk-refresh',None)
        menu_item_refresh.connect('activate',self.refresh_clicked)
        menu_google_reader = gtk.ImageMenuItem ('Open Google Reader', None)
        menu_mark_read = gtk.ImageMenuItem ('Mark all as read', None)
        menu_item_feed = gtk.ImageMenuItem ('Subscribe to feed', None)
        menu_item_about = gtk.ImageMenuItem('gtk-about',None)
        menu_item_preferences = gtk.ImageMenuItem('gtk-preferences',None)
        self.base_menu.add(menu_google_reader)
        self.base_menu.add(menu_item_refresh)
        self.base_menu.add(menu_mark_read)
        self.base_menu.add(menu_item_feed)
        self.base_menu.add(menu_item_preferences)
        self.base_menu.add (gtk.SeparatorMenuItem())
        
        view_item = gtk.Menu()
        menu_view_item = gtk.MenuItem ('View Items', None)		
        menu_view_item.set_submenu (view_item)
        self.base_menu.add (menu_view_item)
        
        self.base_menu.add (gtk.SeparatorMenuItem())
        self.base_menu.add(menu_item_about)
        
        menu_item_quit = gtk.ImageMenuItem('gtk-quit',None)

        menu_item_quit.connect('activate', self.exit)

        self.base_menu.add(menu_item_quit)
        
        self.base_menu.show_all() 
    
    def exit(self,widget):
        gtk.main_quit()
        
    def feed_clicked (self, widget):
        popup = feedPopup()
        
    def refresh_clicked (self, widget):
        global feedsChanged
        feedsChanged = 1		
        updateFeeds()
        refresh().start()
    
    def preferences_clicked (self, widget):
        configureWindow = configure_base_menu()
    
    def about_clicked(self,widget):
    # about menu item handler -> create the about window
        grnotify_app.about.create()
        
    def popup(self,event):
    # popup-show the menu
        self.base_menu.popup( None, None, None, 0, event.time); 
    
    def close(self,widget):
        # the warning close button has been clicked (or the window was closed else way)
        grnotify_app.warning_close_button = True
        
        # the window isn't opened
        grnotify_app.warning_window_opened = False
        self.base_menu.destroy()

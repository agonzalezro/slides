from gi.repository import Gtk, WebKit


class Browser(object):
    def __init__(self):
        self.create_elements()
        self.configure_elements()
        self.bind_signals()

    def create_elements(self):
        self.window = Gtk.Window()
        # Toolbar
        hbox = Gtk.HBox()
        self.entry = Gtk.Entry()
        self.button = Gtk.Button(stock=Gtk.STOCK_FIND)
        hbox.pack_start(self.entry, True, True, 0)
        hbox.pack_start(self.button, False, True, 0)
        # Web view
        self.view = WebKit.WebView()
        scrolled = Gtk.ScrolledWindow()
        scrolled.add(self.view)
        scrolled.show()
        # Progress
        self.progress = Gtk.ProgressBar()
        # All the rest
        vbox = Gtk.VBox()
        vbox.pack_start(hbox, False, True, 0)
        vbox.pack_start(scrolled, True, True, 0)
        vbox.pack_start(self.progress, False, True, 0)
        self.window.add(vbox)

    def configure_elements(self):
        self.window.resize(640, 480)
        self.window.show_all()
        self.progress.hide()

    def bind_signals(self):
        self.window.connect('delete-event', Gtk.main_quit)
        self.button.connect('clicked', self.on_button_clicked)
        self.view.connect('load-progress-changed', self.on_load_progress)

    def get_full_url(self, text):
        return text if text.startswith('http') else 'http://%s' % text

    def on_button_clicked(self, widget):
        self.view.open(
                self.get_full_url(self.entry.get_text()))

    def on_load_progress(self, widget, amount):
        self.progress.set_fraction(amount / 100.0)
        if amount == 100 or amount == 0:
            self.progress.hide()
        else:
            self.progress.show()


if __name__ == '__main__':
    browser = Browser()
    Gtk.main()

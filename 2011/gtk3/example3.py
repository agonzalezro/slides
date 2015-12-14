import json
import urllib
import webbrowser

from gi.repository import Gtk, GdkPixbuf


class IconView(Gtk.Window):
    URL_IDS = ('https://api.twitter.com/1/followers/ids.json?'
               'cursor=-1&screen_name=agonzalezro')
    URL_LOOKUP = ('https://api.twitter.com/1/users/lookup.json?'
                  'user_id=%s&include_entities=true')

    def __init__(self):
        super(IconView, self).__init__()
        self.store = Gtk.ListStore(GdkPixbuf.Pixbuf, str)
        self.icons_list = self.create_list()
        scroll = Gtk.ScrolledWindow()
        scroll.add(self.icons_list)
        self.add(scroll)
        self.show_all()
        self.connect_signals()
        self.resize(640, 480)

    def create_list(self):
        icons_list = Gtk.IconView()
        icons_list.set_model(self.store)
        icons_list.set_pixbuf_column(0)
        icons_list.set_text_column(1)
        return icons_list

    def connect_signals(self):
        self.connect('delete-event', Gtk.main_quit)
        self.icons_list.connect('item-activated', self.on_item_activated)

    def get_twitter_users(self, limit):
        response = urllib.urlopen(self.URL_IDS)
        ids = json.loads(response.read()).get('ids')
        ids = ','.join(map(str, ids[0:limit]))  # Max 100 per query
        response = urllib.urlopen(self.URL_LOOKUP % ids)
        users = json.loads(response.read())
        minimal_info = []
        for user in users:
            minimal_info.append((user['profile_image_url'],
                                 '@%s' % user['screen_name']))
        return minimal_info

    def fill_buddies(self, buddies=30):
        for user in self.get_twitter_users(buddies):
            self.store.append([self.get_icon_from_url(user[0]),
                               user[1]])

    def get_icon_from_url(self, url):
        icon = GdkPixbuf.PixbufLoader()
        icon.set_size(48, 48)
        icon.write(urllib.urlopen(url).read())
        icon.close()
        return icon.get_pixbuf()

    def on_item_activated(self, widget, item):
        webbrowser.open('http://twitter.com/%s' % self.store[item][1][1:])


if __name__ == '__main__':
    window = IconView()
    window.fill_buddies(50)
    Gtk.main()

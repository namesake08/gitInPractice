import json
import requests
import signal
import os
import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Notify', '0.7')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk, GObject
from gi.repository import Notify
from gi.repository import AppIndicator3

APPID = "GTK Test"
CURRDIR = os.path.dirname(os.path.abspath(__file__))
ICON = os.path.join(CURRDIR, 'web.png')

class Notificator:
    def __init__(self, cachefile='config.json', url='http://rmnova.30meridian.com/API'):
        self.cachefile = cachefile
        self.url = url

        try:
            with open(self.cachefile) as file:
                cache = json.load(file)
                self.email = cache['email']
                self.token = cache['token']
        except IOError:
            self.email = None
            self.token = None

    def login(self, email, password):
        self.email = email

        request = {"notify_method": "login", "email": email, "password": password}
        response = json.loads(requests.post(self.url, json=request).json())

        if 'error' in response:
            raise IOError
        else:
            self.token = response['token']

        self.write_cache()



    def check(self):
        request = {"notify_method": "get_last", "email": self.email, "token": self.token}
        response = json.loads(requests.post(self.url, json=request).json())

        if response.get('notifies', None):
            pass
        else:
            pass

        self.start()

    def start(self):
        GObject.timeout_add(3000, self.check)

    def write_cache(self):
        with open(self.cachefile, "wt") as file:
            json.dump({
                'email': self.email,
                'token': self.token,
            }, file)


class TrayIcon:
    def __init__(self, appid, icon, menu):
        self.menu = menu

        APPIND_SUPPORT = 1
        # TODO SAFETY
        if APPIND_SUPPORT == 1:
            self.ind = AppIndicator3.Indicator.new(
                appid, icon,
                AppIndicator3.IndicatorCategory.APPLICATION_STATUS)
            self.ind.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
            self.ind.set_menu(self.menu)
        else:
            self.ind = Gtk.StatusIcon()
            self.ind.set_from_file(icon)


class Handler:
    filename = "config.json"

    def __init__(self, window, notificator):
        self.window = window
        self.notificator = notificator
        self.window_is_hidden = True

    def onShowOrHide(self, *args):
        if self.window_is_hidden:
            self.window.show()
        else:
            self.window.hide()
        self.window_is_hidden = not self.window_is_hidden

    def onQuit(self, *args):
        Notify.uninit()
        Gtk.main_quit()

    def onButtonPressed(self, box, *args, **kwargs):
        children = box.get_children()
        entries = []

        for child in children:
            if isinstance(child, Gtk.Entry):
                entries.append(child)

        values = {}
        for entry in entries:
            values.update({entry.get_name(): entry.get_text()})

        email = values.get('Login')
        password = values['Password']
        self.notificator.login(email, password)
        self.window.hide()
        self.notificator.start()


if __name__ == '__main__':
    signal.signal(signal.SIGINT, Gtk.main_quit)

    notificator = Notificator()

    builder = Gtk.Builder()
    builder.add_from_file('notificator.glade')

    if not notificator.token is None:
        notificator.start()

    window = builder.get_object('window1')
    window.set_icon_from_file(ICON)

    builder.connect_signals(Handler(window, notificator))
    window.show_all()

    entry = builder.get_object('entry1')
    menu = builder.get_object('menu1')
    icon = TrayIcon(APPID, ICON, menu)
    Notify.init(APPID)

    Gtk.main()

#!/usr/bin/env python3
import gi

gi.require_version("Nautilus", "4.0")
gi.require_version("Gtk", "4.0")
from gi.repository import GObject, Nautilus, Gtk, Gio

def back():
    app = Gtk.Application.get_default()
    app.set_accels_for_action("win.up", ["BackSpace"])

class Back(GObject.GObject, Nautilus.InfoProvider):
    def __init__(self):
        pass

    def update_file_info(self, file):
        back()
        return None

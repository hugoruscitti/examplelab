# -*- encoding: utf-8 -*-
import gtk

def on_icon_activate(widget, extra=None):
    print "Icon activated!", extra

def on_icon_popupmenu(widget, button, time, data=None):
    print "Show menu"

icon = gtk.StatusIcon()
icon.set_from_stock(gtk.STOCK_ABOUT)
icon.set_tooltip("Status icon tooltip")

icon.connect('popup-menu', on_icon_popupmenu)
icon.connect("activate", on_icon_activate)

gtk.main()

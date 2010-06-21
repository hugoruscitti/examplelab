# -*- encoding: utf-8 -*-
import gtk

def quit(extra=None, other=None):
    gtk.main_quit()

def on_popup_menu(widget, button, time, menu):
    print "On popup menu"
    menu.show_all()
    menu.popup(None, None, None, 3, time)

def on_item_1_activate(widget, data=None):
    print "Item 1"

def on_item_2_activate(widget, data=None):
    quit()


menu = gtk.Menu()

menu1 = gtk.ImageMenuItem(gtk.STOCK_ABOUT)
menu1.connect('activate', on_item_1_activate)
menu2 = gtk.ImageMenuItem(gtk.STOCK_QUIT)
menu2.connect('activate', on_item_2_activate)

menu.append(menu1)
menu.append(menu2)


window = gtk.Window()
window.set_position('center')
window.set_border_width(8)

image = gtk.Image()
image.set_from_file('image.png')
image.connect('popup-menu', on_popup_menu, menu)

window.add(image)

window.connect('destroy', quit)
window.show_all()

gtk.main()

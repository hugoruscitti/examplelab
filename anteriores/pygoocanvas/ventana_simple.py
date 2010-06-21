# -*- coding: utf-8 -*-
import gtk
import goocanvas

# creación de la ventana
window = gtk.Window()
window.connect("destroy", gtk.main_quit)
window.set_position(gtk.WIN_POS_CENTER)

# creación del Canvas
canvas = goocanvas.Canvas()
window.add(canvas)

# bucle principal
window.show_all()
gtk.main()

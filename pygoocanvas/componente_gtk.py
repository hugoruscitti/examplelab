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

# genera componente gtk y contenedor en canvas
entry = gtk.Entry()
widget = goocanvas.Widget(widget=entry,
                          x=10,
                          y=10,
                          width=150)

# anidación con el nodo principal
root = canvas.get_root_item()
root.add_child(widget)

# bucle principal
window.show_all()
gtk.main()

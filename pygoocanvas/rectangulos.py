# -*- coding: utf-8 -*-
import gtk
import goocanvas

window = gtk.Window()
window.connect("destroy", gtk.main_quit)
window.set_position(gtk.WIN_POS_CENTER)

# creación del Canvas
canvas = goocanvas.Canvas()
window.add(canvas)

# construcción de los rectángulos
box1 = goocanvas.Rect(x=10,
                     y=10,
                     width=50,
                     height=50,
                     radius_x=10,
                     radius_y=10,
                     line_width=1.0,
                     stroke_color="black",
                     fill_color="#cccccc")

box2 = goocanvas.Rect(x=100,
                     y=10,
                     width=50,
                     height=50,
                     line_width=1.0,
                     stroke_color="black",
                     fill_color="yellow")

# se agregan al nodo principal
root = canvas.get_root_item()
root.add_child(box1)
root.add_child(box2)

# bucle principal
window.show_all()
gtk.main()

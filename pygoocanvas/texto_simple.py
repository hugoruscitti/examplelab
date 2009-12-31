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

# creación del texto
text1 = goocanvas.Text(text="Ejemplo de texto",
                      x=10,
                      y=10,
                      font="Sans 12",
                      fill_color="blue")

text2 = goocanvas.Text(text="Texto con <b>atributos</b>\nestilo <i>Pango</i>",
                      x=10,
                      y=50,
                      font="Sans 9",
                      use_markup=True)

# anidación con el nodo principal
root = canvas.get_root_item()
root.add_child(text1)
root.add_child(text2)

# bucle principal
window.show_all()
gtk.main()

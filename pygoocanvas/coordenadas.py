# -*- coding: utf-8 -*-
import gtk
import goocanvas

text_item = None

def on_motion_notify_event(item, event):
    global text_item

    text_item.props.text = "Posición del mouse (%d, %d)" %(event.x, event.y)
    

# creación de la ventana
window = gtk.Window()
window.connect("destroy", gtk.main_quit)
window.set_position(gtk.WIN_POS_CENTER)

# creación del Canvas
canvas = goocanvas.Canvas()
window.add(canvas)

# objeto que muestra el texto
text_item = goocanvas.Text(text="Posición del mouse: ?",
                           x=10,
                           y=10,
                           font="Sans 10",
                           fill_color="blue")

# agrega el texto al canvas
root = canvas.get_root_item()
root.add_child(text_item)

# conecta la señal a la función de respuesta
canvas.connect("motion-notify-event", on_motion_notify_event)

# bucle principal
window.show_all()
gtk.main()

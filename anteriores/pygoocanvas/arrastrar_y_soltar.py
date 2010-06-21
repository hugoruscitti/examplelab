# -*- coding: utf-8 -*-
import gtk
import goocanvas

dragging = False
drag_x = 0
drag_y = 0


# NOTA: el primer argumento será el objeto que gestiona la señal, en este
# caso será "canvas", dado que mas adelante se escribe "canvas.connect..."
def on_button_press_event(item, target, event):
    global dragging, drag_x, drag_y

    if event.button == 1:
        drag_x = event.x
        drag_y = event.y
        dragging = True
    

def on_button_release_event(item, target, event):
    global dragging

    dragging = False

def on_motion_notify_event(item, target, event):
    global dragging, drag_x, drag_y

    if dragging:
        new_x = event.x
        new_y = event.y
        item.translate(new_x - drag_x, new_y - drag_y)

# creación de la ventana
window = gtk.Window()
window.connect("destroy", gtk.main_quit)
window.set_position(gtk.WIN_POS_CENTER)

# creación del Canvas
canvas = goocanvas.Canvas()
window.add(canvas)

# construcción del rectángulo
box1 = goocanvas.Rect(x=10,
                     y=10,
                     width=50,
                     height=50,
                     radius_x=10,
                     radius_y=10,
                     line_width=2.0,
                     stroke_color="black",
                     fill_color="#cccccc")

# eventos asociados al desplazamiento de objetos
box1.connect("button_press_event", on_button_press_event)
box1.connect("button_release_event", on_button_release_event)
box1.connect("motion_notify_event", on_motion_notify_event)

# se agregan al nodo principal
root = canvas.get_root_item()
root.add_child(box1)

# bucle principal
window.show_all()
gtk.main()

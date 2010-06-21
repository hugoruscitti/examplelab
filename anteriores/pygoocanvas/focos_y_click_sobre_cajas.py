# -*- coding: utf-8 -*-
import gtk
import goocanvas

def imprimir_evento(event):
    button, x, y = event.button, event.x, event.y
    print "Pulsa el botón %d en (x=%d, y=%d)" %(button, x, y)

def on_box__button_press_event(view, target, event):
    "Se activa ante la pulsación de un botón en el Mouse"
    imprimir_evento(event)
    canvas = view.get_canvas()
    canvas.grab_focus(view)

def on_box__focus_in_event(view, target, event):
    "El componete ha sido seleccionado por teclado o mediante 'grab_focus'"
    view.props.line_width = 4.0

def on_box__focus_out_event(view, target, event):
    "Selecciona a otro objeto"
    view.props.line_width = 2.0


# creación de la ventana
window = gtk.Window()
window.connect("destroy", gtk.main_quit)
window.set_position(gtk.WIN_POS_CENTER)

# creación del Canvas
canvas = goocanvas.Canvas()
window.add(canvas)

# construcción de los rectángulos
box1 = goocanvas.Rect(x=10, y=10, width=50, height=50, 
                      can_focus=True, # Muy importante
                      fill_color="white")
box2 = goocanvas.Rect(x=100, y=10, width=50, height=50,
                      can_focus=True, # Muy importante
                      fill_color="yellow")

# conexión de señal a función de respuesta
box1.connect("focus_in_event", on_box__focus_in_event)
box1.connect("focus_out_event", on_box__focus_out_event)
box1.connect("button_press_event", on_box__button_press_event)

box2.connect("focus_in_event", on_box__focus_in_event)
box2.connect("focus_out_event", on_box__focus_out_event)
box2.connect("button_press_event", on_box__button_press_event)

# se agregan al nodo principal
root = canvas.get_root_item()
root.add_child(box1)
root.add_child(box2)

# bucle principal
window.show_all()
gtk.main()

import gtk
import goocanvas
 
window = gtk.Window()
window.set_title("Ejemplo de canvas")
window.set_position('center')
window.connect('destroy', gtk.main_quit)

canvas = goocanvas.Canvas()
root = canvas.get_root_item()

box = goocanvas.Rect(x=10, y=10, width=20, height=20)
root.add_child(box)

window.add(canvas)
window.show_all()

gtk.main()

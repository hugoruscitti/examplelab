import gtk
import gaphas
from gaphas.examples import Box

window = gtk.Window()
window.show()
window.connect('destroy', gtk.main_quit)

canvas = gaphas.Canvas()
view = gaphas.GtkView()
view.canvas = canvas

# El cambio mas importante
view.tool = None

view.show()
window.add(view)


box = Box(100, 100)
box.matrix.translate(50, 50)
canvas.add(box)

gtk.main()

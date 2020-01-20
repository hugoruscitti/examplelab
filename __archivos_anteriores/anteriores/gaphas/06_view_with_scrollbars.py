import gtk
import gaphas
from gaphas.examples import Box

window = gtk.Window()
window.connect('destroy', gtk.main_quit)


canvas = gaphas.Canvas()
view = gaphas.GtkView()
view.canvas = canvas
window.set_size_request(300, 300)



# Genera el scroll y lo vincula
scroll = gtk.ScrolledWindow()
scroll.set_hadjustment(view.hadjustment)
scroll.set_vadjustment(view.vadjustment)

window.add(scroll)
scroll.add_with_viewport(view)

box = Box(100, 100)
box.matrix.translate(50, 50)
canvas.add(box)

window.show_all()
gtk.main()

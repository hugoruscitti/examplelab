import gtk
import gaphas
import gaphas.examples

window = gtk.Window()
window.show()
window.connect('destroy', gtk.main_quit)

canvas = gaphas.Canvas()
view = gaphas.GtkView()
view.canvas = canvas
view.show()
window.add(view)


box = gaphas.examples.Box(80, 80)
box.matrix.translate(30, 30)
canvas.add(box)

gtk.main()

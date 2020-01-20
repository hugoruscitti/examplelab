import gtk
import gaphas

window = gtk.Window()
window.show()
window.connect('destroy', gtk.main_quit)

canvas = gaphas.Canvas()
view = gaphas.GtkView()
view.canvas = canvas
view.show()
window.add(view)

gtk.main()

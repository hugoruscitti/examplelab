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

# Normal
line = gaphas.item.Line()
line.handles()[0].pos = (140, 30)
line.handles()[1].pos = (140, 100)
canvas.add(line)

# Orthogonal
line = gaphas.item.Line()
line.handles()[1].pos = (100, 100)
line.handles()[0].pos = (30, 30)
canvas.add(line)
line.split_segment(0, 3)
line.handles()[2].pos = (40, 40)
line.orthogonal = True


# With head
class Line(gaphas.item.Line):

    def __init__(self):
        gaphas.item.Line.__init__(self)

    def set_points(self, p1, p2):
        self.handles()[0].pos = p1
        self.handles()[1].pos = p2

    def draw_tail(self, context):
        cr = context.cairo
        # la linea
        cr.line_to(0, 0)
        cr.stroke()

        # la punta de flecha
        cr.save()
        cr.line_to(10, 5)
        cr.move_to(0, 0)
        cr.line_to(10, -5)
        cr.line_to(10, 5)
        cr.close_path()
        cr.fill()
        cr.restore()


line = Line()
line.set_points((20, 150), (170, 150))
canvas.add(line)


# Si se quiere que sea ortogonal
#line.split_segment(0, 3)
#line.orthogonal = True




gtk.main()

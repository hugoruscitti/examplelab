import gtk
import cairo
import gaphas
import gaphas.examples

window = gtk.Window()
window.connect('destroy', gtk.main_quit)

vbox = gtk.VBox(spacing=8)
window.add(vbox)

canvas = gaphas.Canvas()
view = gaphas.GtkView()
view.canvas = canvas
view.show()
vbox.pack_start(view, expand=True, fill=True)

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



# save Button
button = gtk.Button("Save")
vbox.pack_start(button, expand=False)
button.grab_focus()


def on_button_png_save(widget, canvas):
    svgview = gaphas.View(canvas)
    svgview.painter = gaphas.painter.ItemPainter()

    tmpsurface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 0, 0)
    tmpcr = cairo.Context(tmpsurface)
    svgview.update_bounding_box(tmpcr)
    tmpcr.show_page()
    tmpsurface.flush()

    w, h = svgview.bounding_box.width, svgview.bounding_box.height
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, int(w), int(h))

    cr = cairo.Context(surface)
    svgview.matrix.translate(-svgview.bounding_box.x, -svgview.bounding_box.y)
    cr.save()
    svgview.paint(cr)

    cr.restore()
    cr.show_page()
    surface.write_to_png('demo.png')

    print "saving demo.png"


def on_button_svg_save(widget, canvas):
    svgview = gaphas.View(canvas)
    svgview.painter = gaphas.painter.ItemPainter()

    tmpsurface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 0, 0)
    tmpcr = cairo.Context(tmpsurface)
    svgview.update_bounding_box(tmpcr)
    tmpcr.show_page()
    tmpsurface.flush()

    w, h = svgview.bounding_box.width, svgview.bounding_box.height
    surface = cairo.SVGSurface('demo.svg', w, h)
    cr = cairo.Context(surface)
    svgview.matrix.translate(-svgview.bounding_box.x, -svgview.bounding_box.y)
    svgview.paint(cr)
    cr.show_page()
    surface.flush()
    surface.finish()

    print "saving demo.svg"







button.connect('clicked', on_button_png_save, canvas)
button.connect('clicked', on_button_svg_save, canvas)








window.set_size_request(400, 400)
window.set_border_width(8)
window.set_position("center")
window.show_all()
gtk.main()

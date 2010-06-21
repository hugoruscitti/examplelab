import gtk
import gaphas
import gaphas.examples

class BoxWithText(gaphas.examples.Item):

    def __init__(self, *k, **v):
        gaphas.examples.Item.__init__(self, *k, **v)
        self.width = 0
        self.height = 0

    def draw(self, context):
        cr = context.cairo
        cr.set_source_rgb(0, 0, 0)

        gaphas.util.text_set_font(cr, 'sans bold 14')

        text = "Hola mundo"
        gaphas.util.text_align(cr, 0, 0, text, 1, 1)
        width, height = gaphas.util.text_extents(cr, text)
        p = 10  # padding

        cr.rectangle(0 - p, 0 -p, width + p * 2, height + p * 2)
        cr.stroke()



window = gtk.Window()
window.connect('destroy', gtk.main_quit)

canvas = gaphas.Canvas()
view = gaphas.GtkView()
view.canvas = canvas
window.add(view)

box = BoxWithText()
box.matrix.translate(20, 20)
#box.matrix.rotate(1)
canvas.add(box)


window.show_all()
gtk.main()

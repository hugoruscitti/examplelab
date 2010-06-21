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
        width, height = gaphas.util.text_extents(cr, text)
        p = 10  # padding

        # draw background
        if context.focused:
            cr.set_source_rgb(0.9, 0.9, 1)
        elif context.hovered:
            cr.set_source_rgb(0.9, 1, 0.9)
        else:
            cr.set_source_rgb(1, 1, 1)

        cr.rectangle(0 - p, 0 -p, width + p * 2, height + p * 2)
        cr.fill()

        # draw text
        cr.set_source_rgb(0, 0, 0)
        gaphas.util.text_align(cr, 0, 0, text, 1, 1)

        # draw border
        if context.selected:
            cr.set_source_rgb(0, 0, 1)
        else:
            cr.set_source_rgb(0, 0, 0)

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


box2 = BoxWithText()
box2.matrix.translate(50, 50)
canvas.add(box2)

window.show_all()
gtk.main()

import gtk
import gaphas
import gaphas.examples

class CustomText(gaphas.examples.Text):

    def __init__(self, *k, **v):
        gaphas.examples.Text.__init__(self, *k, **v)

    def draw(self, context):
        cr = context.cairo
        cr.set_source_rgba(0, .5, 0, 1)
        gaphas.util.text_set_font(cr, 'sans bold 20')
        gaphas.examples.Text.draw(self, context)


window = gtk.Window()
window.connect('destroy', gtk.main_quit)

canvas = gaphas.Canvas()
view = gaphas.GtkView()
view.canvas = canvas
window.add(view)

simple_text = gaphas.examples.Text("Simple text.")
simple_text.matrix.translate(30, 50)
canvas.add(simple_text)

message = "This\ntext\nhas\nmany\nlines"
multiline_text = gaphas.examples.Text(message, multiline=True)
multiline_text.matrix.translate(30, 100)
canvas.add(multiline_text)

custom_text = CustomText("This is a custom text")
custom_text.matrix.translate(30, 70)
canvas.add(custom_text)



window.show_all()
gtk.main()

import gtk
import cairo

class Canvas(gtk.DrawingArea):

    def __init__(self):
        gtk.DrawingArea.__init__(self)
        self.connect('expose_event', self.on_event)
        self._name = "Object"
        self.attributes = ["name", "id"]
        self.methods = ["method()", "other_method()"]

    def on_event(self, widget, event):
        """Actualiza todo el area del widget.

        NOTA: hay formas de optimizar esto, ver en [1]."""

        self.context = widget.window.cairo_create()
        allocation = self.get_allocation()
        self.draw(self.context)

        self.queue_draw_area(0, 0, allocation.width, allocation.height)
        return False

    def draw(self, cr):
        # pinta el fondo blanco
        cr.set_source_rgb(1, 1, 1)
        cr.rectangle(50, 30, 100, 150)
        cr.fill()

        # titulo
        cr.set_font_size(14)
        cr.select_font_face("Georgia", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        cr.set_source_rgb(0, 0, 0)
        cr.move_to(75, 50)
        cr.show_text(self._name)

        # nombre de atributos
        cr.select_font_face("Georgia", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
        cr.move_to(60, 80)

        for item in self.attributes:
            cr.rel_move_to(0, 10)
            cr.show_text(item)

        # pinta el borde
        cr.set_source_rgb(0, 0, 0)
        cr.set_line_width(2)
        cr.rectangle(50, 30, 100, 150)
        cr.stroke()



window = gtk.Window()
window.set_position('center')
window.add(Canvas())
window.show_all()
window.connect('destroy', gtk.main_quit)

gtk.main()


# Referencias:
# ------------
#
# 1 = www.pygtk.org/articles/cairo-pygtk-widgets/cairo-pygtk-widgets.htm

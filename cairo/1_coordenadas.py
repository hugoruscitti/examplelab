import gtk

class Canvas(gtk.DrawingArea):

    def __init__(self):
        gtk.DrawingArea.__init__(self)
        self.connect('expose_event', self.on_event)

    def on_event(self, widget, event):
        """Actualiza todo el area del widget.

        NOTA: hay formas de optimizar esto, ver en [1]."""

        self.context = widget.window.cairo_create()
        allocation = self.get_allocation()
        self.draw(self.context)
        self.queue_draw_area(0, 0, allocation.width, allocation.height)
        return False

    def draw(self, cr):
        cr.move_to(80, 30)
        cr.show_text("a = (80, 30)")

        cr.set_source_rgb(0, 0.6, 0)
        cr.move_to(100, 100)
        cr.show_text("b = (100, 100)")


window = gtk.Window()
window.set_position('center')
window.add(Canvas())
window.show_all()
window.connect('destroy', gtk.main_quit)

gtk.main()

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

        self.queue_draw_area(0, 0, allocation.width, allocation.height)
        return False



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

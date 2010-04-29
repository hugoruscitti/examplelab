import gtk, gobject
from PySFML import sf

class SFMLWidget(gtk.DrawingArea):
    def __init__(self):
        gtk.DrawingArea.__init__(self)
        self.connect("realize",self.realize)
        self.connect("unrealize",self.unrealize)
    def realize(self, event):
        self.set_double_buffered(False)
        self.sfml_canvas = sf.RenderWindow(self.window.xid)
    def unrealize(self,event):
        self.sfml_canvas.Close()


def main():
    window = gtk.Window()
    widget = SFMLWidget()

    window.add(widget)
    window.connect("destroy", gtk.main_quit)
    window.show_all()
    def display():
        print "Display"
        widget.sfml_canvas.Clear()
        widget.sfml_canvas.Display()
        return True
    display_tag = gobject.timeout_add(5,display)

    gtk.main()

if __name__ == "__main__":
    main()

import gobject
gobject.threads_init()
import pygtk
pygtk.require("2.0")
import gtk
import goocanvas
from goocanvashelper import *
 

c = goocanvas.Canvas()

factory = (
    goocanvas.Rect,
    {
        "width" : 30,
        "height" : 30,
        "stroke_color" : "black",
        "fill_color" : "green"
    },
    {
        "normal" : "green",
        "active" : "red",
    }
)
def changed_cb(selected, deselected):
    for item in selected:
        item.props.fill_color = item.get_data("active")
    for item in deselected:
        item.props.fill_color = item.get_data("normal")
 
marquee = goocanvas.Rect(stroke_color = "black")
manage_selection(c, marquee, True, changed_cb)
for x in xrange(0, 5):
    i = make_item(factory)
    set_pos(i, (x * 40, x * 40))
    make_selectable(c, i)
    make_dragable(c, i)
    c.get_root_item().add_child(i)

 

# end demo
w = gtk.Window()
w.add(c)
w.show_all()
w.connect("destroy", gtk.main_quit)
gtk.main()


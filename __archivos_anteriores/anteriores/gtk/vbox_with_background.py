import gtk

window = gtk.Window()
window.set_title("Ejemplo")
window.set_position('center')
window.show()

# Load image
pixbuffer = gtk.gdk.pixbuf_new_from_file('image.png')
pixmap, mask = pixbuffer.render_pixmap_and_mask()

# Set background
window.set_app_paintable(True)

vbox = gtk.VBox()

button = gtk.Button("text")
button.show()

other_vbox = gtk.VBox()
other_vbox.show()

vbox.add(button)
vbox.add(other_vbox)
vbox.set_border_width(10)
vbox.set_spacing(20)

other_vbox.set_border_width(20)


b = gtk.Button("in")
b.show()
other_vbox.add(b)


window.add(vbox)


window.connect('destroy', gtk.main_quit)
window.show_all()

other_vbox.set_app_paintable(True)

style = other_vbox.get_style()
style = style.copy()
#stylebg_color(gtk.STATE_NORMAL, pixmap)

other_vbox.set_style(style)

#.window.set_back_pixmap(pixmap, False)
gtk.main()

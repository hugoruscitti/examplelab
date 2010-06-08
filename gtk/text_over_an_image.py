import gtk

window = gtk.Window()
window.set_title("Ejemplo")
window.set_position('center')
window.show()

# Load image
pixbuffer = gtk.gdk.pixbuf_new_from_file('background.png')
pixmap, mask = pixbuffer.render_pixmap_and_mask()

# Set background
window.set_app_paintable(True)
window.window.set_back_pixmap(pixmap, False)


vbox = gtk.VBox()

text = gtk.Label()
text.set_markup("<b>Texto</b> de ejemplo\ncon saltos de linea.")
vbox.add(text)

image = gtk.Image()
image.set_from_file('image.png')
vbox.add(image)

window.add(vbox)

window.connect('destroy', gtk.main_quit)
window.show_all()

gtk.main()

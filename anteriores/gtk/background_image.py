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
window.window.set_back_pixmap(pixmap, False)

window.connect('destroy', gtk.main_quit)
window.show_all()

gtk.main()

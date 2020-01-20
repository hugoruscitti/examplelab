import gtk

window = gtk.Window()
window.set_position('center')
image = gtk.Image()
image.set_from_file('image.png')

window.add(image)
window.show_all()

window.connect('destroy', gtk.main_quit)

gtk.main()

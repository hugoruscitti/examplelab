import gtk

window = gtk.Window()

label = gtk.Label()
label.set_line_wrap(True)
label.set_justify('center')
label.set_size_request(100, 200)
label.set_markup("Este es un texto de <b>Prueba</b>, usando una sola linea")

window.add(label)
window.connect("destroy", gtk.main_quit)
window.show_all()

gtk.main()

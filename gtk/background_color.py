import gtk
window = gtk.Window(gtk.WINDOW_TOPLEVEL)
window.connect("destroy", gtk.mainquit)
label = gtk.Label("one, two, testing...")
eb = gtk.EventBox()
eb.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse("blue"))

window.add(eb)
window.show_all()
gtk.main()


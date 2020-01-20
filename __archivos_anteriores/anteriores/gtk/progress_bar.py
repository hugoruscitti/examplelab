import gobject
import gtk
import gtk.glade

def add(progress_bar):
    value = progress_bar.get_fraction()

    if value < 1:
        value += 0.1
        progress_bar.set_fraction(value)
    else:
        print "Termina de completar la barra."
        return False

    return True



ui = gtk.glade.XML('loading.glade')

loading = ui.get_widget('loading')
loading.show()
loading.connect('destroy', gtk.main_quit)

progress_bar = ui.get_widget('progress')
gobject.timeout_add(1000, add, progress_bar)

gtk.main()

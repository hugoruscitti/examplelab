import gtk
import gobject

def update(label):
    text = label.get_text()
    text += '.'
    label.set_text(text)
    return True             # Retornar True para que se repita constantemente

window = gtk.Window()
window.connect('destroy', gtk.main_quit)

label = gtk.Label()
label.set_text("Contando ")
label.set_size_request(200, 100)
window.add(label)
window.set_position('center')

gobject.timeout_add(1000, update, label)

window.show_all()
gtk.main()

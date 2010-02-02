import gtk

window = gtk.Window()
window.set_position('center')

# create list
list = gtk.TreeView()
model = gtk.ListStore(str, str, bool)
list.set_model(model)

id = gtk.TreeViewColumn('ID', gtk.CellRendererText(), text=0)
name = gtk.TreeViewColumn('Name', gtk.CellRendererText(), text=1)
b = gtk.TreeViewColumn('Boolean', gtk.CellRendererToggle())


list.append_column(id)
list.append_column(name)
list.append_column(b)

model.append(("102", "hola", True))
model.append(("102", "chau", False))
model.append(("102", "chau", False))
model.append(("102", "chau", False))
model.append(("102", "chau", False))
model.append(("102", "chau", False))
model.append(("102", "chau", False))



# show window
window.add(list)
window.connect("destroy", gtk.main_quit)
window.show_all()

gtk.main()

from threading import Thread
import gtk
import gobject

gobject.threads_init()

class Application(Thread):

    def __init__(self, environment):
        Thread.__init__(self)
        self.environment = environment

    def _create_window(self):
        window = gtk.Window()
        window.set_position(gtk.WIN_POS_CENTER)
        window.connect('destroy', gtk.main_quit)
        window.show()
        self.window = window

    def run(self):
        self._create_window()
        gtk.main()

def show(environment):
    app = Application(environment)
    app.start()
    print "He creado el hilo."

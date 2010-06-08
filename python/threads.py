import time
from threading import Thread
import gtk

gtk.gdk.threads_init()

class Hilo(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.killed = False

    def run(self):
        while True:
            print "Soy un hilo."
            time.sleep(1)

            if self.killed:
                return True

    def kill(self):
        self.killed = True

if __name__ == '__main__':
    hilo = Hilo()
    hilo.start()

    try:
        print "Soy el proceso padre y espero 4 segundos."
        time.sleep(4)
    except KeyboardInterrupt:
        print "Ha interrumpido el proceso."

    print "Soy el proceso padre y termino ambos hilos."
    hilo.kill()

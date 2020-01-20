import threading
import sys
import cmd
import Queue

import pyglet
import cocos


def environment(queue, sprite):
    """Representa la session y las variables locales de la instancia interactiva.

    Este entorno funciona como un generador, con la intension de guardar
    el estado de todas las variables locales y acceder a los comandos desde
    la cola."""

    while True:

        try:
            last = queue.get_nowait()

            if last:
                try:
                    exec(last)
                except:
                    print "Error al ejecutar", last

        except Queue.Empty:
            pass

        yield None


class Application(threading.Thread):

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.killed = False
        self.queue = queue

    def run(self):
        cocos.director.director.init(resizable=False, width=800, height=600)
        self.scene = cocos.scene.Scene(cocos.layer.ColorLayer(240, 240, 240, 255))
        sprite = cocos.sprite.Sprite('cara.png')
        sprite.scale = 2
        sprite.x = 400
        sprite.y = 300
        self.scene.add(sprite)

        # Genera el entorno de la session, y le pasa datos que puede
        # manipular.
        self.environment = environment(queue, sprite)
        self.environment.next()

        self.scene.schedule_interval(self.environment_update, 0.01)
        cocos.director.director.run(self.scene)

    def environment_update(self, dt):
        "Mantiene en funcionamiento."
        self.environment.next()

    def kill(self):
        self.killed = True
        pyglet.app.exit()


class CommandLine(cmd.Cmd):

    def __init__(self, app, queue):
        cmd.Cmd.__init__(self, 'TAB')
        self.queue = queue
        self.app = app
        self.prompt = ">>> "

    def default(self, line):
        "Cualquier sentencia la envia a la cola de comandos que consume cocos."
        self.queue.put(line)

    def do_exit(self, line):
        self.app.kill()
        sys.exit(0)



# Cola de mensajes que se utiliza para llevar comandos al hilo.
queue = Queue.Queue()

# Hilo que ejecuta la funcionalidad de cocos.
app = Application(queue)
app.start()

# Interprete de comandos que envia todas las lineas que se escriben
# directamente a la cola de mensajes que consume el hilo.
cmd = CommandLine(app, queue)
cmd.cmdloop()

import threading
from PySFML import sf
import time
import atexit


def do(code, delay=0.001):
    """Run a list of code lines.

    example::

        >>> steps = ['sprite.Move(10, 10)', 'sprite.SetScale(2, 2)']
        >>> do(steps)
    """

    def do_and_pause(a_line_of_code):
        eval(a_line_of_code)
        time.sleep(delay)

    map(do_and_pause, code)

def repeat(code, times=100, delay=0.001):
    "Eval a single code string a number of times."

    for x in range(times):
        eval(code)
        time.sleep(delay)


class InteractiveRenderWindow(threading.Thread, sf.RenderWindow):
    "Creates an independent RenderWindow for interactive learning."

    def __init__(self, *k, **vk):
        threading.Thread.__init__(self)
        sf.RenderWindow.__init__(self, *k, **vk)
        self.video_mode = sf.VideoMode(400, 340)

        self.must_stop = False
        self.drawables = []

    def run(self):
        self.Create(self.video_mode, "Interactive Window")
        event = sf.Event()

        while not self.must_stop:

            while self.GetEvent(event):
                if event.Type == sf.Event.Closed:
                    self.stop()
                    return

            self.Clear(sf.Color(200, 200, 200))
            self.Draw(self.drawables)
            self.Display()

    def stop(self):
        if self.isAlive():
            self.must_stop = True
            self.Close()

    def add(self, drawable):
        self.drawables.append(drawable)

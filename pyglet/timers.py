import pyglet

def program_start(dt):
    print "Hello, program starting."

def tick(dt):
    print "Tick (every 2 seconds), has dt =", dt

pyglet.clock.schedule_once(program_start, 1)
pyglet.clock.schedule_interval(tick, 2)
#pyglet.clock.unschedule(tick)

pyglet.app.run()

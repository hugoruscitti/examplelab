from PySFML import sf
import sys

app = sf.Window()
app.Create(sf.VideoMode(640, 480), "Simple")

# Es el contenedor del evento.
event = sf.Event()
input = app.GetInput()

clock = sf.Clock()

# Por defecto parece que viene con False.
app.UseVerticalSync(True)


# Se puede usar 'app.IsOpened()'
while True:
    #dt = clock.GetElapsedTime()
    #clock.Reset()
    dt = app.GetFrameTime()


    # Retorna true si existe un evento para atender
    while app.GetEvent(event):

        mouse = input.GetMouseX(), input.GetMouseY()
        print mouse

        if event.Type == sf.Event.KeyPressed:
            if event.Key.Code == sf.Key.Escape:
                app.Close()
                sys.exit(0)

    app.Display()

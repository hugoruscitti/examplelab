from PySFML import sf
import sys

app = sf.Window()
app.Create(sf.VideoMode(640, 480), "Simple")

# Es el contenedor del evento.
event = sf.Event()

while True:

    # Retorna true si existe un evento para atender
    while app.GetEvent(event):

        if event.Type == sf.Event.Closed:
            app.Close()
            sys.exit(0)
        elif event.Type == sf.Event.KeyPressed:

            # Quita la aplicacion cuando pulsan la tecla escape
            if event.Key.Code == sf.Key.Escape:
                app.Close()
                sys.exit(0)

    app.Display()

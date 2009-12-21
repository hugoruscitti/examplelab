from PySFML import sf
import sys

app = sf.RenderWindow()
app.Create(sf.VideoMode(640, 480), "Simple")

# Es el contenedor del evento.
event = sf.Event()
input = app.GetInput()

clock = sf.Clock()

# Por defecto parece que viene con False.
app.UseVerticalSync(True)

color = sf.Color(200, 200, 200)


image = sf.Image()
image.LoadFromFile('image.png')


sprite = sf.Sprite(image)
sprite.SetCenter(100, 100)

sprite.Move(200, 200)
# El ultimo parametro del color es la opacidad
circle = sf.Shape.Circle(200, 200, 100, sf.Color(0, 0, 0, 90), 2, 
        sf.Color(200, 0, 0, 128))



#view = app.GetView()
#view.Zoom(1.5)
#app.SetView(view)

# Se puede usar 'app.IsOpened()'
while True:
    app.Clear(color)
    dt = app.GetFrameTime()


    #sprite.Rotate(100 * dt)
    

    app.Draw(sprite)
    app.Draw(circle)
    #dt = clock.GetElapsedTime()
    #clock.Reset()


    # Retorna true si existe un evento para atender
    while app.GetEvent(event):

        x = input.GetMouseX()
        y = input.GetMouseY()

        sprite.SetX(x)
        sprite.SetY(y)

        if event.Type == sf.Event.KeyPressed:
            if event.Key.Code == sf.Key.Escape:
                app.Close()
                sys.exit(0)

    app.Display()

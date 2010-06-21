# -*- encoding: utf-8 -*-
from PySFML import sf
import sys

app = sf.RenderWindow()
app.Create(sf.VideoMode(640, 480), "Simple")

# Es el contenedor del evento.
event = sf.Event()
input = app.GetInput()

font = sf.Font()
#font.LoadFromFile("")

# ¡
text = sf.String("¡á Hola ")
text.SetColor( sf.Color(0, 200, 0))


sf.PostFX.CanUsePostFX()

color = sf.Color(200, 200, 200)

while True:
    app.Clear(color)
    app.Draw(text)



    # Retorna true si existe un evento para atender
    while app.GetEvent(event):

        x = input.GetMouseX()
        y = input.GetMouseY()


        if event.Type == sf.Event.KeyPressed:
            if event.Key.Code == sf.Key.Escape:
                app.Close()
                sys.exit(0)

    app.Display()

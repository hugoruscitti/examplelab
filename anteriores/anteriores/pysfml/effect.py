# -*- encoding: utf-8 -*-
from PySFML import sf
import sys

app = sf.RenderWindow()
app.Create(sf.VideoMode(640, 480), "Simple")

# Es el contenedor del evento.
event = sf.Event()
input = app.GetInput()


image = sf.Image()
image.LoadFromFile('image.png')

sprite = sf.Sprite(image)



sf.PostFX.CanUsePostFX()
effect = sf.PostFX()
effect.LoadFromFile('colorize.sfx')

color = sf.Color(200, 200, 200)

effect.SetTexture("framebuffer", None)
effect.SetParameter("color", 1, 1, 1)

while True:
    app.Clear(color)

    app.Draw(sprite)
    app.Draw(effect)


    # Retorna true si existe un evento para atender
    while app.GetEvent(event):

        x = input.GetMouseX()
        y = input.GetMouseY()

        new_x = x / float(app.GetWidth())
        new_y = y / float(app.GetHeight())

        effect.SetParameter("color", 0.5, new_x, new_y)

        sprite.SetX(x)
        sprite.SetY(y)


        if event.Type == sf.Event.KeyPressed:
            if event.Key.Code == sf.Key.Escape:
                app.Close()
                sys.exit(0)

    app.Display()

# License: Public Domain
# Author: Hugo Ruscitti (http://www.losersjuegos.com.ar)
# Art resources: Walter Velazquez (GPLv2) 

from PySFML import sf
import sys
import sheet

app = sf.RenderWindow()
app.Create(sf.VideoMode(640, 480), "SpriteSheet")

event = sf.Event()
bgcolor = sf.Color(150, 150, 150)

image = sf.Image()
image.LoadFromFile('chanta_running.png')

sprite = sf.Sprite(image)
sprite.Move(200, 200)

other_sprite = sf.Sprite(image)
other_sprite.Move(400, 100)
other_sprite.Scale(2, 2)

sheet = sheet.ImageSheet(image, rows=1, cols=13)
dt = 0
delay = 1/20.0

while True:
    sheet.Assign(sprite)
    sheet.Assign(other_sprite)

    dt += app.GetFrameTime()

    # Advance 20 frames per second (aprox.)
    if dt > delay:
        dt -= delay
        sheet.NextFrame()



    while app.GetEvent(event):
        if event.Type == sf.Event.Closed:
            app.Close()
            sys.exit(0)

    app.Clear(bgcolor)
    app.Draw(sprite)
    app.Draw(other_sprite)

    app.Display()

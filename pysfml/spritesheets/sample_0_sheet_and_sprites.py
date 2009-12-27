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
image.LoadFromFile('pingu.png')

sprite = sf.Sprite(image)
sprite.Scale(0.5, 0.5)
sprite.Move(90, 0)

sprite_1 = sf.Sprite(image)
sprite_1.Move(120, 160)

sprite_2 = sf.Sprite(image)
sprite_2.Move(400, 160)
sprite_2.FlipX(True)

sheet = sheet.ImageSheet(image, rows=1, cols=10)

sheet.SetFrameIndex(0)
sheet.Assign(sprite_1)

sheet.SetFrameIndex(1)
sheet.Assign(sprite_2)

string_for_sprite = sf.String("Sprite with original image (scale 0.5)")
string_for_sprite.SetSize(20)
string_for_sprite.SetPosition(150, 70)

string_for_sprite_1 = sf.String("Sprite showing frame 0")
string_for_sprite_1.SetSize(20)
string_for_sprite_1.SetPosition(60, 300)

string_for_sprite_2 = sf.String("Sprite showing frame 1\n(and flipped)")
string_for_sprite_2.SetSize(20)
string_for_sprite_2.SetPosition(350, 300)


while True:
    app.Clear(bgcolor)

    app.Draw(sprite_1)
    app.Draw(sprite_2)
    app.Draw(sprite)

    app.Draw(string_for_sprite)
    app.Draw(string_for_sprite_1)
    app.Draw(string_for_sprite_2)


    while app.GetEvent(event):
        if event.Type == sf.Event.Closed:
            app.Close()
            sys.exit(0)



    app.Display()

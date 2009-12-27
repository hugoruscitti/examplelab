# License: Public Domain
# Author: Hugo Ruscitti (http://www.losersjuegos.com.ar)
# Art resources: Walter Velazquez (GPLv2) 

from PySFML import sf
import sys
from sheet import ImageSheet

app = sf.RenderWindow()
app.Create(sf.VideoMode(640, 480), "SpriteSheet")

event = sf.Event()
bgcolor = sf.Color(150, 150, 150)

image = sf.Image()
image.LoadFromFile('pingu.png')

sprite = sf.Sprite(image)
sprite.Move(100, 100)

sheet = ImageSheet(image, rows=1, cols=10)
sheet.Assign(sprite)

message = sf.String("Use space key to change to the next frame.")
frame_message = sf.String("Showing frame 0")
frame_message.Move(0, 40)


while True:
    app.Clear(bgcolor)

    app.Draw(sprite)
    app.Draw(message)
    app.Draw(frame_message)

    while app.GetEvent(event):

        if event.Type == sf.Event.KeyPressed:
            if event.Key.Code == sf.Key.Space:
                has_restarted = sheet.NextFrame()
                sheet.Assign(sprite)
                frame_message.SetText("Showing frame %s" %(sheet.GetFrameIndex()))

                if has_restarted:
                    last_text = frame_message.GetText()
                    frame_message.SetText(last_text + " (has restarted)")

        elif event.Type == sf.Event.Closed:
            app.Close()
            sys.exit(0)

    app.Display()

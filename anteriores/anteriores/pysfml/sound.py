# -*- encoding: utf-8 -*-
from PySFML import sf
import sys

app = sf.RenderWindow()
app.Create(sf.VideoMode(640, 480), "Simple")

# Es el contenedor del evento.
event = sf.Event()
input = app.GetInput()


buffer = sf.SoundBuffer()
buffer.LoadFromFile("knock.wav")


sound = sf.Sound()
sound.SetBuffer(buffer)
sound.Play()

color = sf.Color(200, 200, 200)

playing_music = False
message = sf.String("Press Space to start Music or click for sound.")

while True:
    app.Clear(color)
    app.Draw(message)

    # Retorna true si existe un evento para atender
    while app.GetEvent(event):

        x = input.GetMouseX()
        y = input.GetMouseY()


        if event.Type == sf.Event.KeyPressed:
            if event.Key.Code == sf.Key.Escape:
                app.Close()
                sys.exit(0)
            elif event.Key.Code == sf.Key.Space:
                playing_music = True
                message.SetText("ok, well done, i'm playing music...")

                music = sf.Music()
                music.OpenFromFile('otro.ogg')

                music.Play()
        elif event.Type == sf.Event.MouseButtonPressed:
            sound.Play()

    app.Display()

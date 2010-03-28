# -*- encoding: utf-8 -*-
from PySFML import sf
import sys


class MenuTextSprite(sf.String):

    def __init__(self, text, x, y):
        sf.String.__init__(self, text)
        self.default_color = sf.Color(200, 200, 200)
        self.over_color = sf.Color.White
        self.SetColor(self.default_color)
        self.SetPosition(x, y)
        self.my_rect = self.GetRect()

    def on_mouse_move_event(self, mouse_move_event):
        x, y = mouse_move_event.X, mouse_move_event.Y

        # Check if the mouse are over my.
        if self.my_rect.Contains(x, y):
            self.SetColor(self.over_color)
        else:
            self.SetColor(self.default_color)



app = sf.RenderWindow()
app.Create(sf.VideoMode(320, 240), "Menu")



#create all text items

new_game_text = MenuTextSprite("New Game", 80, 50)
about_text = MenuTextSprite("About this game", 50, 100)
quit_text = MenuTextSprite("Quit", 120, 150)

menu_items_list = [new_game_text, about_text, quit_text]


event = sf.Event()
input = app.GetInput()

background_color = sf.Color(100, 100, 100)

while True:
    app.Clear(background_color)

    for text_item in menu_items_list:
        app.Draw(text_item)

    while app.GetEvent(event):

        x = input.GetMouseX()
        y = input.GetMouseY()

        if event.Type == sf.Event.Closed:
            app.Close()
            sys.exit(0)


        if event.Type == sf.Event.MouseMoved:
            for text_item in menu_items_list:
                text_item.on_mouse_move_event(event.MouseMove)


    app.Display()

# -*- encoding: utf-8 -*-
import pyglet
import cocos
from cocos.actions import *
from cocos.director import director

SMALL, NORMAL, LARGE = 0.9, 1, 1.3

class Image(cocos.sprite.ActionSprite):

    def __init__(self, image_path):
        image = pyglet.resource.image(image_path)
        cocos.sprite.ActionSprite.__init__(self, image)
        self._set_initial_state()

    def _set_initial_state(self):
        self.state = -1
        self.scale = SMALL
        self.set_hover_state(0, inmediate=True)

    def set_hover_state(self, state, inmediate=False):
        """Define el grado de selección:

            @state: 0 no seleccionado, 1 seleccionado previamente, 2 seleccionado.
        """
        if self.state != state:
            sizes = [SMALL, NORMAL, LARGE]
            opacity = [128, 180, 255]
            duration = 0.2
            self.opacity = opacity[state]

            if not inmediate:
                action = ScaleTo(sizes[state], duration=duration) 
                self.do(action)

            self.state = state

    def includes(self, x, y):
        my_width = self.image.width
        my_height = self.image.height
        my_x = self.x - my_width / 2
        my_y = self.y - my_height / 2

        if my_x < x < my_x + my_width:
            if my_y < y < my_y + my_height:
                return True

class Menu(cocos.layer.Layer):

    def __init__(self, x, y, align='top'):
        cocos.layer.Layer.__init__(self)
        self.items = self._create_items(x, y, align)
        self._select_first_item()

    def _create_items(self, x, y, align):
        "Genera todos los elementos del menú."
        items = [
                Image('images.png'),
                Image('images.png'),
                Image('games.png'),
                Image('games.png'),
                Image('games.png'),
                ]

        height = items[0].height

        if align == 'top':
            pass
        else:
            print "Error: Valor de 'align' no válido."

        for index, item in enumerate(items):
            item.position = (x, y - (index * height))
            self.add(item)

        return items

    def _select_first_item(self):
        "Define como seleccionado al primer elemento de la lista."
        first_item = self.items[0]
        self.on_pointer_motion(first_item.x, first_item.y)

    def on_pointer_motion(self, x, y):
        "Simula el evento de movimiento de puntero."
        x, y = director.get_virtual_coordinates(x, y)

        for index, item in enumerate(self.items):
            if item.includes(x, y):
                self._set_hover(index)

    def _set_hover(self, index):
        "Define el elemento actual."
        self.items[index].set_hover_state(2)

        try:
            if index > 0:
                self.items[index - 1].set_hover_state(1)
                self.items[index - 2].set_hover_state(0)
        except IndexError:
            pass

        try:
            self.items[index + 1].set_hover_state(1)
            self.items[index + 2].set_hover_state(0)
        except IndexError:
            pass

        self.actual_index = index
                
    def on_mouse_motion(self, x, y, dx, dy):
        self.on_pointer_motion(x, y)


if __name__ == '__main__':
    cocos.director.director.init(resizable=True)

    menu = Menu(320, 300)
    scene = cocos.scene.Scene(menu)
    cocos.director.director.run(scene)

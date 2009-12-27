#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gimpfu import *

def to_sheet(image, drawable):
    dx = 0

    frame_width, frame_height = image.width, image.height
    number_of_layers = len(image.layers)

    image.undo_group_start()

    # Move layers in sheet
    for layer in image.layers:
        layer.resize(frame_width, frame_height, 0, 0)
        layer.set_offsets(dx, 0)
        dx += frame_width

    image.resize(frame_width * number_of_layers, frame_height, 0, 0)
    image.undo_group_end()

if __name__ == '__main__':
    register(
            "redimensionar_imagen",
            "Redimensionar imagen",
            "Redimensionar imagen",
            "Hugo Ruscitti",
            "Hugo Ruscitti",
            "2008",
            "<Image>/Python-Fu/Sprite/Create sheet",
            "RGB*, GRAY*",
            [],
            [],
            to_sheet)
    main()

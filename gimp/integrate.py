#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gimpfu import *

def integrate(image, drawable, frames):
    new_width = image.width / frames
    image.undo_group_start()

    # Move layers in sheet
    for layer in image.layers:
        layer.set_offsets(0, 0)

    image.resize(new_width, image.height, 0, 0)
    image.undo_group_end()

if __name__ == '__main__':
    register(
            "integrate",
            "Integrate sprites",
            "Integrate sprites",
            "Hugo Ruscitti",
            "Hugo Ruscitti",
            "2008",
            "<Image>/Python-Fu/Sprite/Integrate",
            "RGB*, GRAY*",
            [
                (PF_SPINNER, "frames", "Frames", 2, (0, 50, 1)),
            ],
            [],
            integrate)
    main()

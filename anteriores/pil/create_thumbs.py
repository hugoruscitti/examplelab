#!/usr/bin/python
# -*- encoding: utf-8 -*-

import Image
import os

# Tamaño horizontal o vertical.
SIZE = 80

files = [x for x in os.listdir('./')
            if os.path.isfile(x)
            if 'png' in x or 'jpg' in x
            if not '_thumb' in x
            ]

for file in files:
    image = Image.open(file)
    image.thumbnail((SIZE, SIZE), Image.ANTIALIAS)


    name_without_extension = os.path.splitext(file)[0]
    extension = os.path.splitext(file)[1]
    new_name = name_without_extension + "_thumb.png"

    image.save(new_name)
    print "Creating %s" %(new_name)

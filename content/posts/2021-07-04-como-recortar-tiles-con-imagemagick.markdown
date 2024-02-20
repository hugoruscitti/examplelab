---
layout: post
title: Cómo recortar tiles con ImageMagick
date: '2021-07-04 00:00:00'
description: |
  Una lista de comandos y ejemplos para convertir grillas de imágenes en archivos individuales.
cover: /images/2021/como-recortar-tiles-con-imagemagick/portada.jpg
tags:
- imágenes
---

[ImageMagick](https://imagemagick.org/script/index.php) es un conjunto de herramientas que te permiten procesar imágenes
de muchas formas diferentes. Además, se usa a través de la linea de comandos lo
que permite automatizar y procesar muchas imágenes a la vez.


Por ejemplo, algo que necesito hacer muy seguido es tomar una
grilla de *sprites* y dividirla en archivos de imágenes individuales.

Las grillas (o tiles) son muy eficientes, pero no son nada
prácticos a la hora de hacer pruebas o escoger imágenes para
un juego.

Tomemos esta imagen como ejemplo:

![](/images/2021/como-recortar-tiles-con-imagemagick/tiles.png)

La grilla tiene 4 columnas y 7 filas de imágenes, si queremos
separar cada una de estas imágenes podemos ejecutar este
comando:

```
convert SpriteSheet.png -crop 4x7@  +repage  +adjoin  resultado/imagen_%d.png
```

Y lo que vamos a obtener como resultado son varias imágenes como
estas:


![](/images/2021/como-recortar-tiles-con-imagemagick/imagenes.png)


# Evitando bordes

Hay un bug muy común a la hora de usar estas imágenes en un
juego que requiere algo de atención:

Si usamos las imágenes del ejemplo anterior es probable que veamos
un borde raro en cada imagen:

![](/images/2021/como-recortar-tiles-con-imagemagick/bordes.png)

Esto es así porque en memoria de la placa de video las imágenes
se almacenan de forma contigua, y las operaciones de suavizado
suelen hacer que los píxeles de los bordes aparezcan recortados o
como si se mezclaran entre sí.

La solución es muy simple, podemos usar otro comando de [ImageMagick](https://imagemagick.org/script/index.php)
para agregar 2 píxeles transparentes al rededor de cada imagen
y listo:

```
mogrify -bordercolor none -border 2 resultado/*
```

Con esto, los archivos deberían quedarnos de esta forma:

![](/images/2021/como-recortar-tiles-con-imagemagick/padding.png)

Es decir, un poco más grandes (20x20 píxeles), pero sin el defecto
del borde cuando lo usamos dentro de un juego:

![](/images/2021/como-recortar-tiles-con-imagemagick/modos.png)


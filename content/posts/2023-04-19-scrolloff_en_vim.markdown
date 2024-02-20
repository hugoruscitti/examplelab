---
layout: post
title: ¿Para qué sirve scrolloff en vim?
date: '2023-04-19 00:00:00'
description: |
 Explico una configuración de vim para ajustar el
 desplazamiento de pantalla.
cover: /images/2023/scrolloff_en_vim/portada.jpg
tags:
- vim
---

Imaginá que buscas una linea de código en un archivo muy
grande, pero usando una pantalla pequeña que solo te permite
ver una parte del archivo.

Podrías mover el cursor hasta esa linea y quedarte en esa
posición, el area visible del editor va a "acompañar" el
movimiento del mouse para que siempre quede en pantalla así:

![](/images/2023/scrolloff_en_vim/scrolloff-0.png)


El problema es que generalmente nos interesa ver qué hay
debajo y arriba de esa palabra, es decir, el contexto de lo
que estamos buscando.

Cuando esto sucede nos toca mover el cursor hacia abajo y
arriba para desplazar la pantalla o usar el mouse para
desplazar el area visible. Algo molesto realmente, porque
tenemos que hacer movimientos innecesarios con el cursor
solamente para "ver el contexto" de dónde estamos dentro del
documento.

Bueno, por suerte Vim tiene un parámetro de configuración
para resolver este problema fácilmente:


```
set scrolloff=4
```

Con este parámetro, Vim va a intentar mantener al cursor en
pantalla dejando 4 lineas visibles hacia arriba y abajo en
todo momento:

![](/images/2023/scrolloff_en_vim/scrolloff-4.png)

Es un detalle pequeño, pero tener contexto de la linea del
editor me da comodidad instantanea todos los días :)

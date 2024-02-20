---
layout: post
title: Portapapeles en VIM
date: '2021-02-22 00:00:00'
description: |
  Un pequeño consejo para copiar y pegar entre
  VIM y el portapapeles del sistema operativo.
cover: /images/2021/portapapeles-en-vim/portada.jpg
tags:
- vim
---

VIM tiene un sistema de portapapeles propio, independiente del sistema.

Esto nos permite tener múltiples portapapeles dentro de VIM y algo de
independencia con el resto del sistema.

Sin embargo, muchas veces me pasa que quiero copiar y pegar texto
entre distintas aplicaciones, y VIM es un poquito incómodo a la hora de hacer
estas cosas.

Resulta que VIM gestiona todo lo que copiamos o pegamos en registros nombrados. Así
que para acceder al portapapeles del sistema tenemos que anteponer un nombre
de registro a cada operación de copiado y pegado.

Siendo más específico, si queremos copiar algo al portapapeles del sistema tenemos que pulsar
`+"y` en lugar de `y` y para pegar `+"p` en lugar de `p`.

Por suerte VIM se puede configurar como queramos. A mí me resultaba muy incómodo
anteponer ese nombre a cada operación, así que añadí estas dos lineas de
configuración a mi archivo `.vimrc`:

```
vnoremap <S-y> "+y
map <S-p> "+gP
```

Con esta configuración, se vuelve mucho más directo copiar y pegar al portapapeles del
sistema. Con `shift-y` en modo visual "copiamos" el texto de VIM en
el portapapeles del sistema y con `shift-p` en modo normal "pegamos" dentro de
VIM lo que tengamos en el portapapeles del sistema.

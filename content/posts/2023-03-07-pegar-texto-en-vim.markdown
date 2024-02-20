---
layout: post
title: ¿Cómo pegar texto en vim?
date: '2023-03-07 00:00:00'
description: |
  Vim puede recibir texto del portapapeles, pero te puede
  hacer un lío con las indentaciones.
cover: /images/2023/pegar-texto-en-vim/portada.jpg
tags:
- vim
---

Pegar texto en Vim debería ser algo sencillo, pero a veces
da problemas.

Por ejemplo, si copias código del navegador y luego intentas
pegarlo dentro del editor puede pasar algo como esto:

![](/images/2023/pegar-texto-en-vim/editor.png)

El problema es que Vim no reconoce que estamos pegando
texto, sino que cree que estamos escribiendo ese texto poco
a poco, así que intenta agregar indentaciones mientras va
pegando cada una de las lineas.

Una forma de resolver esto activar y desactivar el indentado
cuando estamos por pegar texto:

```
:set paste
CTRL+V # para pegar el texto
:set nopaste
```

Sin embargo, hay una forma mejor. En lugar de usar esos 3
comandos se puede crear un atajo para copiar y otro para
pegar desde el portapapeles del sistema:


```
map <leader>Y "+gP
```

De esta forma, pulsando `<space>Y` se puede pegar respetando
la indentanción original.

Por cierto, escribí sobre el portapapeles del sistema y vim
en [otro post del blog](/posts/2021-02-22-portapapeles-en-vim/).

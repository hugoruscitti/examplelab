---
layout: post
title: El camino de Valentín
date: '2024-06-10 00:00:00'
description: |
  Hice una aplicación para visualizar cuándo llegará Valentín.
cover: /images/2024/el-camino-de-valentin/portada.jpg
---

¡En unas semanas va a nacer mi hijo Valentín!

Con Any estamos superilusionados y felices esperando su nacimiento. Tenemos
fecha probable de parto en dos meses y ya estamos preparando todo para recibir
el bebé.

Así que me pareció buena idea crear una aplicación que nos permita mirar cuánto
tiempo falta para su nacimiento y qué camino recorrimos hasta ahora.

Primero, pensé una forma de representar la evolución del embarazo y el punto en
donde nos encontramos:

![](/images/2024/el-camino-de-valentin/grafico.png)

Cada fila en este diagrama representa las semanas del embarazo. El corazón
simboliza el día actual y los colores de los círculos representan días. 

Esta forma de visualizar las semanas la diseñé en papel, y luego la convertí en
HTML y CSS. Luego, con ese boceto funcionando, agregué algo de JavaScript y la
fecha probable de parto para hacerla funcionar.

Hasta aquí, tenía una página web que solamente podía ver yo. Sin embargo, como
ya había aprendido algo de PWA haciendo [mi propia versión de
winamp](https://www.examplelab.com.ar/posts/2024-05-11-creando-retroplayer/)
hace unas semanas, se me ocurrió crear una aplicación mobile usando lo que había
aprendido.

Así quedó luego de unas horas de trabajo:

![](/images/2024/el-camino-de-valentin/icono.png)

![](/images/2024/el-camino-de-valentin/captura-mobile-valentin.png)

Lo bueno de haber creado esta aplicación es que pude compartirla con mi familia
y ver que les gustó mucho. ¡De hecho reconocieron algunas mejoras de animaciones
y efectos que agregué hace unos días!

Si querés ver o modificar el código del proyecto visita el
[repositorio](https://github.com/hugoruscitti/el-camino-de-valentin) en GitHub.

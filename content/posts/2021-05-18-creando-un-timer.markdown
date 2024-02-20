---
layout: post
title: Creando un timer
date: '2021-05-18 00:00:00'
description: |
 Armé un timer pomodoro usando arduino y unos componentes extra.
cover: /images/2021/creando-un-timer/portada.jpg
tags:
- proyecto
---

El mes pasado escribí sobre como me ayuda [hacer una sola cosa a la vez](../2021-04-09-una-cosa-a-la-vez) para
realizar tareas durante el día.

Sin embargo en el artículo me faltó describir cómo armé mi temporizador
externo:

![](/images/2021/creando-un-timer/temporizador.jpg)

El temporizador lo pude construir usando una plaqueta arduino, un display LCD 16x2, un
botón de arcade y algunas cosas más.

Empecé viendo algunos videos de youtube donde explicaban como conectar la plaqueta
arduino, cargar un programa e incluso mostrar mensajes en la pantalla LCD:

![](/images/2021/creando-un-timer/prototipo.jpg)

Miré unos cuantos videos, es increíble lo fácil que lo tienen muchos chicos de hoy
en día para aprender cosas nuevas; el formato en video para aprender sobre estas
placas es ideal, no me imagino cómo podría haber aprendido lo mismo leyendo un
libro.

En fin, una vez que vi los videos empecé a conectar los componentes usando una
*protoboard* siguiendo una guía que mostraba cómo interactuar con un pulsador:

![](/images/2021/creando-un-timer/proto.jpg)

El programa que usé como referencia solamente imprimía la frase "hola mundo" cuando
se pusaba el botón, pero como yo ya tenía en mente hacer el temporizador adapté el mensaje para que se vea como
especie de barra de progreso con un
indicador de minutos como el que se ve en la foto.

Es tan sencillo modificar y relanzar el programa en *arduino* que uno siente como
si estuviera programando contra un test, te anima a probar el código rápido sin
pasar mucho tiempo en el editor. Y el solo hecho de "verlo andar" en la plaqueta
es muy motivador.

Luego para darle forma de accesorio y no tener la plaqueta con todos los cables
sobre la mesa encargué una caja a una imprenta que hace impresiones 3D:

![](/images/2021/creando-un-timer/case.jpg)

La caja quedó muy bien, pero al tiempo me di cuenta de que era muy pequeña para el
tipo de botón que tenía pensado agregarle.

Resulta que hace un tiempo armé un arcade y tenía un par de botones que me gustaban
mucho. En esta foto se puede ver que el botón es apenas más largo que la caja:

![](/images/2021/creando-un-timer/boton.jpg)

Estos botones son muy buenos, pasé gran parte de mi infancia jugando
arcades y quería tener un botón de esos en el temporizador, ya era una cuestión de
capricho personal.

Así que me puse a adaptar un poquito el botón por dentro: en lugar de usar el pulsador
negro que viene con el arcade pegué dos botones de arduino entre sí, y recorté el
plástico blanco del botón de arcade para que sea "cortito" y quepa dentro de la
caja:

![](/images/2021/creando-un-timer/recorte.jpg)

El efecto de pulsación no es igual a lo que quería, pero aun así me gustó
como quedó.

Luego terminé de hacer el programa y me puse a empalmar los cables entre sí para no
tener que usar el protoboard:

![](/images/2021/creando-un-timer/soldar.jpg)

![](/images/2021/creando-un-timer/soldar2.jpg)

Y una vez finalizado, quedó mucho más compacto de lo que parecía al principio:

![](/images/2021/creando-un-timer/fin.jpg)

Luego para mejorar un poco el diseño de la caja la pinté de negro y le busqué un
lugar en el escritorio:

![](/images/2021/creando-un-timer/desktop.jpg)

Ya hace dos años que estoy usando este temporizador y estoy muy contento, tendría que
haber hecho este post hace tiempo porque incluso ahora que estoy escribiendo
esto no recuerdo dónde puse el código que cargué en la plaqueta.

---
layout: post
title: Se viene huayra-motion ...
date: '2014-03-05 17:42:52'
description: Una de las novedades que tenemos preparadas para huayra 2 es huayra stopmotion...
cover: /images/2014/Mar/portada-presentacion-huayra-stopmotion.jpg
tags:
- linux
---

**Huayra-motion** es una de las novedades que tenemos preparadas para el lanzamiento de  **huayra 2**:

![](/images/2014/Mar/huayra_2_beta__Running__2014_03_04_23_01_32_2014_03_04_23_01_41.png)

Un programa que te permite crear películas y cortos animados usando la técnica de [stop-motion](http://es.wikipedia.org/wiki/Stop_motion) de manera sencilla y divertida.

En este post te voy a contar las características principales y un poquito de historia sobre el proyecto.

## Funcionalidades

**huayra-motion** tiene varias funcionalidades, pero se van desplegando a medida que utilizas el programa.

Cuando abrís el programa aparece un asistente que te guia en los primeros pasos:

![](/images/2014/Mar/huayra_2_beta__Running__2014_03_04_23_13_28_2014_03_04_23_13_30.png)

Lo hicimos super simple, apenas queremos agregarle algunos proyectos de ejemplo para que sea mas ilustrativo en el primer inicio.

Luego, cuando inicias un proyecto, hay 4 partes principales en la interfaz:

![](/images/2014/Mar/huayra_2_beta__Running__2014_03_04_23_15_01_2014_03_04_23_17_48.png)

1 - Un área de previsualización.
2 - El panel de ajustes, tiene capas, efectos y opciones.
3 - Las operaciones básicas.
4 - Una línea de tiempo, con un cursor indicando el cuadro actual.

En este caso abrí una animación muy básica que armé con lo único que tenía a mano en el bar donde suelo ponerme a escribir el blog.

Con solo ajustar la cámara web y pulsando el botón "capturar" se pueden hacer cosas sencillas en poco tiempo.

## Exportación simple

Una de la cosas que agregamos recientemente es la posibilidad de exportación directa a video y animaciones GIF:

![](/images/2014/Mar/huayra_2_beta__Running__2014_03_04_23_10_42_2014_03_04_23_10_44.png)

Mi intención es añadir más opciones y un previsualizado rápido. Como estamos utilizando la herramienta *FFMPEG* por detrás, tenemos un montón de parámetros disponibles para ajustar la calidad y el tamaño del video a generar.

Incluso nos gustaría implementar la posibilidad de subir videos a youtube o vimeo directamente.

Este es el resultado de la animación exportada como GIF desde la aplicación:

![](/images/2014/Mar/animado.gif)

Claramente no soy un talentoso del stopmotion ñ_ñ pero estoy seguro de que muchos chicos en las escuelas si lo son, y huayra-motion seguramente les va a resultar de mucha utilidad.


## Pensada para integrarse

**huayra-motion** también se puede integrar con otras aplicaciones del ecosistema Linux. Por ejemplo, podrías usar [Open Shot](http://www.openshot.com) para integrar los cuadros en un video o [Audacity](http://audacity.sourceforge.net) para componer los efectos de sonido.

Todos los cuadros de animación se guardan como archivos *.png* individuales, así que se pueden leer y modificar desde casi cualquier programa multimedia.

## ¿Cómo surgió huayra-motion?

Iván y Claudio, del equipo de diseño en huayra, tenían esta idea en mente hace tiempo: Hacer un programa que permita enseñar y construir películas usando la técnica de stopmotion, una herramienta que sea libre y sencilla de utilizar.

Además, en [conectar igualdad](http://www.conectarigualdad.gob.ar/) se realizan de manera periódica varias actividades y talleres sobre stopmotion y composición de video, así que veíamos en esta herramienta una forma de contribuir a los talleres y un desafio divertido de resolver.

Al principio pensamos en hacerle mejoras a un software existente, llamado [linux-stopmotion](http://linuxstopmotion.org/), pero al tiempo surgió otra idea: "Hacer nuestra propia versión desde cero" :)

## ¿Desde cero?

Sé que muchas personas no se sienten cómodas pensando en hacer software desde cero; en cambio yo si me siento cómodo, para mí es bueno encarar aplicaciones desde cero, y por suerte los chicos de huayra también comparten esa visión.

Hay algo profundamente útil en empezar algo nuevo, podés conocer en detalle cada pieza del programa, volverte mejor diseñador y programador. Porque si haces un programa desde cero todo puede elegirse: herramientas, diseño, características, componentes, funcionalidad, ¡todo!.

No hay [deuda técnica heredada](http://es.wikipedia.org/wiki/Deuda_t%C3%A9cnica) cuando haces un programa desde cero, si el programa tiene bugs o puntos flojos no es culpa de alguien mas, son tus bugs, y esa situación por si sola se convierte en un aprendizaje enorme.

Por supuesto iniciar proyectos desde cero es mucho más difícil que buscar algo prefabricado y modificarlo, pero eligiendo hacer algo desde cero te ves obligado a buscar un diseño simple,  objetivo y funcional.

## Prototipando con node-webkit

Al igual que pasó con [huayra-compartir](http://www.examplelab.com.ar/presentanto-huayra-compartir/), aquí hicimos algunas pruebas y experimientos para ver que nos podía resultar mejor y resultó ser node-webkit.

A fin del año pasado había hecho un trabajo freelance junto a unos amigos, usando  django y algunas cosas de html5 como angularjs y captura de video con [getUserMedia](http://www.html5rocks.com/en/tutorials/getusermedia/intro/). Así que me animé a poner en práctica ese conocimiento e intentar un prototipo enteramente usando *html5*.

La primer versión se veía así:

![](/images/2014/Mar/test.jpg)

Pero luego de hacer algunos retoques sentí que se podía simplificar un poco más. También por esos días Claudio me sugirió que la barra superior (tipo header) no aportaba mucho, ¡y tenía razón!, así que la quité.

El resultado me parece mucho mejor ahora:

![](/images/2014/Mar/salero_animado_2014_03_05_01_25_40_2014_03_05_01_25_49.png)

Hay más espacio para desplegar componentes, cámaras adicionales y pestañas.

## El modo colaborativo

**huayra-motion** incorpora un modo colaborativo, la aplicación puede funcionar en *red*, haciendo que los chicos puedan trabajar en equipo sobre uno o varios proyectos.

Este modo no es muy complejo en sí, pero es algo innovador si pensamos en otras aplicaciones de escritorio para Linux: casi todas las aplicaciones funcionan de manera aislada, un usuario por programa/proyecto.

El modo colaborativo de *huayra-motion* es apenas una nueva incursión en algo colaborativo desde el diseño. Es algo que también estamos investigando en [huayra-compartir](http://examplelab.com.ar/presentanto-huayra-compartir/).

La aplicación inicializa un webserver sencillo realizado con [express](http://expressjs.com) y  [socket.io](http://socket.io) al que se puede conectar cualquier netbook o PC para compartir su cámara web.

Así, podrías tener **huayra-motion** en una netbook y usar otras computadoras como cámaras secundarias, todas como recursos para el mismo proyecto.

Creo que podemos mejorar un montón acá. Pensar aplicaciones multi-usuarios y colaborativas es super desafiante, hay un montón de bibliotecas y patrones de diseño que ya no nos sirven, y por supuesto hay muchas nuevas ideas y investigaciones que tenemos por explorar...

Pienso que es una de los desafíos técnicos que tenemos en el equipo de huayra por delante: descentralizar aplicaciones, pero buscando hacerlas colaborativas entre sí.


## Interface "casi" no-modal

Una de las cosas que nos dio varios dolores de cabeza, pero que me gustaría conservar, es el funcionamiento no-modal.

La aplicación no te invita a fragmentar tu modo de trabajar, no tiene un modo reproducción y un modo edición completamente separados, o un panel de preferencias que te interrumpe hasta que guardas los resultados.

Por el contrario, mientras la aplicación funciona podés hacer ajustes, seguir capturando fotos o consultar los atajos de teclado:

<iframe width="640" height="480" src="//www.youtube.com/embed/xZIgKShW0po?rel=0" frameborder="0" allowfullscreen></iframe>

Pienso que este enfoque es mucho útil a la hora de trabajar, te permite observar y construir de manera más fluida, sin interrupciones o demoras.

Lamentablemente algunas cosas siguen siendo bloqueantes para los usuarios en este momento, por ejemplo cuando exportas una película el programa te hace esperar hasta que el video está listo. Aunque creo que si seguimos investigando, podemos hacerlo funcionar de otra manera.

## Invitación

Estamos ansiosos conocer la recepción de los jóvenes en las escuelas, en el equipo creemos que *huayra-motion* tiene un buen camino por delante, hay muchos detalles por pulir, y funcionalidades que aún están en pleno diseño, así que escribimos código todos los días para mejorar la herramienta poco a poco.

¿Nos ayudas a mejorar **huayra-motion**?, ¿Qué te gustaría ver en la próxima versión de la aplicación?

https://github.com/HuayraLinux/huayra-stopmotion

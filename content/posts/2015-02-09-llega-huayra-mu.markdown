---
layout: post
title: "¡ huayra-mu !"
image: "/images/2015/02/2015-02-07-00-59-29.jpg"
date: '2015-02-09 16:31:56'

description: "Hoy quiero presentarles una aplicación nueva, diseñada especialmente para el nuevo huayra 3..."
cover: '/images/2015/02/portada.jpg'
tags:
- linux
---

Hoy quiero presentarles una aplicación nueva, diseñada especialmente para el nuevo huayra 3.0, [huayra-mu](https://github.com/hugoruscitti/huayra-mu):

![](/images/2015/02/preview.png)

La herramienta está orientada principalmente a programadores y diseñadores, porque permite crear la estructura inicial de un proyecto con mucha facilidad, siguiendo buenas prácticas y de manera muy rápida.

La idea es simple, [huayra-mu](https://github.com/hugoruscitti/huayra-mu) se inicia desde una terminal, pregunta el nombre del proyecto, la tecnología a utilizar y listo:

![](/images/2015/02/2015-02-07-19_10_49.gif)

El proyecto generado quedará guardado dentro de un directorio, en donde podemos encontrar los archivos iniciales para comenzar a trabajar.


Motivación
----

Cuando comenzamos un proyecto, hay muchas tareas que son comunes a casi cualquier proyecto: hacemos un repositorio, creamos los directorios iniciales, construimos los archivos de configuración, armamos los scripts para realizar los paquetes instalables, etc...

Hacer estas tareas iniciales por cada proyecto se hace algo tedioso y en muchos casos genera proyectos muy diferentes entre sí, o incompletos.

Imagina estas tareas siendo realizadas una y otra vez, por cada nuevo proyecto... ¿no sería bueno resolver esas tareas una sola vez?.

El objetivo de [huayra-mu](https://github.com/hugoruscitti/huayra-mu) es que podamos hacer esa tarea inicial una sola vez y de manera óptima, reuniendo buenas prácticas y logrando consistencia en la estructura de nuestras aplicaciones.


Plantillas incluidas
-------

Las plantillas son simplemente los modelos de aplicación inicial que te ofrece [huayra-mu](https://github.com/hugoruscitti/huayra-mu) al crear un nuevo proyecto. En esta primer etapa de la aplicación hicimos 4 plantillas, pero esperamos poder agregar algunas más conforme la aplicación se empiece a utilizar.

Las plantillas que incluimos permiten hacer aplicaciones de escritorio con [nwjs](http://nwjs.io/), videojuegos con [pilas-engine](http://pilas-engine.com.ar/) y presentaciones con [reveal.js](http://lab.hakim.se/reveal-js/):

- html5
- emberjs
- pilas-engine
- reveal

Seguramente hay muchas otras tecnologías interesantes para sugerir, pero optamos por estas 4 para comenzar, además de que las conocemos y nos sienta bien recomendarlas sin dudarlo :)

Un ejemplo de uso
-------

A modo de ilustración, hagamos un pequeño proyecto de videojuego usando  [huayra-mu](data/plantillas/nwjs-ember-seed):

- ¿Que necesitamos?:

El primer paso es abrir una terminal y ejecutar el comando **mu**:

![](/images/2015/02/huayra-mu-2015-02-07-20-42-16.png)

En pantalla tenemos que escribir el nombre de nuestro juego y luego elegir [pilas-engine](http://www.pilas-engine.com.ar):

![](/images/2015/02/huayra-mu-2015-02-07-20-46-12.png)

Luego se van a mostrar las instrucciones para comenzar a trabajar en el proyecto:

![](/images/2015/02/ppp-2015-02-13-12-40-27.png)

Si escribís esos pasos, la aplicación va a iniciar inmediatamente:

    cd mi-juego
    make ejecutar_linux

![](/images/2015/02/huayra-3---beta-febrero---32-bits--Running--2015-02-13-12-53-34.png)

¿Pero qué hizo **mu** por nosotros?, si abrimos *caja* o comenzamos a navegar el contenido del directorio van a aparecernos varias cosas:

![](/images/2015/02/huayra-3---beta-febrero---32-bits--Running--2015-02-13-12-56-42.png)

**mu** generó dos directorios, uno para el código (directorio ``src``) y otro para las imágenes y sonidos (el directorio ``data``).

Así que podríamos empezar a programar ahí mismo, editando o creando archivos nuevos en src.

Por ejemplo, en mi equipo puedo abrir el editor **geany** y comenzar a editar el archivo ``src/juego``:

![](/images/2015/02/huayra-3---beta-febrero---32-bits--Running--2015-02-13-13-06-35.png)

Ah, por cierto, si usaste [pilas-engine](http://pilas-engine.com.ar/) antes, vas a notar una novedad interesante en esta plantilla: cada vez que guardes el código, la ventana de pilas va  a detectar el cambio y se va actualizar sola. ¡No hace faltar cerrar y abrir la ventana!


Más comandos
----

Todos los proyectos que genera **mu** vienen con una serie de comandos para hacer cosas típicas, como ejecutar la aplicación, publicar una nueva versión o incluso empaquetarla en un archivo ``.deb``.

Para ver estos comandos, lo único que tienes que hacer es llamar al comando ``make`` dentro del directorio del proyecto:


![](/images/2015/02/huayra-3---beta-febrero---32-bits--Running--2015-02-13-13-13-54.png)


¿Ideas?
-----

Me encantaría conocer qué otras tecnologías podemos agregar, ¿te animas a sugerirnos alguna?. ¿Qué otras tareas se pueden automatizar para ayudar a los desarrolladores?.

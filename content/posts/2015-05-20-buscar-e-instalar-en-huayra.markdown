---
layout: post
title: Buscar e instalar en Huayra
image: "/images/2015/05/2015-05-19-23-26-58-copia.jpg"
date: '2015-05-20 03:13:32'

description: "Creamos una herramienta para facilitar la instalación de software en Huayra"
cover: '/images/2015/05/portada.jpg'
tags:
- linux
---

Esta semana creamos una herramienta nueva para todos los usuarios de huayra linux: **huayra-alias**.

El objetivo de esta herramienta es facilitar la búsqueda e instalación de paquetes con dos comandos nuevos. Ayudando a simplificar tutoriales, acortar instrucciones y escribir menos :)

## Pensando en comandos ...

Huayra está basado en **debian gnu/linux**, una de las distribuciones más sólidas y prestigiosas impulsada por la comunidad de software libre.

Y en **debian**, como en muchas otras distribuciones de linux, se utilizan comandos para casi todo: hay comandos para procesar archivos, instalar software, iniciar servicios, compartir archivos etc...

Pero curiosamente, entre estos comandos, no se incluyen atajos pensados para facilitarnos el uso de la computadora. Por ejemplo, para buscar software a veces terminamos escribiendo algo como *"sudo apt-get update; apt-get search ..."*  y algunas cosas más.

Pienso que algunos comandos se diseñaron como si fueran [navajas suizas](http://es.wikipedia.org/wiki/Navaja_suiza), con muchos parámetros y opciones pensadas para contemplar un montón de casos de uso.

Por suerte podemos cambiar esto, y construir comandos rápidos para realizar las tareas más cotidianas, como *buscar* e *instalar*.

## Buscar

El primer comando que creamos es **buscar**, que simplemente se encarga de realizar búsquedas en la base de datos de software disponible en los repositorio y mantener actualizados lo índices de búsqueda para responder rápido.

Por ejemplo, si escribimos **buscar stopmotion** en una consola de huayra:

![](/images/2015/05/huayra-3-0--i386---Running--2015-05-19-23-29-26.png)

aparecerán dos opciones, donde la primer columna de nombres en color verde son los nombres de paquetes, y lo que sigue es una descripción breve.

Y también vale comentar que el comando **buscar** realizará una actualización y optimización de búsquedas si fuera necesario, automáticamente:

![](/images/2015/05/huayra-3-0--i386---Running--2015-05-19-23-28-32-png.png)

## Instalar

El siguiente comando es **instalar**, que nos sirve para descargar, instalar y configurar un paquete de forma automática escribiendo solamente su nombre.

Volviendo al ejemplo anterior, si quisiéramos instalar o actualizar **huayra-stopmotion** podemos escribir:

![](/images/2015/05/huayra-3-0--i386---Running--2015-05-19-23-30-03.png)

y listo: El mismo comando nos puede servir para realizar instalaciones y actualizar, ya sea un paquete o varios.


## Ideas a futuro

Una vez que implementamos la primer versión, como era de esperar, nos dimos cuenta que llegamos a algo interesante, y que podemos comenzar a implementar funcionalidades nuevas poco a poco.

Por ejemplo, nos gustaría añadirle una ayuda al comando *instalar*, y que nos guíe si equivocamos el nombre de un paquete, algo así como hace google cuando nos muestra un texto que dice "usted quiso decir ...", o incluso, que nos muestre una lista de los paquetes que podríamos actualizar.

También podemos añadir algunos comandos como *doctor*, para detectar problemas de configuración o imprimir sugerencias de actualización o algo así...

En fin, los dejo con el [link al proyecto en github](https://github.com/HuayraLinux/huayra-alias), donde te invitamos a participar del desarrollo junto a nosotros: pensar funcionalidades nuevas, buscar errores y programar :)

---
layout: post
title: Jugando con PWA
date: '2023-03-02 00:00:00'
description: |
  Adapté una app django al formato PWA
cover: /images/2023/jugando-con-pwa/portada.jpg
---

Estamos usando el sistema de presupuestos y gastos
personales que armé en Django junto con Any.

El tema es que ella suele usar el sistema desde el celular y
no desde una computadora como hago yo. Así que notamos
varias cosas para mejorar en la aplicación.

Por una lado, acceder a la aplicación con el navegador es
algo incómodo, notamos que se podía hacer una acceso rápido
desde la pantalla inicio del celular, pero con ese acceso
igual aparecían las barras de navegación y eso quitaba algo
de espacio en pantalla.

Tampoco se veían bien algunas opciones por el tamaño de la
pantalla y cómo se mostraban los diálogos modales.

Así que me puse a pensar formas de mejorarlo y dí con
una solución para todo esto: Existe un paquete de django que
nos permite convertir la aplicación web en una PWA
(Progressive Web App), haciendo que nuestra aplicación
Django parezca una aplicación mobile.

Este es el paquete:

https://github.com/silviolleite/django-pwa

Así que lo instalé y comencé a jugar. Pude hacer que la
aplicación tenga un icono de acceso y se pueda instalar en
la pantalla principal del celular, que desaparezcan las
barras de menú, la URL de la pantalla y algunos detalles
más.

Lo primero que noté luego de configurar el paquete es que la
aplicación se podía instalar desde la computadora. Lo que me
resultó muy práctico para probar todos los cambios de forma
local:

![](/images/2023/jugando-con-pwa/instalación-en-osx.png)

Una vez que se instala la aplicación web, se puede abrir
directamente desde la sección de aplicaciones del navegador:

![](/images/2023/jugando-con-pwa/apps.png)

Es decir, con solo instalar el paquete y configurar algunos
parámetros ya pude ver que todo funcionaba bien desde mi
computadora, ¡bien!.

Lo siguiente que miré es cómo se comportaba todo esto en el
celular, y por suerte se veía perfecto desde el primer
momento. Las barras desaparecieron:

![](/images/2023/jugando-con-pwa/comparativa.png)

Y también pude instalar la aplicación para que aparezca en
la pantalla principal:

![](/images/2023/jugando-con-pwa/inicio.png)

No se si todo este tema de las PWA va a seguir existiendo en
unos años, pero hoy me resolvió algo que hace unos años me
hubiera llevado un montón de tiempo.

Ahora puedo concentrar esfuerzo en hacer una sola
aplicación, que produce HTML del lado del servidor y que
además puede funcionar muy similar a una aplicación nativa
de celulares.

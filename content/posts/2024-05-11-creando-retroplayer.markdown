---
layout: post
title: Creando un reproductor de música como Winamp
date: '2024-05-11 00:00:00'
description: |
  Hice un reproductor de audio para rendir homenaje a Winamp, el mejor player de música de todos los tiempos.
cover: /images/2024/creando-retroplayer/portada.jpg
---


Winamp fue mi reproductor de música favorito por muchos años, me trae a la mente muy lindos recuerdos.

![](/images/2024/creando-retroplayer/winamp-original.png)

Tan solo ver esa pequeña pantalla con botones me lleva a mis primeros años frente a la computadora, cuando intentaba aprender a programar en Delphi mientras escuchaba música desde archivos `mp3`.

Si bien pasaron muchos años, extraño tener un programa como ese en mi computadora. Así que me puse a crear una versión homenaje de Winamp, imitando algunas de sus funcionalidades.

## ¿Cómo hacer un reproductor de música?

Hay muchas formas diferentes de hacer un reproductor de música, muchas tecnologías de donde elegir y enfoques de todo tipo. Pero desde el primer momento me pareció buena idea hacer las cosas lo más artesanalmente posible.

Comencé a escribir el proyecto usando vanilla JavaScript, sin frameworks ni compiladores, tratando de reducir al mínimo las dependencias, y así tener un proyecto simple y fácil de ejecutar.

También aproveché a declarar la aplicación como una PWA, de forma que se pueda instalar en el escritorio como una aplicación independiente del acceso a internet y la estética de un navegador.

## ¿Qué hacer y qué no hacer?

Parece una pregunta tonta, pero winamp hacía muchas cosas, y tratar de hacer una copia fiel del programa es imposible para mí.

Lo único que me gustaría implementar es la funcionalidad básica de reproducir archivos desde una carpeta. Agregarle botones para navegar la lista de canciones y algunas cosas más.

Es fácil listar las cosas que quiero hacer, pero… ¿Qué cosas debería dejar afuera?

- No quiero leer o procesar `metadata` de los archivos, ni el nombre del artista, ni el año de lanzamiento, etc. Voy a identificar a las canciones por el nombre de archivo.
- No quiero un ecualizador.
- La lista de canciones tiene que estar visible todo el tiempo. No ser una ventana independiente y configurable.
- No quiero integración con el sistema, la ventana tiene que ser como cualquier otra. Ni notificaciones, ni atajos de teclado para pasar canciones.
- No quiero implementar ningún menú de opciones, que todo funcione por omisión.
- Quiero quitar el paneo, con el control de volumen está bien.

## Primeros pasos haciendo mi propio Winamp

Para comenzar, hice un proyecto web que se pueda instalar como una aplicación PWA. Muy simple, sin ningún `feature` especial, solo una ventana con un botón:


![](/images/2024/creando-retroplayer/primer-version.png)

Armar esta primera versión me gustó porque pude crear una estructura muy simple. Usé módulos, HTML, JavaScript sin dependencias ni frameworks.

Además, logré hacer que se pueda instalar como una aplicación de escritorio.

## Buscando la estética de Winamp

Para imitar la estética de Winamp, usé un `skin` moderno [que encontré en Internet](https://forums.winamp.com/forum/skinning-and-design/modern-skins/314306-winamp-classic-modern-by-victhor). Este `skin` es muy similar a la versión original, pero está diseñado desde cero, usando imágenes con más resolución y más colores:

![](/images/2024/creando-retroplayer/comparacion-original-moderno.png)

Llevar los archivos del `skin` a la aplicación fue sencillo, tuve que editar algunas imágenes para separarlas en archivos `.png` y vincularlas con el archivo `.css`:

![](/images/2024/creando-retroplayer/imagenes-del-skin.png)

Luego, dentro de la estructura HTML, tuve que crear algunos elementos del tamaño esperado y asociarle estas imágenes para “vestir” la interfaz de usuario.

Acá se ve cómo estos elementos se combinan entre sí:

![](/images/2024/creando-retroplayer/winamp-inspector.png)

Por un lado, la estructura HTML que representa el botón, luego el CSS con la imagen del botón y a la izquierda de la pantalla el resultado.


## Arrastrando archivos

Lo siguiente que hice fue incorporar una forma de cargar archivos para reproducirlos.

Opté por la estrategia más sencilla, el reproductor solo permite reproducir canciones si se arrastra y suelta una carpeta completa con archivos `.mp3`

## Visualización de frecuencia

Para recrear el visualizador de frecuencia investigué la documentación de Mozilla y encontré un artículo que explicaba a la perfección lo que estaba buscando:

![](/images/2024/creando-retroplayer/mdn-visualizador.png)

De hecho, el artículo también menciona a Winamp.

Jugué un montón con esta parte del programa, y fue una de las cosas más gratificantes de hacer.

Así quedaba el visualizador luego de unas cuantas horas de pruebas:

![](/images/2024/creando-retroplayer/winamp-animacion.gif)

## Publicando el resultado como una PWA

Para publicar el proyecto, lo más sencillo que encontré fue usar `gitpages`, un servicio que ofrece GitHub para publicar sitios estáticos a partir de un repositorio. Lo único que tuve que hacer es ingresar a la configuración del repositorio y activar esta opción:

![](/images/2024/creando-retroplayer/winamp-configuracion-de-gitpages.png)

La aplicación me quedó tal y como esperaba, funciona sin problemas (al menos para mi caso de uso), y me gusta como se ve:

![](/images/2024/creando-retroplayer/winamp-version-final.png)

Por cierto, si quieres usar e instalar la aplicación en tu computadora visita esta web:

- https://hugoruscitti.github.io/retroplayer/
- (o el repositorio en: https://github.com/hugoruscitti/retroplayer)

y luego pulsa el botón instalar en la barra de navegación del navegador:

![](/images/2024/creando-retroplayer/winamp-instalancion-pwa.png)



## Ideas a futuro

No voy a agregar mejoras al programa por ahora, me gustaría usar la aplicación un par de meses y evaluar ahí qué añadir.

También me gustaría reflexionar sobre qué buenas ideas y patrones encontré haciendo el sistema de eventos y creando los componentes desde cero sin usar frameworks, tal vez escriba más sobre esto en futuros post.

¡Gracias por leer!

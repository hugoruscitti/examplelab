---
layout: post
title: Presentando huayra-caripela
date: '2014-06-27 22:00:00'
---

Hace unas semanas empezamos a realizar una aplicación nueva:  *huayra-caripela*.

Es una aplicación muy sencilla, que sirve para hacer avatares y personalizar las preferencias de tu usuario en *huayra linux*:


![](/images/2014/Jun/Caripela_2014_06_22_19_20_12_2014_06_22_19_20_24.jpg)


Como se puede ver en la captura, "caripela" te muestra una galería de objetos en pantalla para armar un rostro, con muchas posibles combinaciones:

![](/images/2014/Jun/Caripela_2014_06_22_18_44_52_2014_06_22_18_47_20.png)

![](/images/2014/Jun/Caripela_2014_06_22_18_50_45_2014_06_22_18_50_48.png)

<iframe width="960" height="720" src="//www.youtube.com/embed/B6qsvYkTTAA?rel=0" frameborder="0" allowfullscreen></iframe>


## ¿Por qué?

Pensamos que sería buena idea contar con una aplicación que te permita dibujar fácilmente, realizar un avatar representativo y que puedas darle un toque personal a tu configuración de usuario.

En *huayra* el perfíl de usuario se ve en varios lados, por ejemplo en la pantalla inicial de acceso y en huayra-compartir:

![](/images/2014/Jun/huayra_rc4__Running__2014_06_22_19_21_44_2014_06_22_19_22_17.png)
![](/images/2014/Jun/huayra_rc4__Running__2014_06_22_19_28_08_2014_06_22_19_28_27.png)



## ¿Y cómo está hecho?

Usamos varias herramientas y algunas prácticas que aprendimos hace unas semanas, imaginá que hicimos esta aplicación en muy poquitos días, prototipando y aprendiendo sobre la marcha.

Usamos [fabric.js](http://fabricjs.com/) para que los chicos puedan manipular cada parte del personaje que quieren construir. [fabric.js](http://fabricjs.com/)  actúa sobre el canvas de HTML5 y agrega controles a cada objeto, además nos brinda una API para exportar todas las figuras a diferentes formatos de imágenes, como .PNG o .SVG, entre otras características más.

Otras herramientas que usamos fueron [nodewebkit](https://github.com/rogerwang/node-webkit), [angularjs](https://angularjs.org/) y [bootstrap](http://getbootstrap.com/), al igual que hicimos con otras aplicaciones como huayra-motion y huayra-compartir.

Internamente la aplicación, "lee" un directorio de imágenes SVG que representan a cada una de las piezas que podrías usas para realizar las caripelas. Así que para agregar nuevas piezas simplemente se pueden copiar mas archivos SVG dentro de esa carpeta.

## ¿Y si fuera web?

Si bien la aplicación es offline, también experimentamos con crear una versión online, donde todos podamos crear nuestras "Caripelas" y compartirlas sin necesidad de instalar nada, todo funciona desde el navegador:

<ul>
<li><a href='http://dev-losersjuegos.com.ar:9599/' target='_black'>Ingresar a caripela on-line</a></li>
</ul>


Obviamente esta versión online es sólo un experimento, lo creamos para evaluar el costo de llevar un aplicación como *caripela* a un webserver y experimentar con [sailsjs](http://sailsjs.org/):

![](/images/2014/Jun/Caripela_2014_06_22_19_04_02_2014_06_22_19_04_06.png)


## Descarga e instalación

Actualmente la aplicación se puede descargar  desde [github](https://github.com/hugoruscitti/caripela) e incluso se puede instalar en huayra con el siguiente comando:

	sudo apt-get install caripela
    
y luego va a estar visible en el menú:

![](/images/2014/Jun/huayra_rc4__Running__2014_06_22_19_12_27_2014_06_22_19_12_55.png)

Y la versión online que mencionamos antes también está en [github](https://github.com/hugoruscitti/caripelaweb), solo que esta versión online es un poco mas compleja de hacer andar (requiere node, sailsjs etc...):

## Ideas a futuro

¿Que te gustaría ver en las siguientes versiones de *huayra-caripela*?

Seguramente en estos días estemos agregando algunas mejoras y actualizando algunos detalles que nos quedaron en el tintero. Cualquier sugerencia o idea que quieras compartir con nosotros vamos a estar super agradecidos de escucharla ;)

---
layout: post
title: "¡ The Zombie Smasher !"
image: "/images/2016/04/header.jpg"
date: '2016-04-26 19:18:46'
---

Esta semana publicamos un videojuego nuevo para iOS: ¡The Zombie Smasher!

En este post me gustaría hacer una pequeña reseña del juego y cómo lo realizamos:

![](/images/2016/04/teaser.jpg)

<iframe width="420" height="315" src="https://www.youtube.com/embed/jufMEynEfQQ" frameborder="0" allowfullscreen></iframe>





## ¿De qué se trata?

El juego tiene una mecánica muy similar a [Dragon Punch](http://examplelab.com.ar/nuestro-juego-nuevo-dragon-punch/), de hecho partimos del mismo código base. Comenzamos mejorando los controladores de efectos sonoros y las músicas, luego agregamos niveles y mucho más:

![](/images/2016/04/2-1.jpeg)
![](/images/2016/04/4.jpeg)
![](/images/2016/04/6-1.jpeg)
![](/images/2016/04/7-1.jpeg)
![](/images/2016/04/8-1.jpeg)

![](/images/2016/04/sprites-final-hero.jpg)

## Lo que aprendimos

Unity es fascinante, no sólo para desarrollar el juego en sí, sino su ecosistema completo.

![](/images/2016/04/gameScene-unity---unity-the-zombie-smasher---iPhone--iPod-Touch-and-iPad--Personal--2016-04-26-15-45-20.jpg)

Lo primero que llevamos adelante es mejorar el workflow para realizar pruebas. Comenzamos llevando todo el código a bitbucket, y configurando la compilación en la nube de unity:


![](/images/2016/04/-Commits---Bitbucket-2016-04-25-11-27-38.png)

![](/images/2016/04/History---Unity-Cloud-Build-2016-04-25-11-12-11.png)

Esto nos permite delegar la compilación del juego a los servidores de unity.


Por último, para probar el juego en nuestros teléfonos y tablets, usamos itunes-connect y una aplicación llamada testflight:

![](/images/2016/04/iTunes-Connect-2016-04-25-11-02-57.png)

Otra cosa que mejoramos desde el principio es el manejo de imágenes, preparamos todo para minimizar el uso de texturas. Así que empaquetamos todos los sprites en spritesheets:

![](/images/2016/04/Sprites-2016-04-25-10-49-49.png)

Por último, también mejoramos mucho el proceso de composición para músicas y sonidos. Dejamos de trabajar en mp3 y usamos el formato OGG. el cambio fue drástico en el muestreo y calidad de los tracks:

Particularmente the zombie smasher tiene 4 tracks compuestos especialmente para la temática de cada nivel.

Usando algunas técnicas aprendidas en libro de Gryzor87: "Cool music for videogames", pudimos darle una sensación de progresión de dificultad a través de la mezcla y utilización de instrumentos en FL STUDIOS.

![](/images/2016/04/3d03b088-6651-499d-881e-484dbc7ed8d6.jpg)

![](/images/2016/04/Foto-resen-a-1.jpg)

## ¿Dónde se puede conseguir el juego?

El juego está publicado en la tienda oficial de apple, tanto para ipad, iphone y ipod touch:

https://itunes.apple.com/us/app/the-zombie-smasher/id1065520591

![https://itunes.apple.com/us/app/the-zombie-smasher/id1065520591](/images/2016/04/The-Zombie-Smasher-on-the-App-Store-2016-04-24-23-51-17.png)

Posiblemente en unas semanas vamos realizarle algunas mejoras adicionales y subirlo a google play también, ¿tenés android?, ¿te gustaría comprar el juego? ¡Avísanos!.

Links útiles:

 - [La web de twoplayers.](http://www.twoplayers.com.ar)
 - [Página de la tienda AppStore.](https://itunes.apple.com/us/app/the-zombie-smasher/id1065520591)
 - [Post sobre efectos utilizados.](http://examplelab.com.ar/convertir-videos-en-imagenes-con-canal-alpha/)
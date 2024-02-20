---
layout: post
title: Devolviendo el control a tu navegador
date: '2021-04-05 00:00:00'
description: |
  Cómo personalizar la forma en la que tu navegador muestra contenidos de la web.
cover: /images/2021/devolviendo-el-control-a-tu-navegador/portada.jpg
tags:
- web
- reflexión
---

Algo que me gusta mucho de la web es que está diseñada para ser interpretada
por un navegador:

Tomemos como ejemplo alguna de las extensiones para bloquear contenido 
tipo [AdBlock](https://es.wikipedia.org/wiki/AdBlock), ¿acaso no es una
genialidad poder bloquear
publicidades usando JavaScript?. ¿Y qué tal poder aumentar el tamaño de los textos pulsando
`CTRL +`?, ¿y ver la actividad de red y bloquear dominios?.

Es fácil habituarse a un navegador, dar por sentado que todo lo que hace es algo común, pero lo cierto
es que casi ningún otro medio nos permite tener tanto control sobre el contenido como hace
un navegador. Con un navegador podemos inspeccionar y ver cómo están hechas las cosas, incluso modificarlas.


Y de esto último me gustaría escribir hoy: el navegador nos permite modificar cosas de
las web que visitamos.

Por ejemplo, una vez al mes suelo ingresar al sitio de *visa* para consultar
mis gastos de la tarjeta de crédito y tomar notas en mi presupuesto.

Una de las primeras pantallas que visito siempre tiene una imagen ofreciendo ayuda para obtener
una clave que tengo hace más de 10 años, lo que hace que el mensaje esté de más
para mí:

![](/images/2021/devolviendo-el-control-a-tu-navegador/login.png)

y luego, cuando ingreso al sitio hay un panel de chat que se mueve llamando la atención
cada 5 segundos y un carrusel de publicidades, ¡sí, un carrusel de publicidades que
se mueve todo el tiempo!:

![](/images/2021/devolviendo-el-control-a-tu-navegador/home.png)

Ahora bien, como el navegador es un intérprete, hay ciertas cosas que se pueden inspeccionar
y cambiar.

Por ejemplo, el logo de la pantalla inicial se puedo ocultar usando este *css*:

```css
.imagen-login {
  display: none;
}
```

mientras que el molesto carrusel de publicidades y el chat se pueden ocultar así:

```css
.banner.container-12 {
  display: none;
}

#AgentAppContainer {
  display: none !important;
}
```

Ahora, para que este estilo se aplique automáticamente cada vez que ingresamos
a esta web se puede instalar algo como
[witchcraft](https://github.com/luciopaiva/witchcraft) y guardar nuestros estilos
css en archivos, así quedan privados en nuestro disco.

Además, *witchcraft* también nos permite inyectar archivos JavaScript, para añadir
algo de personalización más avanzada.


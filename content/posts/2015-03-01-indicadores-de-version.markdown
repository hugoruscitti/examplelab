---
layout: post
title: Haciendo indicadores de actualización
image: "/images/2014/10/1204-image_versioning_intro_1.jpg"
date: '2015-03-01 04:30:33'

description: "Esta semana pusimos en marcha un indicador de versiones muy simple para las aplicaciones de Huayra ..."
cover: '/images/2015/03/portada.jpg'

---

Esta semana pusimos en marcha un indicador de versiones muy simple para las aplicaciones de [huayra](http://huayra.conectarigualdad.gob.ar/).

Hicimos algo similar a lo que venía haciendo en [pilas-engine](http://www.pilas-engine.com.ar/), pero de manera mas sencilla:

![](/images/2014/12/pilas-engine-2014-12-28-11-47-09.png)

La idea es muy simple, cada vez que se abre una aplicación, buscamos informar a los usuarios si existe una versión mas reciente en nuestros servidores, y si es así, lo informamos.


## ¿Cómo se ve en las aplicaciones?

Imaginá que el usuario abre una aplicación como **huayra-curriculum**, si está usando la versión más reciente va a observar algo así:

![](/images/2015/03/huayra-curriculum-2015-03-01-00-50-51.png)

En cambio, si está usando una versión anterior lo que
va a mostrarse es lo sigiuente:

![](/images/2015/03/2015-03-01-00_02_15.gif)

Este indicador funciona junto con un servicio web, así que el usuario se puede enterar de la actualización el mismo día de la publicación.

En la imagen se puede ver que también incluimos un texto: *"Existe actualización"*, que se puede pulsar, y te envía directamente a una página con información de la actualización.

En estas primeras versiones, hicimos que [la página de actualización](http://hugoruscitti.github.io/huayra-tips/#/actualizar/huayra-curriculum) sea muy sencilla, incluyendo los pasos de actualización y algunas recomendaciones:

![](/images/2015/03/HuayraTips-2015-03-01-00-08-24.png)

Nuestra idea es que la página cuente lo mínimo e indispensable para que los usuarios puedan actualizar la aplicación rápidamente.

Obviamente en el futuro nos gustaría que las actualizaciones se puedan hacer con un solo click, así que vamos a seguir trabajando :)

## ¿Cómo funciona?

Para que el indicador funcione correctamente tuvimos que construir varias cosas:

En primer lugar, [Mauro](https://github.com/lvm) armó  un *webservice* al que se le pueden hacer preguntas para conocer las versiones de los paquetes en huayra.

Por ejemplo, si pedimos [esta ruta con navegador](http://devel.huayra.conectarigualdad.gob.ar/pkg/version/huayra-curriculum), el *webservice* nos retornará la información mas reciente del paquete  **huayra-currilum**:

![](/images/2015/03/huayra-curriculum-2015-03-01-00-21-36.png)

La segunda tarea consistió en armar un indicador de versión para cada una de las aplicaciones de huayra:

![](/images/2015/03/Huayra-Motion-2015-03-01-00-34-08.png)

Y por último, para completar el circuito de actualización completo, armamos un sitio con el tutorial para actualizar aplicaciones. Haciendólo personalizable por cada aplicación:

 - http://hugoruscitti.github.io/huayra-tips/#/actualizar/huayra-curriculum


Y acá un dato curioso: el sitio lo armé con ember, para que sea sencillo personalizar cada página, así que si incluís ``?debug`` al final de la URL anterior vas a ver la separación entre modelo y contenido :)



## Ideas a futuro

Hasta ahora logramos algo interesante, podemos tener la seguridad de que las nuevas versiones no van a pasar desapercibidas por mucho tiempo.

Sin dudas el canal más directo para informar a los usuarios es la misma aplicación, pero creemos que se puede hacer mejor.

Una de las cosas que me gustaría lograr es que las aplicaciones se puedan actualizar de forma más directa, como hace la aplicación de escritorio de [spotify](https://www.spotify.com/ar/) o el cliente gráfico de [github](https://github.com/):

![](/images/2015/03/687474703a2f2f6769746875622d696d616765732e73332e616d617a6f6e6177732e636f6d2f626c6f672f323031312f6d61632d73637265656e73686f74732f757067726164652e706e67.png)

Es decir, las dos aplicaciones tienen un enfoque ideal de actualización (al menos para mí), porque descargan la actualización automáticamente y luego informan al usuario que puede "reiniciar" la aplicación para usar la nueva versión.

La otra idea que me queda en mente por investigar, es una forma sencilla de integrar el sistema de versiones de github, y hacer mas sencillo mirar hacia atrás y ver el historial de todas las versiones publicadas.

En fin, queda mucho por investigar, pero avanzamos :)

---
layout: post
title: "¡Comenzamos Pilas Engine 2!"
image: "/images/2018/03/IMG_3696.jpg"
date: "2018-03-04 21:00:46"
---

Wooow, ¡Pilas está cerca de cumplir 8 años!, y semejante acontecimiento me hizo tomar valor para encarar un cambio muy grande que veníamos planeando con la comunidad hace tiempo: crear la versión 2 de Pilas Engine.

Desde que el proyecto comenzó el 1 de Agosto de 2010 pudimos transitar todos estos años mejorando y ayudando a un montón de personas a aprender a programar videojuegos. El motor creció, formamos una gran comunidad y aprendimos mucho.

Ahora tenemos la posibilidad de dar un salto de calidad muy grande: hacer una retrospectiva de lo que hemos aprendido, reforzar los puntos más fuertes de la herramienta y pensar en los desafíos que vienen.

### ¿Por qué estoy pensando en un cambio importante en pilas-engine?

Pilas 1 comenzó siendo un módulo de Python 2, y poco a poco fue incorporando funcionalidad hasta convertirse en un proyecto completo. Naturalmente las herramientas que teníamos disponibles para hacer pilas en aquellos años no son las mismas que podríamos elegir hoy, sin embargo lo pudimos llevar adelante.

Python es fabuloso, es mi lenguaje favorito, pero la nueva versión de pilas va a inclinarse hacia tecnologías web como javascript, no por el lenguaje en sí, sino por el ecosistema de herramientas que tiene la plataforma web en general: phaser, chrome, ember etc…

Usando esas tecnologías, Pilas Engine 2 podría funcionar sobre las mismas plataformas que lo hace hoy pilas 1, pero además podría funcionar sobre navegadores web y brindar muchas mejoras a la comunidad.

### Presentando el nuevo prototipo de Pilas

Esta idea de migrar pilas a la web no es nueva, hace tiempo que lo venimos conversando y hasta construí un prototipo de lo que podemos llegar a ver en una futura versión de Pilas.

Actualmente el prototipo tiene muy pocas cosas, pero es una base sólida para construir todo lo demás y permite visualizar las ventajas de la plataforma.

Si queres ir mirando lo que incluye hasta ahora podés visitar la siguiente web:

- https://app.pilas-engine.com.ar

En la web vas a ver algo similar a lo que aparece en las siguientes capturas de pantalla, solamente que las capturas fueron capturadas funcionando dentro de electron (una tecnología para empaquetar la aplicación completa y usarla de forma offline):

![](/images/2018/03/image_preview.png)

Dentro del prototipo también incluí una versión inicial del editor:

![](/images/2018/03/image_preview--2-.png)

### Pensando en metas

Los primeros pasos técnicos para iniciar la versión 2 están en camino: construir el prototipo inicial y crear una base sólida para encarar el desarrollo del motor.

Sin embargo, me pareció buena idea continuar este artículo compartiendo algunas metas que quisiera que guíen el desarrollo de pilas a futuro.

### Meta 1: Pilas 2 debe ser una herramienta para descubrir

Siempre tuvimos en mente que Pilas sea una herramienta para aprender a programar haciendo juegos, descubriendo conceptos y posibilidades técnicas a medida que se comienza a utilizar.

Pilas no es muy convencional en ese sentido, no se parece a aprender a programar o usar otras herramientas en donde se tiene que cumplir el requisito inicial de leer el manual o seguir una guía de primeros pasos. Tampoco es realmente necesario que un docente lo explique paso a paso; La meta de pilas es que el usuario pueda “descubrir la herramienta” usándola, por sí mismo, motivado por las ganas de crear un proyecto propio o grupal.

En otras palabras, creemos que el aprendizaje más significativo se produce cuando el usuario descubre y persigue el desarrollo de un proyecto.

Por eso, en la versión 2 podemos proponernos hacer que pilas sea mucho más fácil de descubrir mejorando el editor y la interacción con la escena que construye.

Por ejemplo, los actores tiene que estar a la vista, y las tareas típicas como posicionar actores tienen que ser fácilmente realizables (sin escribir código).

Un ejemplo de esto se ve en el diseño del nuevo editor, ahora se pueden crear actores visualizándolos previamente, mirándolos en una grilla, seleccionándolo y colocándolo en el escenario:

![](/images/2018/03/image_preview--1-.png)

Además, el editor tiene un modo de edición y ejecución completamente identificados. Para que el usuario pueda controlar a los actores, moverlos como si fueran piezas sobre un tablero y luego “ponerlos en acción” con el botón “Ejecutar”:

![](/images/2018/03/image_preview.gif)

Lo mismo sucede con los atributos de los actores, en la versión 2 estoy experimentando con un panel de propiedades que se puede modificar fácilmente:

![](/images/2018/03/image_preview--1-.gif)

### Meta 2: Que los usuarios puedan compartir sus juegos fácilmente

Un paso muy importante de nuestros usuarios es el momento en donde muestran su juego a otras personas; es un momento fascinante, porque es el que los pone en un rol protagonista frente a la tecnología, y le da un sentido completamente diferente sus proyectos. ¡Tiene que ser fácil mostrar nuestros juegos!.

Creo que una forma de lograrlo es agregando un botón al editor que permita generar una dirección web para compartir. Con eso los usuarios van a poder copiar y pegar esa dirección en el foro, facebook o donde quieran.

### Meta 3: Exponer el código completo de los actores

Un objetivo importante de Pilas es que los usuarios se “apoderen” del concepto de actores muy rápido, que puedan personalizar y crear sus propios actores.

Por eso en el prototipo de Pilas 2 experimenté con la idea de exponer el código completo de los actores al momento de crearlos, así el usuario va a poder cambiar y personalizar los actores sin necesidad de comprender jerarquía de clases de los actores o revisar el manual.

Por ejemplo, el actor nave ahora expone todo su código (no una clase derivada). Si el usuario quiere cambiar la velocidad de la nave o jugar con algún otro comportamiento lo puede hacer directamente ahí:

![](/images/2018/03/image_preview--3-.png)

### Meta 4: Mantener ambas versiones de Pilas

Hacer la versión 2 de pilas va a requerir muchísimo esfuerzo, pero no debería ser excusa para dejar de mantener la versión 1. Me gustaría que sigamos manteniendo activamente ambas versiones. Hoy existen muchos cursos, programas, tutoriales, juegos y usuarios usando la versión 1 de pilas.

El desafío aquí es más organizativo que técnico, requiere que nos organicemos para llevar los dos proyectos de la mano, y darle a los usuarios la posibilidad de elegir qué versión prefieren utilizar.

### Meta 5: Aprender y seguir divirtiéndonos creando Pilas Engine

Se que este último objetivo no es técnico ni formal, ¿pero qué importa?: pilas es un proyecto creado por personas, buscando transformar el rol de los jóvenes frente a la tecnología: queremos que sean protagonistas en lugar de espectadores. Es un proyecto lleno de desafíos y mucho trabajo por realizar.

Así que creo que debemos tenerlo como uno de nuestros principios más importantes: colaborar en el desarrollo de Pilas tiene que ser divertido y desafiante, necesitamos activamente de toda la comunidad para que sea un éxito.

La buena noticia es que formamos un grupo magnífico, tenemos perseverancia a pesar de todo el trabajo y las dificultades que trae aparejado .

Vamos a lograr que Pilas Engine llegue a ser mucho mejor de lo que soñamos.

### ¿Y cómo seguirá el desarrollo?

Seguramente en estos días comience a buscar colaboradores y conversar en el foro de pilas-engine sobre esta nueva iniciativa. Si estás interesado en participar escribí en el foro de pilas para que podamos organizarnos un poco mejor.

Además del foro de mensajes, también vamos a contar con un tablero de trello con las tareas a realizar:

- https://trello.com/b/eQJOjpOF/pilas-engine-2

Y el repositorio en donde vamos colocar todas las contribuciones:

- https://github.com/pilas-engine/pilas-engine

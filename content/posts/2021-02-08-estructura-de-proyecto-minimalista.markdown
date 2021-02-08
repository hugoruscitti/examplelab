---
layout: post
title: Una estructura de proyecto minimalista en TypeScript
date: '2021-02-08 00:00:00'
description: |
  Empezar a desarrollar un proyecto web se puede convertir
  en una tarea compleja, con dependencias y archivos
  de configuración. En este post intentaré mostrar
  una alternativa modesta.
cover: /images/2021/estructura-de-proyecto-minimalista/portada.jpg
---

Hace algunos meses me empecé a interesar en formas simples
en hacer proyectos en JavaScript, leí el libro [Modest JS Works](https://modestjs.works/book/part-1/intro/)
y también empecé a usar algunas ideas de [The VanillaJS Toolkit](https://vanillajstoolkit.com/).

Realmente extraño la sensación de hacer aplicaciones completas por mi mismo,
sin depender de cientos de megabytes en dependencias, frameworks
sofisticados y un ecosistema de herramientas que están cambiando
todo el tiempo.

# ¿Por qué?

Hace unos años, podías escribir un sistema completo por tu propia cuenta,
necesitabas Apache, PHP, un editor de textos y ganas de programar. 

Incluso si recién estabas aprendiendo a programar, las herramientas hacían
muy poquito por vos, pero aún así podías concentrarte en tu aplicación y no tanto
por todo lo demás.

Hoy la historia es un poco diferente, hubo un cambio de cultura muy grande
entre los desarrolladores web; no se muy bien por qué, pero ahora parece
que la forma más aceptada de iniciar un proyecto web es elegir un framework, instalar
dependencias con npm, configurar tu IDE y algunas cosas más. 

Pienso que la forma en la que trabajan las empresas grandes y los equipos altamente
capacitados influenciaron a todo el mundo. Como si sus ideas se hubieran vuelto
el "nuevo estándar" a la hora de hacer software.

# Un enfoque simple

Estrictamente hablando, al navegador no le importa cómo vas a construir tu aplicación
web, el navegador interpreta HTML, CSS y JavaScript, independientemente de cómo
lo escribas.

A mí me gusta la idea de no tener demasiadas dependencias, sobre
todo si soy el único desarrollador y cada actualización o problema de configuración
lo tengo que arreglar por mí mismo.

Entonces, un proyecto se puede iniciar con 3 archivos, "index.html", "app.js" y "app.css":

```
→ ls 
app.css     app.js      index.html
```

Y conforme necesite más, puedo ser conciente de qué piezas me conviene
agregar y si realmente me benefician a no.

# Un webserver en modo desarrollo

Una de las piezas que me gusta tener a la hora de programar es un servidor
web que actualice el navegador cada vez que realizo cambios en los archivos
del proyecto.

Para eso utilizo [este comando](https://www.npmjs.com/package/live-server) que
instalé de forma global en mi sistema:

```
live-server
```

Esto es un "chiche" en realidad, porque solamente me ahorra cambiar
de ventana y pulsar cmd+r para recargar la página. 

Sin embargo para mí esto añade algo de diversión y comodidad, porque puedo
permanecer en el editor y asegurarme que el navegador siempre me muestra
la versión más reciente de la aplicación.

:TODO: Pantalla con editor y navegador a la derecha.

# Modularizar usando TypeScript

:todo

# Autocompletado con vim

:todo

# ¡Pero necesito componentes web!

:todo

# Conclusión

:todo

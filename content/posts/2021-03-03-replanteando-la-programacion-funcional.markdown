---
layout: post
title: Replanteando la Programación Funcional
date: '2021-03-03 00:00:00'
description: |
  Si miramos a la programación funcional como una serie
  de herramientas y habilidades podemos tomar muchas cosas
  de ahí para simplificar gran parte de nuestro trabajo.
cover: /images/2021/replanteando-la-programacion-funcional/portada.jpg
tags:
- reflexión
- programación
---

Esta semana escuché una [entrevista a Eric Normand](https://changelog.com/jsparty/163)
en donde describía la programación funcional de una manera completamente
diferente para mí.

Resulta que mis nociones de programación funcional vienen de mi paso por la facultad
de ingeniería, donde descubrí la programación funcional en una materia llamada Paradigmas
de Programación.

En esa materia abordamos la programación funcional desde sus fundamentos, usando
[haskell](https://www.haskell.com/) y resolviendo ejercicios para familiarizarnos con el enfoque
del paradigma. Estos ejercicios consistían en cálculos matemáticos, operaciones con listas
de números, algoritmos recursivos y esas cosas...

Y por lo que mencionan en la entrevista, en otras partes del mundo también se aborda la
programación funcional desde ese enfoque:

<audio controls>
  <source src="../2021-03-03-replanteando-la-programacion-funcional/audios/programacion-funcional-se-complica-demasiado.ogg" type="audio/ogg">
  <source src="../2021-03-03-replanteando-la-programacion-funcional/audios/programacion-funcional-se-complica-demasiado.mp3" type="audio/mpeg">
</audio>

Sin embargo, mientras escuchaba la entrevista, noté que muchas de mis ideas
sobre programación funcional se podrían abordar de otra manera. Existe un enfoque más
práctico sobre programación funcional que puedo empezar a aplicar desde hoy, incluso
usando un lenguaje como JavaScript o Python, que nos son lenguajes puros del paradigma
funcional.

## Revalorizando ideas de la Programación Funcional

Eric Normand describe la programación funcional así:

> Es una serie de skills, ideas que nos permiten pensar en la programación
> de manera más simple y accesible.

Y creo que su enfoque está bueno, porque no traza una linea para decir "esto es funcional" y "esto
no es funcional", no introduce temas como fundamentos matemáticos, funciones puras, efecto colateral, etc... Tampoco
entra en el debate de *pureza* del paradigma o sus ideas.

Con su definición, tranquilamente se puede introducir programación funcional dentro de
un sistema en desarrollo. La clave está en definirlo como una serie de "habilidades".

La definición formal de programación funcional no es práctica.

Si le decís a alguien que buscas introducir programación funcional en un sistema podría
hacerse una idea diferente de lo que tenes en mente, esa persona podría 
pensar que buscas eliminar cualquier "efecto colateral" o re-escribir la arquitectura
por completo.

¿Evitar efectos colaterales?, ¿y cómo vamos a guardar cosas en una base de
datos?, ¡Si ese es el motivo por el que estamos escribiendo este software!

Creo que esta ilustración del libro [Grokking Simplicity](https://www.manning.com/books/grokking-simplicity)
lo resume muy bien:

![](/images/2021/replanteando-la-programacion-funcional/toon.png)


## Otra forma de ver a la programación funcional

Una de las habilidades que menciona Eric consiste en comenzar
a distinguir estas tres cosas:

1. Actions
2. Calculations
3. Data

**Actions** son aquellas partes del sistema que producen un impacto
externo, como guardar un registro en una base de datos, enviar un
email o alterar una estructura de datos. Estas partes del sistema son las más
complejas, porque para probarlas necesitamos "que el entorno esté ahí". 

**Calculations** son funciones puras, que producen un valor a partir
de una serie de parámetros. Se las puede llamar muchas veces y es fácil
replicar su funcionamiento cuando escribimos un test.

**Data** son datos inertes, que fácilmente podemos guardar, graficar o
analizar de distintas formas. Son hechos, o resultados que se generaron
a partir de una operación.

Esta distinción es muy práctica, porque las **actions** suelen ser 
problemáticas, pero son indispensables, no podemos quitarlas del sistema. Lo
más valioso del software son estas acciones.

En cambio, las **calculations** son más fáciles, y nos pueden servir para
quitarles *responsabilidad* a la **actions** del sistema.

Y esta es una de las cosas que sostiene Eric: si tratamos de mover la mayor
parte del código a **calculations**, podemos reducir la cantidad de cosas
*difíciles* en nuestro código. Es inevitable tener **actions**, pero sí
podemos evitar que hagan demasiadas cosas.

En otras palabras, lo que podemos tomar de la programación funcional es
estas habilidades para hacer nuestro código *fácil* de probar. Todo comienza
con esta distinción, análisis y disciplina.

Este es un recorte que hice la entrevista donde Eric menciona cómo
poner en práctica estas ideas:

<audio controls>
  <source src="../2021-03-03-replanteando-la-programacion-funcional/audios/el-objetivo-de-la-programacion-funcional-es-quitar-carga-sobre-las-acciones-y-simplificar-cosas.ogg" type="audio/ogg">
  <source src="../2021-03-03-replanteando-la-programacion-funcional/audios/el-objetivo-de-la-programacion-funcional-es-quitar-carga-sobre-las-acciones-y-simplificar-cosas.mp3" type="audio/mpeg">
</audio>

Creo que es muy interesante revisar estas ideas, por mi parte voy a tomarme el
tiempo y esfuerzo para maximizar la proporción de código dedicado a **calculations**
y reducir la cantidad de **actions**.

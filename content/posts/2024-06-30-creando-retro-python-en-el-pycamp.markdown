---
layout: post
title: Creando retro-python en el PyCamp
date: '2024-06-30 18:00:00'
description: |
  Un breve recorrido por la idea y los primeros prototipos
  de retro-python
cover: /images/2024/creando-retro-python-en-el-pycamp/portada.jpg
---

El fin de semana pasado participé del PyCamp, un evento de 4 días
organizado por amigos de la comunidad de PyAr (Python Argentina):

![](/images/2024/creando-retro-python-en-el-pycamp/foto-grupal.jpeg)

Volví muy entusiasmado y con mucha felicidad de haber disfrutado cada momento,
para mí el PyCamp es un evento único, me deja ilusionado y con muchas ganas de
inventar cosas nuevas.

# Sobre retro-python

Uno de los proyectos en los que trabajamos fue `retro-python`, una idea que
propuse unos días antes de comenzar el evento y que resultó muy bien, ya que
pudimos crear la herramienta y publicarla para mostrar al final del evento:

https://retro-python.com.ar

Con **retro-python** se pueden crear dibujos, animaciones y juegos usando Python
y algo de código como se ve aquí:

![](/images/2024/creando-retro-python-en-el-pycamp/cielo.png)

Estas son algunas de las creaciones que se pueden hacer:

![](/images/2024/creando-retro-python-en-el-pycamp/creaciones.png)

Muchas de estas creaciones están animadas, podés verlas en funcionamiento
visitando la [página de la herramienta](https://retro-python.com.ar) y haciendo
*click* en los ejemplos:

![](/images/2024/creando-retro-python-en-el-pycamp/ejemplos.png)

# Acerca de la idea

La idea inicial del proyecto fue crear un entorno de programación que permita a
las personas crear un programa para dibujar o producir animaciones, todo en una
pantalla de píxeles similar a una computadora antigua.

Este es uno de los bocetos que usamos para comenzar:

![](/images/2024/creando-retro-python-en-el-pycamp/boceto.png)

A la izquierda está la pantalla con el resultado de ejecutar el programa y a la
derecha está el código que introduce el usuario.

Mi inspiración vino principalmente de otra herramienta llamada pico-8
(https://www.lexaloffle.com/pico-8.php) y mi recuerdo de las clásicas revistas
de computación de los años 80, donde podías encontrarte con un listado de
código, copiarlo en tu Commodore 64 y ver algo hermoso en la pantalla:

![](/images/2024/creando-retro-python-en-el-pycamp/pagina.png)

> página de la revista Input publicada en 1983
> ([ver en archive.org](https://archive.org/details/Input_Vol_1_No_01_1997_Marshall_Cavendish_GB/page/n17/mode/2up)),
> donde se muestra un código que podíamos escribir en nuestra computadora y el
> resultado en pantalla.

Yo nací en 1983, así que me perdí una parte grande de esta época dorada de las
revistas y el descubrimiento de la programación en Basic. Sin embargo, pensé en
este proyecto como una forma de recuperar algo de todo eso que se perdió en los
80s: la posibilidad de curiosear, crear dibujos en la pantalla o de "jugar"
creando animaciones a partir de números, funciones y píxeles.

# ¿Cómo empezamos a implementar retro-python?

Unos días antes de comenzar el evento, las personas que vamos a participar del
PyCamp escribimos en el foro de PyAr una propuesta del proyecto en el que nos
gustaría participar:

Esta es una captura de pantalla de lo que escribí en el foro:

![](/images/2024/creando-retro-python-en-el-pycamp/propuesta-en-el-foro.png)

Luego, cuando comenzó el evento volvimos a charlar de los proyectos y nos
comenzamos a organizar en equipos de personas interesadas en participar en cada
proyecto:

![](/images/2024/creando-retro-python-en-el-pycamp/trabajando.png)

*retro-python* tuvo varias colaboraciones y personas que se interesaron y
implementarlo, en particular 4 personas estuvimos en el día a día de la creación
de retro python

![](/images/2024/creando-retro-python-en-el-pycamp/equipo.jpeg)

En la foto estamos (de izquierda a derecha): José Cabrera, Hebert Ferrer, yo
(Hugo Ruscitti) y Luis Cova.

También fue muy importante para mí hablar con osiux y rodo de
[gcoop](https://gcoop.coop), ya que me dieron muy buenas ideas y acompañaron con
pruebas y mejoras.

### El futuro de retro-python

Mi idea a futuro es dedicar algunas horas los fines de semana a crear algunas
mejoras para retro-python, al menos mantener el proyecto funcionando y que se
pueda usar.

De hecho, creo que puede ser un lindo proyecto para llevar al próximo PyCamp;
tal vez puedo pensar en alguna característica nueva y proponerla como proyecto.

Me gustaría cuidar del proyecto y mantenerlo cuidadosamente, así como hago con
[pilas-engine](https://pilas-engine.com.ar/), mi intensión es verlo crecer
de forma sostenida y por amor a las cosas que me gusta hacer y compartir.

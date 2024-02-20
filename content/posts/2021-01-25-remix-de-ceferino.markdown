---
layout: post
title: Haciendo un Remix del juego Ceferino
date: '2021-01-25 00:00:00'
description: |
 Hice una versión renovada del juego Don Ceferino
 Hazaña usando pilas-engine para la web.
cover: /images/2021/ceferino/portada.jpg
tags:
- juegos
- pilas
---

[Don Ceferino Hazaña](http://losersjuegos.com.ar/juegos/ceferino) es uno de los
primeros juegos que hicimos con Walter Velazquez allá por el año 2004:

![](/images/2021/ceferino/capturas.png)

Creo que fue uno de los juegos a los que más tiempo y ganas le dedicamos, yo
apenas estaba aprendiendo a programar así que me costó el triple de lo que
esperaba al principio. Fue una de las primeras estimaciones "fallidas" de mi
vida, imaginé que el juego completo se podría hacer en "un par de semanas", y
casi estuvimos un año entero haciéndolo :P


{{<figure src="/images/2021/ceferino/piezas.png" caption="Wally armaba los sprites separados por piezas en Animator Pro">}}

También fue uno de los primeros proyectos que pudimos empezar
y terminar completos; no es fácil conservar el entusiasmo cuando
el desarrollo de un proyecto se extiende por tanto tiempo.

Sin embargo, al juego le guardo muchísimo cariño, y cuando lo recordé
y quise jugarlo, ya no era nada fácil recompilarlo y jugar. 

Así que se me
ocurrió traerlo al futuro, crear una versión renovada del juego lo más
parecida a la original pero que funcione directamente en el navegador.

Además, me pareció un buen experimento hacerlo completamente en
[pilas-engine](https://www.pilas-engine.com.ar), así podría poner a prueba la
herramienta y ver qué mejoras surgían en el camino.

# Primeras pruebas

Los movimientos básicos del personaje fueron la parte más fácil de hacer,
pilas tiene un editor de animaciones que es muy práctico, no hace falta
que las imágenes de los personajes estén en una grilla sino que se pueden
incorporar por separado:

{{<figure src="/images/2021/ceferino/animacion.png" caption="Editor de animaciones de Pilas">}}

Además, hay algunos conceptos que aprendí desde que empecé a hacer
pilas que en su momento no conocía. Ahora casi siempre que hago
que los personajes puedan detectar suelos o colisiones suelo usar
lasers (o raycasts):

{{<figure src="/images/2021/ceferino/lasers.png" caption="Ceferino tiene dos lasers para detectar colisiones con el suelo">}}

Estos lasers los incorporé a pilas hace unos meses, pero los venía
usando en otro motor de juegos llamado Unity hace algunos años. Hacer
juegos sin estos lasers era mucho más difícil cuando hicimos el Ceferino
original.


# Armando todo por separado

Otra cosa que me ayudó un montón al momento de hacer
esta nueva versión fue poder trabajar en los actores
del juego por separado.

El protagonista lo compuse en una escena, los enemigos
del nivel en otra y así.

{{<figure src="/images/2021/ceferino/escena-de-enemigos.png" caption="Los enemigos en su propia escena">}}

Y como estas escenas nunca la ve el jugador, funcionan como una paleta de
actores personalizados.

Este es otro ejemplo, para armar el escenario hice pequeños actores que representan todos
los elementos que se pueden ver en la pantalla. Pude trabajar sobre cada uno de estos
actores y despreocuparme por los enemigos o el protagonista, cada vez que quería mejorar
alguno de estos bloques abría la escena en donde estaban estos y simplemente mejoraba
su código o alguna propiedad:

{{<figure src="/images/2021/ceferino/bloques.png" caption="Todos los actores que se utilizan para crear mapas">}}


# Adaptando los niveles

El juego original tenía 30 niveles, y como mi intención era hacer una versión
lo más fiel a la original, me propuse adaptar cada uno de los niveles originales.

Al principio imaginé copiarlos uno a uno, ya que el formato era muy diferente. Los
niveles originales estaban en formato binario, que eran mucho más fáciles de crear y
cargar en la versión original, mientras que los niveles para
la versión nueva de pilas tenían que estar en formato texto ([como se
describe en el manual](https://app.pilas-engine.com.ar/#/manual?seccion=mapas)).

Luego, probando el juego original y revisando los niveles me dí cuenta que 30
niveles no es poco, ¡y qué aburrido se veía copiar uno a uno los niveles!.

Así que me propuse editar el código del juego original para que me convirtiera los
niveles a texto. Lo hice de esta forma: tomé una virtual de linux, bajé
el código fuente del juego original, edité el código y lo volví a compilar.

{{<figure src="/images/2021/ceferino/linux.png" caption="El editor de niveles de ceferino corriendo en una máquina virtual">}}

Me llevó como 2 horas encontrar en el código dónde se cargaban los niveles, pero una
vez que lo encontré esto lo demás fue muy fácil. Terminé cambiando el código del editor de
niveles que había hecho para la versión original e imprimiendo todo el mapa en consola
así:

{{<figure src="/images/2021/ceferino/niveles.png" caption="Nivel pasado a texto">}}

El texto de cada nivel no era exactamente lo que podía cargar dentro de la versión
nueva de pilas, pero por lo menos era texto, así que lo podía leer con algún script
y convertir a lo que quisiera.

Así que armé un script en python que convertía esos números en identificadores de bloques
y los copié en el editor de pilas:

{{<figure src="/images/2021/ceferino/nivel.png" caption="Nivel como mapa dentro de pilas">}}

El formato de niveles de la versión nueva de pilas es un poco raro a simple
vista, pero es super útil. Cada letra que aparece en el mapa
representa un actor.

Pilas sabe a qué actor corresponde cada letra mediante este diccionario:

{{<figure src="/images/2021/ceferino/mapa.png" caption="Diccionario para componer el nivel">}}

y como ese diccionario es configurable, resulta muy flexible, se pueden agregar
tipos de actores fácilmente y realizar ajustes rápidos.

# Ideas a futuro

Me quedé con ganas de recuperar varios juegos de aquellos años, incluso
habíamos hecho [juegos con DIV](http://losersjuegos.com.ar/juegos) y que
ahora son casi imposibles de ejecutar en una computadora nueva sin usar
un emulador de ms-dos.

Me parece una buena idea recuperar esos juegos, no solo por los juegos
en sí, sino porque me despiertan muchos recuerdos y ganas de seguir
aprendiendo sobre videojuegos.

¡Hasta el próximo post!

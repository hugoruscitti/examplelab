---
layout: post
title: Tortugas en el tiempo
date: '2020-08-08 00:00:00'
description: En este artículo describo como realicé un pequeño editor de código que permite ejecutar código para dibujar en pantalla, recreando parte de la clásica tortuga de Logo e investigando sobre ideas de aprendizaje y código.
cover: /images/2020/08/portada.jpg
tags:
- proyecto
- web
---

En este artículo describo como realicé un pequeño editor de código que permite ejecutar código para
dibujar en pantalla, recreando parte de la clásica tortuga de Logo e investigando sobre ideas de
aprendizaje y código.

![](/images/2020/08/inicio.png)

Podes ver el proyecto aquí:

- https://hugoruscitti.github.io/tortugas-en-el-tiempo

<style>
video {
  width: 100%;
  border: 1px solid gray;
  margin-top: 0.5em;
  margin-bottom: 0.5em;
}
</style>


## Motivación

Hace algunos años vi una charla llamada [“Inventing on Principle”](https://youtu.be/e7QYMgSk9s0)
que me dejó con varias inquietudes a la hora de pensar sobre cómo programamos computadoras y
pensamos acerca del código.

En esta charla Bret Victor comienza mencionando una situación típica de nuestra profesión:

> Así es como programamos: escribes un montón de código en un editor de textos, tratas de imaginar
> en tu cabeza que hará cada linea de código. Luego lo compilas, ejecutas y algo sucede. Pero si
> algo sale mal, tienes que ir devuelta al código.

y sigue con una frase que me quedó resonando en la cabeza:

> La mayoría del tiempo estamos frente al código, trabajando a ciegas en un editor de texto, sin tener una conexión con lo que estamos haciendo.

Y da un ejemplo adicional:

![](/images/2020/08/034947C6-A4E5-4B97-9633-E80CDE1C5ABF.png)

> […] La búsqueda binaria se ve así. Desde mi perspectiva, aquí no se puede ver nada. Veo la
> variable “array” pero no veo su contenido. Entonces, para escribir código de esta manera, tienes
> que imaginarte un array en tu cabeza, y esencialmente debes jugar a ser una computadora, debes
> simular en tu cabeza lo que cada líneas de código haría en la computadora. Y las personas que
> consideramos hábiles desarrolladores de software son solamente aquellas personas que son hábiles
> jugando a ser computadoras.
>
> Pero para escribir código en la computadora… ¿Por qué simulamos lo
> que haría la computadora en nuestra mente?, ¿Porqué simplemente no lo hace la computadora y nos
> muestra?
>
> (https://youtu.be/e7QYMgSk9s0?t=1043)

Luego de ver esta charla me quedé con una sensación incómoda con respecto al código y cómo
programamos. Pienso que estas ideas son una suerte punto de partida para pensar y diseñar formas
nuevas de programación.

¿Cómo podríamos diseñar una interfaz que acompañe a desarrollares a entender sus programas?, ¿Qué
elementos de un programa podemos hacer “visibles” a los usuarios?

## Pensando en un proyecto

Pienso que desde que vi esa charla comencé a ver las herramienta de otra forma, re diseñe
[Pilas](https://www.pilas-engine.com.ar) “dando vueltas” muchas cosas, y hasta hoy sigo imaginando cómo
resolver los problemas que plantea Bret Victor.

No es sencillo abordar todo lo que plantea en su charla, hacer visible el contexto de un programa y
permitirle a las personas manipular directamente sus programas es muy desafiante, y se requiere
práctica.

Así que en búsqueda de tener algo de práctica con estas ideas y como excusa para volver a leer
textos como [Learnable Programming](http://worrydream.com/LearnableProgramming/) me propuse crear
una herramienta de programación similar a
[logo](https://es.wikipedia.org/wiki/Logo_(lenguaje_de_programación)), pero mucho más acotado, y
con algunas mejoras como el resaltado de código, la posibilidad de realizar una depuración paso a
paso y algunas cosas más.

## ¿Qué permite hacer esta herramienta?

La herramienta te permite realizar dibujos controlando la tortuga que aparece en pantalla usando
código.

![](/images/2020/08/E9158063-9158-4D4E-9B95-21A084A572F4.png)

La tortuga solo entiende unas pocas palabras, como “avanzar”, “girarDerecha” o “cuadrado”; pero se
le pueden enseñar más palabras creando funciones nuevas.

Sin embargo, lo interesante es que cada una de las acciones que realiza la tortuga se pueden
visualizar progresivamente, mientras el código se resalta para mostrar qué linea de código está
siendo ejecutada.

<video preload="false" controls>
  <source src="/videos/2020/08/ejecucion.mp4" type="video/mp4">
  <source src="/videos/2020/08/ejecucion.webm" type="video/webm">
</video>

Además, una vez que termina la ejecución del programa el usuario puede pulsar el botón “pausa” y
revisar la ejecución del programa retrocediendo o avanzando en el tiempo:

<video preload="false" controls>
  <source src="/videos/2020/08/depuracion.mp4" type="video/mp4">
  <source src="/videos/2020/08/depuracion.webm" type="video/webm">
</video>

## Bucle principal

Una característica que me interesaba re-crear para las personas que usen esta herramienta es poder
ver cómo se produce el dibujo de manera gradual, como si estuviera dibujando sobre una pizarra con
un marcador:

<video preload="false" controls>
  <source src="/videos/2020/08/screencast.mp4" type="video/mp4">
  <source src="/videos/2020/08/screencast.webm" type="video/webm">
</video>

Obviamente es mucho más sencillo crear un entorno en donde el código se ejecuta al instante, de
forma sincrónica, sin embargo eso hubiera hecho que el programa se vuelva mucho más difícil de
entender. Cuando el código se ejecuta inmediatamente las personas se ven obligadas a “pensar como
una computadora” para entender qué está haciendo el código.

Así que fui directo por una implementación similar a la que se realiza en el desarrollo de
videojuegos, creando un temporizador que mantiene la escena “viva” dibujado una y otra vez la
posición de la tortuga y reaccionando a los cambios de atributos.

![](/images/2020/08/game-loop.png)

Tener un temporizador encargado de dibujar la pantalla hace que el resto del sistema sea mucho más
simple, porque a partir de ahí cualquier cambio que realicemos a la tortuga se va a reflejar en el
canvas automáticamente.

Por ejemplo, esta es una de las primeras pruebas que realicé, en donde puse a funcionar el bucle
principal y comencé a editar la estructura de datos que representa la tortuga con algunos
controladores:

<video preload="false" controls>
  <source src="/videos/2020/08/propiedades.mp4" type="video/mp4">
  <source src="/videos/2020/08/propiedades.webm" type="video/webm">
</video>

Es decir, con solo alterar alguno de esos atributos de forma directa el usuario va a percibir
“movimientos” graduales en lugar de cambios inmediatos.

## Dibujado en pantalla

Para realizar dibujos utilicé el elemento [Canvas de
HTML](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial), pero en lugar de usar
un solo elemento tuve que usar dos separados.

![](/images/2020/08/8291458D-A0AE-4DE5-AB43-A6AEB2FDF874.png)

La razón por la que tuve que separarlos es porque quería poder controlar la tortuga como si se
tratara de un Sprite de video juego, pudiendo moverlo o aplicándole transformaciones fácilmente por
un lado, y por otro lado lograr que el dibujado que hace el usuario sobre la pantalla quede estable
sin necesidad de volver a dibujarlo.

Después de todo, por más que se trate de dos elementos diferentes, es fácil mostrarlos solapados,
uno arriba del otro, como si se tratara de “capas” de la misma porción de la pantalla.

## Modo pausa

El editor también incluye una funcionalidad para detener la ejecución del programa y analizar paso
a paso qué movimiento realizó la tortuga.

Para activar este modo hay que ejecutar el programa y luego pulsar el botón “Pausar”:

![](/images/2020/08/950D1711-7C1E-44F2-84DC-133112873C91.png)

En ese punto, el editor ingresa en un modo especial, en donde el usuario puede manipular una linea
de tiempo para revisar el movimiento de la tortuga. Y no solo el movimiento, también puede ver qué
linea de código se ejecutó en ese instante:

<video preload="false" controls>
  <source src="/videos/2020/08/modo-pausa.mp4" type="video/mp4">
  <source src="/videos/2020/08/modo-pausa.webm" type="video/webm">
</video>

Ahora bien, ¿cómo está implementada esta funcionalidad?: El entorno tiene una lista en memoria en
donde va guardando cada una de las acciones que hace la tortuga.

Esta lista se podría ejemplificar así: imagina que tenemos un código que dibuja un triángulo:

![](/images/2020/08/861E3835-CA41-4523-953D-94A2D1C4A4BE.png)

Cuando pulsamos el botón ejecutar la lista debería quedar con un solo elemento, la posición inicial
de la tortuga:

```
pasos = [
	{
		tipo: "posicion-inicial",
		x: 150,
		y: 150,
		lapiz: "abajo",
		# rotación, etc ...
	}
]
```

Luego, como el programa está en ejecución se va a procesar la linea que dice `avanzar(50)` y cuando
terminé de realizarse esa acción, se va a añadir este elemento a la lista:

```
lista.push({
	tipo: "movimiento-de-dibujado",
	x: 150,
	y: 200,
	lapiz: "abajo",
	# rotación, etc ...
})
```

Es decir, cada acción va a añadir un elemento en esta lista de pasos, detallando la posición de la
tortuga y algunos atributos mas. Con solo guardar esos datos alcanza para “recrear” toda la escena
una vez que se activa el modo pausa.

Este video muestra una versión más completa de esta estructura de datos y cómo se van a agregando
elementos a la lista de pasos:

<video preload="false" controls>
  <source src="/videos/2020/08/pasos-del-depurador.mp4" type="video/mp4">
  <source src="/videos/2020/08/pasos-del-depurador.webm" type="video/webm">
</video>

Por cierto, esta estrategia de depuración también la implementé en [Pilas Engine
2](https://www.pilas-engine.com.ar), donde incluso puede haber muchos actores en movimiento
interactuando entre sí:

<video preload="false" controls>
  <source src="/videos/2020/08/depuracion-en-pilas.mp4" type="video/mp4">
  <source src="/videos/2020/08/depuracion-en-pilas.webm" type="video/webm">
</video>


Ah, y como dato curioso, incluso algunos videojuegos usan esta técnica de guardar el estado del
programa para realizar efectos de repetición (como los juegos de fútbol) o incluso para lograr
mecánicas como el control de tiempo. Pienso que el juego
[Braid](https://www.youtube.com/watch?v=R9Exh6uhJno) es el mejor ejemplo de esto, incluso hay una
charla de su autor [explicando cómo está implementada esa
característica](https://youtu.be/8dinUbg2h70?t=408) por si te resulta interesante para investigar.

## Editor de código

En las primeras pruebas de este proyecto comencé trabajando con un elemento de tipo HTML TextArea
simple, pero al poco tiempo noté que para escribir código necesitaba números de lineas, coloreado
de sintaxis y alguna forma de resaltar lineas.

Así que armé un componente de VueJS basado en [Monaco
Editor](https://microsoft.github.io/monaco-editor/index.html), una biblioteca que provee un editor
de código muy completo, con soporte de auto-completado, resaltado de sintaxis y varias opciones de
configuración para utilizarlo en donde sea.

Una de las características de Monaco que más exploré es la posibilidad de configurar el módulo de
auto-completado; de hecho resultó ser más sencillo de lo que imaginaba, simplemente tenemos que
enviarle las definiciones de funciones a Monaco así:

![](/images/2020/08/editor.png)

Esta definición alcanza para que el editor autocomplete el nombre de las funciones, detecte errores
y nos muestre documentación de cada función:

![](/images/2020/08/4A9FD284-3E0F-428D-B86B-33738E872D61.png)

## Código visible

Algo que menciona Bret Victor [en el ensayo que mencioné
antes](http://worrydream.com/LearnableProgramming/) es que las funciones y elementos del lenguaje
deberían estar a la vista de las personas. Así que intenté explorar la posibilidad de colocar las
funciones disponibles para utilizar en un panel a la derecha del editor:


<video preload="false" controls>
  <source src="/videos/2020/08/ingresar-codigo-desde-panel.mp4" type="video/mp4">
  <source src="/videos/2020/08/ingresar-codigo-desde-panel.webm" type="video/webm">
</video>

Igualmente, siento que este panel de funciones se podría mejorar un montón; me imagino que se le
podría presentar a las personas una previsualización de qué hace cada función, algo más de
información sobre sus parámetros o algo de documentación.

## Resaltado de código al ejecutar

Pienso que lo más importante de este prototipo es que logra resaltar las lineas de código cada vez
que la tortuga realiza una acción:

![](/images/2020/08/B9CC4EA7-4016-4E5A-82EA-B0574B289396.png)

Para implementar esta característica utilicé una biblioteca JavaScript llamada
[JS-Interpreter](https://neil.fraser.name/software/JS-Interpreter/docs.html). Esta biblioteca te
provee de una clase llamada `Interpreter` que se puede configurar para ejecutar código paso a paso.

Este es un ejemplo básico de lo cómo se puede enviar código a esa clase e iniciar la ejecución del
programa:

![](/images/2020/08/interpreter.png)


A grandes rasgos parece similar a tener el código en una cadena de texto como
`código` y luego llamar a `eval(código)`.

Sin embargo, este intérprete hace mucho más que eso:

Una de las características que incluye es la posibilidad de ejecutar código de manera aislada del
resto de entorno, así que podemos controlar qué cosas puede ejecutar el código que le enviemos
limitando el acceso a objetos o APIs que nosotros queramos.

De hecho, este intérprete nos permite vincular funciones asincrónicas y que el programador las
perciba como simples funciones sincrónicas.

Por ejemplo, el movimiento de la tortuga se ve como una función muy sencilla: `avanzar(20)`, pero
internamente se implementó como un comportamiento asincrónico, que gradualmente va avanzando pixel
a pixel y dibujando hasta que la tortuga llega al punto solicitado:

![](/images/2020/08/secuencia.png)

Algo que también permite este intérprete es analizar el programa completo y saber qué linea de
código está ejecutando en cada momento, cosa que utilicé para resaltar el código del editor.

## Conclusión

Hacer este experimento me sirvió muchísimo… pude volver a leer algunas ideas de Seymour Paper, de
Bret Victor y ver varios videos de Logo.

También me sirvió para aprender a utilizar VueJs, Monaco y Cypress de forma práctica, con un
proyecto realizable en manos.

Además, si bien se trata de un programa muy pequeño (e incompleto si lo comparamos con una
herramienta de verdad) me dio mucho impulso para programar algunos experimentos nuevos.

Hasta la próxima, ¡y gracias por leer!

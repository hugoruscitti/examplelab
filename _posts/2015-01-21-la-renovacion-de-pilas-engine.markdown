---
layout: post
title: La renovación de pilas-engine
image: "/images/2015/01/DSCN1110.JPG"
date: '2015-01-21 02:26:10'
---

Estamos muy cerca de lanzar la versión ``0.91`` de *pilas-engine*, así que me pareció buena idea compartir en el blog las características más importantes de esta nueva versión y contarte el por qué de estos cambios.

Esta es una versión muy especial, principalemente porque añadimos muchos cambios en la estructura completa del motor.

Por supuesto no hice estos cambios solo. Irving, Quique Porta, Fernando Salamero, Walter Velazquez y el equipo de HuayraLinux hicieron posible esta nueva versión.

## ¿Por qué refactorizar?

En las primeras versiones del motor, [pilas-engine](http://www.pilas-engine.com.ar) no era una herramienta que incluía manual, interfaz gráfica o intérprete. [pilas-engine](http://www.pilas-engine.com.ar) era sólo un módulo de python que podía ser utilizado desde la consola estándar de python.

Por ese motivo, algunas cosas eran globales y estaban pensadas para tener un solo punto de salida: el cierre del proceso (mediante "sys.exit")

![](/images/2015/01/image04.jpg)

Pero cuando el proyecto comenzó a crecer, nos dimos cuenta que a muchos chicos no les resultaba muy atractivo el intérprete estándar de python, y con mucha razón: el intérprete de python no tiene colores, no cuenta con autocompletado, los errores están en inglés etc ...

Así que poco a poco fuimos implementando nuestro propio intérprete python, una ventana que sirva de punto inicial y muchas cosas más. Por eso, al seguir en esa dirección, pilas comenzó a convertirse en un entorno de desarrollo, incorporando un manual, ejemplos, modos para realizar depuraciones y todo eso buscando una experiencia uniforme para los sistemas Linux, Mac y Windows.

![](/images/2015/01/image01.png)

Pero en este punto, se hacía muy difícil construir arriba de la arquitectura inicial, necesitábamos abordar un enfoque diferente: usando componentes que pudieramos poner a prueba con tests y reduciendo los *hacks* al mínimo...

Incluso hace unos años, cuando armé el proyecto *patín* tuve problemas similares al querer re-iniciar pilas...

![](/images/2015/01/image09.png)


## Ahora, pensando en integrarse

A diferencia de la primer arquitectura, donde muchas variables eran globales al módulo, en esta nueva versión buscamos representar a **pilas** como un objeto, y no como un módulo.

La idea de “hablar” con **pilas** como un objeto es poder *iniciar*, *pausar*, *reiniciar* o descartar el contexto de **pilas** tantas veces como sea necesario. Además nos permitirá integrarlo con mayor facilidad a otras interfaces.

Este es un ejemplo en donde se inicializa pilas como un componente para una interfaz:

	import pilasengine

	pilas = pilasengine.iniciar()
	widget = pilas.obtener_widget()

En este punto, podríamos usar el objeto “widget” dentro del intérprete:

![](/images/2015/01/image07.png)

Esta facilidad de integración también simplifica un poco la tarea de empaquetado para otras plataformas, gnu/linux no dá muchos problemas, pero en Mac osx y Windows aparecen varios problemas: la forma en la que inicializamos el intérprete producía errores difíciles de capturar, teníamos que lidiar con manejo de múltiples instancias en memoria de pilas y procesos para sortear este problema de diseño.

## Un solo motor: pyqt

Una de las cosas que había planificado inicialmente en pilas es soportar varias bibliotecas por debajo; o "engines" como se les suele decir.

Pilas utilizaba SFML, pyqt y en algún momento soportó pyglet, según el programador seleccione. Era una forma de proveer mayor soporte a distintos equipos y hacer de **pilas** una especie de “capa” que unifica el uso de multimedia para videojuegos, como una plataforma de abstracción y simplificación.

Lo cierto es que luego de varias versiones comenzó a notarse el costo de mantener varios motores... y después de todo, fuimos notando que pyqt podía resolver muy bien todas las necesidades que teníamos en mente. No tenía mucho sentido invertir tiempo en mantener otros motores...

Sin embargo, como nos focalizamos en pyqt y nunca decidimos abandonar el resto de los motores oficialmente, la arquitectura de pilas quedó con mucho código pensado para soportar otros motores. Llegamos al punto en donde el diseño es algo más complejo de lo que necesitamos, así que me pareció buena idea aprovechar la posibilidad para simplificarlo.

Al simplificarlo, ahora pilas ya no tiene un atributo "motor", el código de manejo de imágenes, sonidos y eventos quedó mucho más simple, todo usando pyqt y pygame solamente para audios (solo porque phonon, el plugin para gestionar sonidos en qt, no funciona en varios casos).

Este es un ejemplo de esa inicialización en la nueva clase Pilas.Observa que ahora solo tenemos un punto de selección para el motor, puede tener aceleración gráfica o no:

![](/images/2015/01/image00.png)

Esto es algo bastante contundente si tenías en mente el modo de funcionamiento de pilas hace unos años, ahora es mucho mas simple y hasta dan ganas de añadirle cosas :)


## Notificaciones

Ahora el motor utiliza archivos de **log** como las aplicaciones web tradicionales, podrías ver el funcionamiento completo del motor mirando el archivo de log que produce pilas y emitiendo tus propios mensajes.

Para inicializar el reporte de errores tenemos que inicializar pilas con el flag “habilitar_mensajes_log”:

	import pilasengine

	pilas = pilasengine.iniciar(habilitar_mensajes_log=True)

Y por un terminal tendríamos que ver cada uno de los mensajes que nos permiter ver "qué" está haciendo pilas en cada momento.

Este *flag* también se puede cambiar en cualquier momento, llamando a:

	pilas.habilitar_mensajes_log(False)

o bien:

	pilas.habilitar_mensajes_log(False)

Pienso que esta funcionalidad puede ser útil para conocer “qué” hace pilas internamente en cada momento, e incluso nos permitiría a futuro hacer distintos tipos de log. Ahora solo existe este tipo de “log” en consola, pero podríamos hacer uno que guarde un archivo en disco, o que imprima en una ventana de pyqt, algo similar a lo que hace el navegador web cuando encuentra errores:

![](/images/2015/01/image08.png)

## Manejo de errores

Otro punto a mejorar en las versiones anteriores de *pilas* era el manejo de errores. Porque inicialmente nunca habíamos pensando exactamente el flujo de errores y notificaciones para el programador. Cuando pilas fallaba, la aplicación entera podía quedar "congelada" o cerrarse de forma abrupta... 

Ahora, cada vez que hay un error, **pilas** detiene su bucle principal y pone un cartel con el motivo del error.

![](/images/2015/01/image10.png)

Esto ayuda a eliminar por completo los efectos colaterales que teníamos con respecto a los errores dentro del bucle de pilas, esos errores que ocurrían y se imprimían una y otra vez en la consola o volvían inestable todo el proceso.

Al mismo tiempo hace completamente compatible la experiencia de tener un error en distintos sistemas operativos. Hasta ahora, cuando teníamos un error, había que mirar la consola si estábamos en GNU/Linux, ver el diálogo modal en Windows o atender los mensajes de sistema si estábamos en OSX …


![](/images/2015/01/image02.png)

Este nuevo sistema de notificación de errores está implementado como una escena nueva, que se puede encontrar en el archivo ``pilasengine/escenas/error.py``. Básicamente es una escena con el fondo Plano y dos actores de texto que muestran la excepción. Tal vez en el futuro pongamos algo mas de divertido para anunciar el error: http://www.intertech.com/Blog/funny-computer-error-messages/ (en busca de inspiración…)

## Livereload y prototipado

Con estos cambios es más sencillo y limpio reiniciar **pilas**, así que podemos implementar livereload y acelerar el prototipado de juegos. Por ejemplo, en el siguiente video estoy editando un script sencillo, cada vez que guardo el archivo pilas lo reconoce y lo vuelve a ejecutar completo:

<iframe width="960" height="720" src="//www.youtube.com/embed/BrLq25JsYk8?rel=0" frameborder="0" allowfullscreen></iframe>


## Inicializadores de actores y escenas

Algo característico de pilas, es que construir actores y escenas es muy simple, podemos escribir:

	pilas.actores.Aceituna()

y el actor aparece inmediatamente en pantalla. En muchas otras bibliotecas de juegos necesitamos guardar una referencia al objeto y luego “agregarlo” a una lista de sprites a dibujar o árbol de nodos.

Para hacer que esta característica se conserve, necesitamos poder vincular el actor creado con el objeto pilas automáticamente. La forma que descubrí para hacer esto me parece bastante útil, aunque es un poco rara…

Cuando el programador escribe “pilas.actores.Aceituna()” en lugar de estar invocando directamente a la clase Actor, ahora “Actor()” podría ser un método:

![](/images/2015/01/image06.png)

De esta forma, al crear un actor podemos invocar a su constructor internamente y producir la vinculación.

Otra cosa útil de este enfoque, es que podemos simplificar la creación de nuevos actores. No va a ser necesario re-definir los constructores. Podemos decirle a cualquier chico “para implementar un actor, construí una clase con estos dos métodos”, no hace falta _ _init_ _ :

	from pilasengine import Actor

	class NuevActor(Actor):

		def iniciar(self):
			[…]

		def actualizar(self):
			[…]

Esta idea también podríamos llevarla a pilasweb, para que crear actores no necesite anteponer “new” y las sintaxis sean lo más parecidas posibles.


## Testing

Aprovechando la refactorización, comencé a pulir algunos tests y terminé haciendo una batería de tests más robusta y completa.

Ejecutando “make” podemos ver el comando disponible para ejecutar los test y otras cosas:

![](/images/2015/01/image05.png)

Ahora cuando cambiamos el código de pilas, tenemos la posibilidad de corroborar que la mayor parte de la biblioteca continúa funcionando correctamente.

Mi intensión es hacer que estos tests funcionen bien sobre “travis-ci.org”, así podemos tener tests automáticos cada vez que hacemos “push” sobre github, de la misma forma que ocurre con pilasweb.

Este es un ejemplo de travis ejecutando tests de un cambio que introdujo irving:


![](/images/2015/01/image03.png)

## Otras ideas para pensar…

¿Podremos implementar estas mejoras y hacerlas retro-compatibles?, ¿qué otras cosas podríamos mejorar?, ¿Nos ayudaría a unificar la interfaz entre pilas y pilas-web?.


## Referencias

Mientras escribía este documento, hice algunas pruebas y bocetos sobre el siguiente repositorio, si todo sale bien, se volverá el código principal de la próxima versión de pilas-engine:

https://github.com/hugoruscitti/python-pilas-experimental

Puede ser útil para consultar dudas o ver el progreso de estas ideas. Hay varias cosas implementadas, pero va avanzando...

PD: Ningún método, módulo o actor de pilas fue dañado mientras se escribió este documento.

---
layout: post
title: Escalando imágenes con node-webkit
image: ''
date: '2015-01-06 18:37:43'

description: "En este artículo quiero mostrar cómo se pueden procesar imágenes de manera rápida y multiplataforma desde node-webkit..."
cover: '/images/2015/01/portada-escalar.jpg'
tags:
- web
---

En este artículo quiero mostrar cómo se pueden procesar imágenes de manera
rápida y multiplataforma desde
[node-webkit](https://github.com/rogerwang/node-webkit), usando
[ImageMagick](http://www.imagemagick.org/) y [emberjs](http://emberjs.com/).

*ImageMagick* es un conjunto de herramientas para procesar imágenes: escalar,
recortar, convertir y aplicar efectos principalmente.



# Un pequeño ejemplo

Para mostrar cómo combinar estas dos tecnologías, armé un proyecto mas pequeño a
modo de ejemplo. Está disponible en el repositorio
[hugoruscitti/image-resizer-node-webkit](https://github.com/hugoruscitti/image-resizer-node-webkit)
de mi cuenta en github.

La aplicación simplemente convierte la imagen que enviemos a 2 tamaños
diferentes, y lo informa en pantalla. No importa cuan grande sea la imagen, el
trabajo pesado lo hará imagemagick :)

![](/images/2015/01/animacion.gif)


# Paso a paso

Veamos paso a paso la realización de este prototipo usando ember, node-webkit y la integración de ImageMagick.

## Estructura inicial

Para armar el ejemplo comencé con la [estructura inicial del proyecto](https://github.com/hugoruscitti/node-webkit-ember-seed) que te había comentado en el [post anterior](http://examplelab.com.ar/usando-ember-cli-con-node-webkit/).

Luego integré [bootstrap](http://getbootstrap.com/) y un tema de [bootswatch](http://bootswatch.com/) con los comandos:

```
npm install --save-dev ember-cli-bootswatch
ember generate ember-cli-bootswatch
```

y agregando el nombre del tema [lumen](http://bootswatch.com/lumen/) en el archivo ``app.js``:

```js
[...]
var app = new EmberApp({
  'ember-cli-bootswatch': 'lumen'
});
[...]
```

Con esto, la aplicación ya tiene esta apariencia:

![](/images/2015/01/node-webkit-ember-seed-2015-01-03-00-18-14.png)

## Creando la interfaz

Para indicarle a la aplicación la imagen que tiene que procesar hay muchas opciones, pero me pareció que la mas sencilla es tener una zona dentro de la aplicación para soltar el archivo y listo, algo así como hace [Miro Video Converter](http://www.mirovideoconverter.com/):

![](/images/2015/01/Miro-Video-Converter-2015-01-03-00-30-24.png)

Pero algo mas básico, porque en este caso alcanza con tener la zona para soltar archivos y un pequeño espacio para mostrar mensajes:

![](/images/2015/01/image-resizer-node-webkit-2015-01-03-17-41-00.png)

Hacer la interfaz usando las herramientas que brinda *emberjs* es bastante práctico, primero armé dos componentes. Uno para representar la zona donde se pueden soltar archivos y otra para los mensajes.

Estos son los comandos que hacen el código inicial de los componentes:

```
ember generate component iresize-dropzone
ember generate component iresize-messages
```

![](/images/2015/01/image-resizer-node-webkit-2015-01-03-00-40-48.png)

Luego, para componer la interfaz armé la ruta ``index`` con:

```
ember g route index
```

y luego edité el archivo ``app/templates/index.hbs`` para mostrar estos dos componentes nuevos:

```html
{{iresize-dropzone}}
<hr/>
{{iresize-messages}}
```


## Incorporando archivos

Para poder colocar archivos en la aplicación hay que escribir un poco de código para atender los eventos de arrastrar y soltar archivos sobre la ventana.

En el wiki de node-webkit hay un ejemplo que [tomé de referencia](https://github.com/rogerwang/node-webkit/wiki/Dragging-files-into-page). Hace exactamente lo que quiero, y con un ejemplo. Lo único diferente, es que en este caso lo necesito encapsular dentro del componente :

<script src="http://gist-it.sudarmuthu.com/github/hugoruscitti/image-resizer-node-webkit/blob/master/app/components/iresize-dropzone.js"></script>

Con esto ya tenemos div especial, que se pinta de color cuando estamos por soltar archivos y atiende el evento `drop`:

![](/images/2015/01/arrastrar.gif)


## Incorporando ImageMagick

Para incorporar ImageMagick lo mas sencillo es instalar un paquete de node llamado [imagemagick](https://github.com/yourdeveloper/node-imagemagick):

```
npm install imagemagick --save-dev
```

Este módulo simplemente ofrece una interfaz para acceder a los comandos de ImageMagick, pero no incluye ningún binario o biblioteca para compilar, es simplemente un *wrapper*.

Por ejemplo, en mi equipo tengo instalado ImageMagick, y estos son los dos binarios que puedo usar desde la biblioteca:

```
➤ which identify
/usr/local/bin//identify
```

```
➤ which convert
/usr/local/bin//convert
```

Así que para convertir o identificar un archivo primero tengo que requerir el módulo, configurar las rutas y luego utilizarlo. Acá hay un ejemplo de invocación:

![](/images/2015/01/index-html-2015-01-03-03-10-36.png)


## Incorporando binarios

Ahora bien, que nuestra aplicación dependa de tener instalado ImageMagick en el equipo no es lo que buscamos, esto podría ser válido en un sistema con dependencias de software como *GNU/Linux*, pero en windows (por ejemplo) no es nada común... el usuario espera que la aplicación funcione sin instalar nada adicional.

Así que vamos a incorporar imageMagick "dentro" de nuestra aplicación:

Lo primero es descargar los binarios de ImageMagick tanto para windows como para OSX. En mi caso descargué ambos en sus versiones de 32 bits y los [subí a dropbox](https://www.dropbox.com/sh/hy5mg0ouvbx126u/AABJoKLgswbrBOc9aqxtYCsFa?dl=0) eliminando algunos archivos opcionales para hacerlo mas liviano.

Luego los incorporé al directorio ``public``, que usa ember para colocar cualquier archivo estático. Algo así:

![](/images/2015/01/public-2015-01-03-13-01-31.png)

y luego podemos reproducir la misma prueba de antes, pero ahora usando los binarios internos:

![](/images/2015/01/index-html-2015-01-03-13-12-50.png)

## Encapsulando ImageMagick

Para que el código de nuestra aplicación quede sencillo y fácil de comprender, podemos hacer un módulo y colocar ahí todo el código relacionado con ImageMagick:

```
ember generate util resizer
```

![](/images/2015/01/image-resizer-node-webkit-2015-01-03-13-37-44.png)

El código del módulo es un poco largo, pero simplemente obtiene la ruta a los binarios (dependiendo de la plataforma) y luego retorna el resultado en forma de promesa:

https://github.com/hugoruscitti/image-resizer-node-webkit/blob/master/app/utils/resizer.js

de esta forma, desde el controlador podemos convertir imágenes invocando al módulo ``resizer`` así:

```js
import resizer from 'image-resizer-node-webkit/utils/resizer';

resizer().resize(input_path, output_path, 200, 200).
        then(function(data) {
          self.get('messages').pushObject("Creando " + data.output);
        }).
        catch(function(reason) {
        	alert(reason);
        });
```


## Conclusiones

ImageMagick y node-webkit tienen un montón de cosas para seguir investigando, con este simple ejemplo pude resolver un problema particular, pero seguramente hay muchas otras aplicaciones que necesiten algo similar.

Si te resulta útil lo que viste acá, ¡comentalo!.

Te dejo un link al repositorio en donde está todo el código de [este mini-ejemplo](https://github.com/hugoruscitti/image-resizer-node-webkit), los [binarios de ImageMagick](https://www.dropbox.com/sh/hy5mg0ouvbx126u/AABJoKLgswbrBOc9aqxtYCsFa?dl=0) alivianados listos para utilizar y [los binarios de la aplicación generada](https://www.dropbox.com/sh/2iivinhqt9h4r5i/AACCKszLJ6S-8ZlJr2mboUBla?dl=0).

¡Saludos!

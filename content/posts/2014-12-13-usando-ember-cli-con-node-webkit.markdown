---
layout: post
title: Usando ember-cli con node-webkit
date: '2014-12-13 08:38:28'

description: "En este artículo vemos cómo integrar una aplicación emberjs dentro de node-webkit..."
cover: '/images/2014/12/portada.jpg'
tags:
- web
---

Hace unas semanas estoy muy entusiasmado con [emberjs](http://emberjs.com/) y la posibilidad de incorporarlo en las aplicaciones desktop que desarrollamos en  [huayra](http://huayra.conectarigualdad.gob.ar) y [conectar igualdad](http://www.conectarigualdad.gob.ar/).

![](/images/2014/12/0cf15665a9146ba852bf042b0652780a.png)

[emberjs](http://emberjs.com/) es un framework javascript para construir aplicaciones web, en cierta manera es similar a [angularjs](https://angularjs.org/), pero con un [enfoque diferente](http://eviltrout.com/2013/06/15/ember-vs-angular.html) y algunas herramientas fantásticas como [ember-cli](http://www.ember-cli.com/).

Mi sorpresa principal fue encontrarme que [ember-cli](http://www.ember-cli.com/), no funcionaba junto a node-webkit inmediatamente. Me llevó varias horas comprender el motivo y poder resolverlo, así que en este post voy a resumir lo que aprendí y lo quiero compartir con ustedes.

**NOTA**: Si queres tomar un atajo, todo los pasos que realizo acá están en un repositorio que armé para iniciar proyectos llamado [node-webkit-ember-seed](https://github.com/hugoruscitti/node-webkit-ember-seed).



## Instalando ember-cli

Para desarrollar aplicaciones con ember es aconsejable usar una herramienta llamada [ember-cli]((http://www.ember-cli.com/)), ya que nos permite crear fácilmente la estructura de la aplicación inicial, ejecutar tests y construir componentes fácilmente.

Para instalarlo hay que ejecutar el siguiente comando:

```
npm install -g ember-cli
```

o bien:

```
sudo npm install -g ember-cli
```

Si no tenés npm, tendrías [que instalar nodejs](http://examplelab.com.ar/como-instalar-nodejs-en-huayra-linux/) antes (npm es el gestor de paquetes que incluye nodejs).


## Creando un proyecto de ejemplo

Para listar los pasos y mostrar como integrarlo a node-webkit, tomemos un directorio de ejemplo y vamos a construir una aplicación dentro.

Estos son los comandos para iniciar el proyecto:

	mkdir ejemplo
	cd ejemplo
	ember init ejemplo

Con esos comandos, ember va a comenzar a instalar todas
las dependencias:

![](/images/2014/12/dependencias.png)


En este punto, podríamos probar la aplicación creada directamente
desde el navegador usando el comando ``serve``:

	ember serve

![](/images/2014/12/serve.png)

Y cualquier cambio que hagamos se va a ver directamente en el navegador, sin necesidad de reiniciar el servidor o actualizar el navegador :)


## Integrando a node-webkit

Para crear la aplicación node-webkit, necesitamos construir el archivo ``package.json`` con la definición del proyecto y compilar la aplicación.

El archivo que tenemos que crear tiene que llamarse [``public/package.json``](https://github.com/hugoruscitti/node-webkit-ember-seed/blob/master/public/package.json) y
puede tener este contenido:

    {
      "main": "app://localhost/index.html",
      "name": "ejemplo",
      "version": "0.0.1",
      "window": {
        "title": "Ejemplo",
        "width": 800,
        "height": 500,
        "toolbar": true,
        "position": "center"
      }
    }

Luego tenemos que asegurarnos de colocar las rutas como ``node-webkit`` las espera en el archivo ``config/environment.js``:

![](/images/2014/12/config.png)

Posiblemente ni siquera tengas que cambiarlas, al menos en la versión que utilizo aquí de `ember-cli` no hizo falta.

Por último, tenemos que generar el proyecto con ``ember build`` y probar la aplicación
con ``open -a nodewebkit dist`` (en mac) o ``nw dist`` (en huayra/linux):

![](/images/2014/12/prueba-nw.png)


## El bug...

Nos faltaría un solo paso, aún, porque si pulsamos el botón para abrir las herramientas de desarrollo de nodewebkit vamos a ver un error así:

![](/images/2014/12/error.png)

El problema se origina porque ``ember-cli`` re-define la función ``require`` que espera usar node-webkit, así que podemos hacer
algunos cambios en el archivo ``app/index.html`` para resolverlo.

Lo ideal es que tanto ``ember-cli`` y ``node-webkit`` puedan acceder a su propia función ``require``, así que redefiní la función de modo tal que responda tal y como espera cada uno:


![](/images/2014/12/patch.png)

Este es el contenido ``app/index.html``:

```html

<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Ejemplo</title>
    <meta name="description" content="">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <script>
      var is_nodewebkit = (typeof process == "object");

      if (is_nodewebkit) {
        window.node_require = window.require;
      }
    </script>

    {{content-for 'head'}}

    <link rel="stylesheet" href="assets/vendor.css">
    <link rel="stylesheet" href="assets/pilas-engine-bloques.css">
  </head>
  <body>
    {{content-for 'body'}}

    <script src="assets/vendor.js"></script>
    <script src="assets/pilas-engine-bloques.js"></script>

    <script>
      var is_nodewebkit = (typeof process == "object");

      if (is_nodewebkit) {
        window.ember_require = window.require;

        window.require = function(module) {
          try {
            return window.ember_require(module);
          } catch (e) {
            return window.node_require(module);
          }
        }
      }
    </script>

  </body>
</html>
```



## Activando live reload con node-wekbit

Por último, hay una forma de actividad el modo ``live-reload`` en ``node-webkit``, la idea es agregar una sentencia dentro
del archivo ``app/index.html`` para actualizar node-webkit así:

```
<script src='livereload.js'></script>
```

y luego crear el archivo ``public/livereload.js`` con este contenido:


```js
var fs = require('fs');

fs.watchFile('index.html', function() {
  require('nw.gui').Window.get().reloadIgnoringCache();
});
```

De esa forma, cada vez que cambiemos un archivo desde el editor, [ember-cli]() va a detectar los cambios, se va a iniciar la re-compilación, nuestro script encontrará que se actualizó algo y lanzará la actualización de toda la aplicación:


<iframe width="1280" height="720" src="//www.youtube.com/embed/BFDwHhcKOjs?rel=0" frameborder="0" allowfullscreen></iframe>


En fin, nada mal, se vuelve bastante productivo prototipar aplicaciones así, veremos que tal va para las nuevas aplicaciones que tenemos en mente en [huayra](http://huayra.conectarigualdad.gob.ar) y [conectar-igualdad](http://www.conectarigualdad.gob.ar/).

¡Saludos!

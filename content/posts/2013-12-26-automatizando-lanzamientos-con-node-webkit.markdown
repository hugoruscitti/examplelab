---
layout: post
title: Automatizando lanzamientos en node-webkit
date: '2013-12-26 01:15:39'
description: Cómo automatizar empaquetado de aplicaciones con grunt-node-webkit-builder
cover: /images/2013/Dec/portada-empaquetado.jpg
tags:
- linux
---

Existe una tarea para **grunt** que nos permite  automatizar el empaquetado de
nuestras aplicaciones para cada plataforma:
[grunt-node-webkit-builder](https://npmjs.org/package/grunt-node-webkit-builder).

Esto es super útil, imaginá que podés tener tu aplicación lista para distribuir
en linux, windows y mac en unos minutos...


## Instalación

El primer paso es instalarnos la tarea para grunt:

    npm install grunt-node-webkit-builder --save

Luego tenemos que agregar algunas reglas a nuestro archivo **GruntFile.js**.

Por ejemplo, mi archivo **GruntFile.js** a la hora de comenzar un proyecto nuevo se ve así:


```prettyprint javascript
module.exports = function (grunt) {
    grunt.initConfig({
      nodewebkit: {
                    options: {
                              build_dir: './webkitbuilds',
                              mac: true,
                              win: true,
                              linux32: true,
                              linux64: true
                  },
                  src: [
                    './app/**/*',
                    './node_modules/**/*',
                  ]
              },
      });

      grunt.loadNpmTasks('grunt-node-webkit-builder');
  }
```

Luego, para empaquetar la aplicación en todos los sistemas que definimos anteriormente tenemos que ejecutar el siguiente comando:

	grunt nodewebkit

La tarea ``nodewebkit`` se encarga de bajar las versiones compiladas de nodewebkit justo para empaquetar. Esto demora un buen rato la primera vez, porque tiene que descargar unos ``300 MB``.

![](/images/2013/Dec/build.png)


Por último, el resultado del empaquetado va a estar dentro del directorio "releases". Listo para distribuir:

![](/images/2013/Dec/resultado.png)

Y listo, ahora cada vez que quieras hacer un release, lo único que hay que ejecutar es el comando ``grunt nodewebkit``.

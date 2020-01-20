---
layout: post
title: Creando un visor de videos offline con electron y ember
date: "2016-06-02 19:17:18"
description: "Esta semana me propuse hacer una aplicación muy sencilla con ember y electron, un visor de videos offline HTML5..."
cover: "/images/2016/06/preview.png"
---

## Introducción

Esta semana me propuse hacer una aplicación muy sencilla con ember y electron, un visor de videos offline HTML5:

![preview](/images/2016/06/preview.png)

La aplicación en sí es muy simple, está pensanda para crear una biblioteca de videos para mirar con los más chiquitos de la familia sin necesidad de Internet, youtube o publicidades.

![visor](/images/2016/06/visor-1.png)

Técnicamente hablando, la aplicación simplemente busca videos en un directorio del equipo, los lista en pantalla y permite visualizarlos usando HTML5.

## Creando la aplicación

El primer paso fue crear la aplicación ember e instalar algunas pocas extensiones:

```
ember new visor-offline
cd visor-offline

ember install ember-electron
ember install ember-bootstrap
```

Luego, para tener todo el código respaldado en un repositorio utilicé github:

- https://github.com/hugoruscitti/visor-offline

## Previsualizando la aplicación

Lo interesante de ember-electron es que te permite simplificar un montón de pasos, por ejemplo, para ejecutar la aplicación podemos escribir:

```
ember electron
```

y lo que veremos en pantalla es la aplicación corriendo dentro del entorno de electron:

![primer-version](/images/2016/06/primer-version.png)

y al igual que sucede cuando ejecutamos `ember serve`, cualquier cambio que hagamos en el código nos va a mostrar los cambios inmediatamente.

## Cargando datos

Mi intensión es tener una aplicación sencilla y segura. Sin muchas opciones o modos de uso: El visor-offline inicia, busca videos mp4 en el directorio de la aplicación y permite visualizarlos.

Nada más.

Entonces, para descargar videos necesitaba de otra aplicación. Así que elegí usar ClipGrab, una aplicación muy sencilla que permite descargar videos desde youtube en distintos formatos:

![descargas](/images/2016/06/descargas.png)

Ahora, para generar las miniaturas usé un pequeño script, que internamente invoca al comando `ffmpegthumbnailer`:

```
# Archivo: crear_miniaturas.py
import os

for x in os.listdir('.'):
  if x.lower().endswith('.mp4'):
    print("Creando miniatura para: " + x)
    video_input = x
    file_output = "thumbs/" + video_input.replace(".mp4", ".jpg")
    os.system("ffmpegthumbnailer -i '%s' -o '%s' -s400" %(video_input, file_output))
```

## Cargando el listado de videos

Mi intensión es que la aplicación tenga una lógica muy sencilla, sin bases de datos o sincronización, simplemente un visor de videos ya descargados previamente.

Así que adopté la siguiente convención: los videos se deberían grabar directamente en el directorio `c:\videos` y las miniaturas generadas en `c:\videos\thumbs`, así el visor de video solo tendría que ir a buscarlos en esos directorios.

En el caso de osx y linux el procedimiento es muy similar, solamente que buscará videos en `$HOME/videos` y las miniaturas en `$HOME/videos/thumbs`.

```javascript
// archivo: app/routes/index.js

import Ember from "ember";

export default Ember.Route.extend({
  videos: Ember.inject.service(),

  model() {
    return this.get("videos").getVideos();
  }
});
```

Y como el hook "model" está preparado para manejar promesas, implementé la función `getVideos` para que retorne una promesa:

```javascript
// archivo: app/services/video.js

[...]

getVideos() {
    return new Ember.RSVP.Promise((resolve) => {
      let videoPath = this._get_video_path();


      fs.readdir(videoPath, (error, data) => {

        let items = data.map((file) => {
          let title = file.replace(".mp4", "");

          return {
            id: title,
            title: title,
            img: videoPath + "/thumbs/" + title + ".jpg",
            video: videoPath + "/" + file
          };
        });

        resolve(items);

      });

    });
  }
},

[...]
```

El siguiente paso es recorrer la lista de videos desde el template:

```
{{#each model as |video|}}
  {{v-videoThumb video=video}}
{{else}}

  <div class="mensaje-error">
    <p>Lo siento, no hay videos para mostrar.</p>

    <p>Por favor descarga los videos que quieras visualizar
      en <code>c:\videos</code> (o en <code>$HOME/videos</code> en linux y osx).
    </p>
  </div>

{{/if}}
```

Y luego de algunos retoques de estilo quedo así:

![preview2](/images/2016/06/preview2.png)

### Automatizando la generación de binarios

En este punto, si quisiéramos crear los binarios desde nuestra propia computadora tendríamos que ejecutar el siguiente comando:

```
ember electron:package --platform=win32 --ignore "node_modules/\.bin"
```

Sin embargo, algo más interesante es automatizar este procedimiento, hacer que los binarios se generen en un servidor remoto y se suban a github.

Para eso configuré el servicio [travis-ci](travis-ci.org) que va a ejecutar los tests, generar los binarios y los sube a github. Todo de manera automatizada, sin ocupar recursos en mi computadora y super rápido:

![](/images/2016/06/travis.png)

![release](/images/2016/06/release.png)

Por cierto, si querés probar la aplicación compilada podés descargarla desde acá:

- https://github.com/hugoruscitti/visor-offline/releases

### Conclusiones

Ember y electron hacen una muy buena combinación, es super productivo dedicarle algunas horas a un proyecto sencillo como este, y los resultados son muy buenos. Al menos mis sobrinos nos se han quejado aún :P

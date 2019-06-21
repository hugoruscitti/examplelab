---
layout: post
title: Agregando efectos especiales en juegos 2D
image: "/images/2016/02/fuego.jpg"
date: '2016-04-15 21:02:50'
---

Esta semana estuvimos agregando efectos especiales a uno de nuestros juegos en unity:

![](/images/2016/02/Untitled-2016-02-19-15-45-33.png)


Pero a diferencia de lo que hicimos en otros juegos, aquí no usamos partículas sino efectos prediseñados de video, que luego de procesarlos como imágenes se pueden integrar a unity.


## ¿Por qué?

Los efectos de videos tienen una apariencia espectacular, sobretodo cuando de trata de juegos 2d, caricaturescos y divertidos.

Por ejemplo, mirá la galería de efectos que produjo [dyomin](http://videohive.net/user/dyomin) en videhive, como la la serie [toonstool-fx](http://videohive.net/item/toonstool-fx-kit/12815828).


¿No son espectaculares?

![](/images/2016/02/x10_Smoke_Explosions.png)


Ahora bien, ¿cómo los podemos incorporar a un videojuego?

## Integrar a Unity


Para integrar los efectos en unity primero tuvimos que convertir el video de efectos a una serie de imágenes y luego crear la entidad dentro de unity.


### Convertir el video a imágenes

Buscamos varias herramientas, pero la que resultó mejor fué [ffmpeg](https://www.ffmpeg.org/), un conversor de videos multiplataforma de consola completamente libre.

Para instalarlo en osx se puede usar este comando:

```
brew install ffmpeg
```

Una vez instalado, hay que abrir un terminal e invocar a ffmpeg con la ruta del video y el directorio a donde vamos a guardar las imágenes:

```
mkdir output
ffmpeg -i video_fx_1.mov -f image2 output/%05d.png -frames:v 1
```

Así queda el directorio ``output``:

![](/images/2016/02/output-2016-02-19-17-46-57.png)


### Crear la entidad en unity


Lo primero que hicimos es importar todas las imágenes dentro del directorio asserts del proyecto en unity:

![](/images/2016/02/Untitled-2016-02-19-14-58-26.png)

Después, para crear la entidad, seleccionamos todos cuadros de animación y los arrastramos sobre la escena.

En este punto, unity va a realizar varias cosas: va a crear la entidad, la va instanciar en la escena y también creará una animación inicial.

Así, el siguiente paso es posicionar la entidad y ya tenemos algo animado en pantalla:

![](/images/2016/02/2016-02-19-15_23_45.gif)


Por último, para que animación se muestre una sola vez, tuvimos que crear un script llamado ``destroy`` con una función que nos permita representar la eliminación de la entidad:

![](/images/2016/02/Untitled-2016-02-19-15-18-06.png)

El script es super sencillo, alcanza con que tenga una sola función:

```
using UnityEngine;
using System.Collections;

public class destroy : MonoBehaviour {

    void DestroyGameObject() {
        Destroy(gameObject);
    }

}
```

Y para finaizar, tenemos que pulsar el botón detecho sobre el timeline:

![](/images/2016/02/Untitled-2016-02-19-15-16-47.png)

y vincular el nombre de la función ``DestroyGameObject`` para que se invoque en ese instante de la animación:


![](/images/2016/02/Untitled-2016-02-19-15-20-36-1.png)


¡Es todo!
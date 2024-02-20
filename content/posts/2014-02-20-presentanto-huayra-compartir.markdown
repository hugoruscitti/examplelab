---
layout: post
title: Presentando huayra-compartir
date: '2014-02-20 13:14:26'
description: Esta semana quiero presentarles un software que estamos escribiendo en conectar igualdad...
cover: /images/2014/Feb/portada-huayra-compartir.jpg
tags:
- linux
---

Esta semana quiero presentarles un software que estamos escribiendo en conectar igualdad. Es una aplicación que vamos a incluir en el sistema operativo **huayra GNU/Linux 2.0**:


![](/images/2014/Feb/parallaxvieww.png)



**huayra-compartir** es una herramienta que permite intercambiar archivos de manera muy sencilla; la aplicación puede descubrir a todos los equipos en la red automáticamente, ofrece una interfaz de usuario muy simple y no necesita acceso a Internet para funcionar:

![](/images/2014/Feb/huayra_2_generador_de_paquetes__beta___Running__2014_02_01_19_49_36.png)

El software surgió de una idea que teníamos en el equipo hace tiempo; por suerte los primeros prototipos salieron tan bien que arrancamos con todo!

### Secciones

La aplicación tiene tres funcionalidades importantes: te permite ver a los equipos conectados en la red, navegar por los archivos compartidos e iniciar descargas.

La sección **amigos** te permite ver a todos los equipos en la red que utilizan **huayra-compartir**.

Por ejemplo, en esta captura, Ignacio estába compartiendo archivos en dos computadoras:

![](/images/2014/Feb/huayra_2_generador_de_paquetes__beta___Running__2014_02_01_19_55_13-1.png)

Luego hay una vista de archivos. Por ejemplo si existe un equipo en la red bajo el nombre Hugo y hago click sobre él aparece la siguiente pantalla:

![](/images/2014/Feb/huayra_2_generador_de_paquetes__beta___Running__2014_02_01_20_01_09.png)

Cada vez que hacés click sobre un archivo, se inicia una descarga dentro de la sección **descargas**. De forma tal que la interfaz nunca te interrumpe, podés seguir navegando y seleccionando mas cosas para bajar.

Así se ve la sección **descargas**:

![](/images/2014/Feb/huayra_2_generador_de_paquetes__beta___Running__2014_02_01_20_02_32.png)




### Su versión predecesora

Esta aplicación no es algo completamente nuevo. Bah, en realidad es casi todo nuevo, excepto la "idea".

**huayra-compartir** es la secuela de una aplicación llamada **compartir-web** (que se incluía en la primer versión de huayra-linux).

**compartir-web** ofreciá algo muy parecido, te permitía colocar archivos en una carpeta y desde cualquier equipo de la red podía verlos y descargarlos.

Por ejemplo, cuando ingresabas a localhost, o el puerto 80 con la ip del equipo te aparecería en pantalla lo siguiente:

![](/images/2014/Feb/huayra_2_generador_de_paquetes__beta___Running__2014_02_01_20_09_41.png)

Lo diferente en esta nueva versión es que cuenta con una interfaz de usuario propia, donde se descubren los equipos automáticamente. Pero la idea general es muy similar.

Otra diferencia es la plataforma de implementación. Antes se utiliza **lighttpd** para servir los archivos y **chromium** para visualizarlos. Ahora todo está sobre **node-webkit** encapsulando a *express*, *angularjs*, *bootstrap*, y algunas cosas mas !

Pienso que esta nueva versión es algo mas sencilla de utilizar, pero naturalmente reconozco que también es mucho mas compleja... es un balance algo raro, el enfoque que usabamos antes era mucho mas sólido.

## ¿Cómo está implementado?

Para implementar la aplicación usamos varias ideas y tecnologías diferentes.

Intentaré resumirte los conceptos principales de la solución por si lo querés investigar y ayudarnos a mejorarlo ;)


### Node-webkit como plataforma

La aplicación completa está implementada sobre [node-webkit](https://github.com/rogerwang/node-webkit), una plataforma para construir aplicaciones nativas usando HTML5 + nodejs.

Si nunca viste node-webkit, tal vez te resulte útil ver una charla que di hace tiempo llamada: [Haciendo aplicaciones complejas de manera simple (con node-webkit)](http://www.youtube.com/watch?v=TzDhzayO_uk)

### Interfaz con CSS y HTML

La interfaz está construida utilizando HTML, el famoso framework CSS [bootstrap](http://getbootstrap.com/) y un *theme* que había comprado hace unos meses en el sitio [wrapbootstrap](https://wrapbootstrap.com/).

Luego, la estructura de aplicación y todas las interacciones las realizamos mediante [angularjs](http://angularjs.org)

Aquí se ve un ejemplo de intercambio de vistas que utilizamos para el panel principal:

![](/images/2014/Feb/ScreenFlow2.gif)


### El formato de intercambio

Para que los equipos puedan exponer sus archivos compartidos usamos el microframework [express](http://expressjs.com) y un formato de intercambio muy simple: **json**

Si querés visualizar cómo se ve el formato de intercambio, lo mas sencillo es abrir un navegador y apuntar a la url que muestra la consola de **huayra-compartir** cuando se inicia:

![](/images/2014/Feb/Huayra_Compartir_2014_02_13_23_25_49.png)

Así es como se ve el formato de datos desde un navegador tradicional:

![](/images/2014/Feb/192_168_1_101_9110_2014_02_13_23_28_27.png)


A su vez, el atributo "archivos" de la respuesta nos da una URL para acceder a los archivos compartidos:

![](/images/2014/Feb/_2014_02_13_23_31_45.png)

Esta forma de construir las rutas y exponerlas como datos (*à la* [hypermedia](http://en.wikipedia.org/wiki/HATEOAS)) nos ayudó un montón a depurar y visualizar lo que la aplicación efectivamente cuando las cosas no funcionába como esperábamos.

Además, este formato de datos "enlazados" se pueden navegar de manera muy sencilla si instalás en tu navegador la extensión [JSON View](https://chrome.google.com/webstore/detail/chklaanhfefbnpoihckbnefhakgolnmc).

### Descubriendo equipos con "polo"

Para descubrir los equipos comencé investigando  varias bibliotecas en [npmjs.org](http://npmjs.org).

Casi todas las bibliotecas que probé hacían prácticamente lo mismo, ofrecián una capa de abstracción sobre zeroconf/bonjour/mdns.

*mdns* me pareció una de las mas completas y funcionales, pero luego de varias pruebas y experimentos cambié mi elección por una alternativa mas sencilla llamada "polo".

En **Polo**, la idea general es que cada equipo tiene la posiblidad realizar un anuncio de inicialización de servicio (llamado "up") en la red local. Emitir un mensaje de aviso de este tipo sirve para que todos los equipos en la red reciban la noticia y los datos para comenzar a usar ese servicio.

Esto me pareció espectacular, imaginá: podés iniciar un servicio tipo webserver, luego hacer un anuncio en la red y corroborar que todos los equipos subscriptos se enterarán al instante.

![](/images/2014/Feb/2014_02_19_23_08_28.jpg)

Así funciona el corazón de **huayra-compartir**,  cada cliente inicia un webserver (que expone los archivos que comparte el equipo), luego hace un anuncio en la red y por último se pone a escuchar las notificaciones en la red.

Para instalar ``polo`` en nodewebkit usamos ``npm`` así:

     npm install polo --save

Hay unos ejemplos básicos de utilizanción de polo en el [repositorio oficial de npm](https://www.npmjs.org/package/polo), es mucho mas sencillo de usar de lo que parece al principio.


## A futuro ...

Hay varias cosas que nos gustaría implementar en las próximas versiones: estaría buenisimo tener un chat, poder descargar carpetas completas con un solo click, añadir gráficas de la red, etc...

Cuando mostramos el software en la oficina volaron mil ideas, y saltaron algunos bugs también (naturalmente).

Te invito a visitar el repositorio del proyecto, me gustaría que nos cuentes que cosas le agregarías o te gustaría cambiar.

Seguramente vamos a estar implementando mas cosas por ahí pronto:

https://github.com/HuayraLinux/huayra-compartirweb

¡Saludos!

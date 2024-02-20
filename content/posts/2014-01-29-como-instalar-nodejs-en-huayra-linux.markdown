---
layout: post
title: Como instalar nodejs en huayra-linux
date: '2014-01-29 21:04:56'
description: NodeJs es una de las herramientas que estoy utilizando en huayra como plataforma ...
cover:  /images/2014/Jan/portada-nodejs.jpg
tags:
- linux
---

**Importante:** **En huayra 3.0 se incluyó nodejs de forma nativa, así que estas instrucciones no son necesaria, solamente son útiles para versiones anteriores a la huayra 3.0 u otros sistemas que no incluyan nodejs.**



**Nodejs** es una de las herramientas que estoy utilizando en *huayra* como plataforma para las aplicaciones nuevas, como [huayra-compatir](https://github.com/HuayraLinux/huayra-compartirweb), [huayra-motion](https://github.com/HuayraLinux/huayra-stopmotion) y el [visor de manual](https://github.com/HuayraLinux/huayra-visor-manual).

Hoy lamentablemente no tenemos **nodejs** como paquete pre-instalado en la distribución, así que para tenerlo funcionando hay que hacer algunos pasos previos.

Además, como *huayra* está basado en la rama estable de *Debian*, hay varios paquetes como **nodejs** o **npm** que solamente podemos instarlos mediante backports.

### Instalando nodejs

Primero vamos a comenzar abriendo una terminal y editando el archivo ``/etc/apt/sources.list``

![](/images/2014/Jan/huayra_2_generador_de_paquetes__beta___Running__2014_01_29_15_20_16.jpg)


Para editar el archivo podés escribir:

    sudo nano /etc/apt/sources.list

luego agregá esta linea al principio del archivo:

    deb http://ftp.debian.org/debian wheezy-backports main


Después hay que actualizar el listado de software disponible e instalar todo lo necesario:

	sudo apt-get update
    sudo apt-get install nodejs nodejs-legacy curl


Por último, para instalar **npm** hay que ejecutar:

    curl https://www.npmjs.org/install.sh | sudo sh

### Probando que todo funcione bien

¡Listo!, ahora desde una terminal vas a poder usar los comandos **node** o **npm** tranquilamente.

Acá incluyo un pequeño ejemplo sobre cómo obtener las interfaces de red directamente desde el intérprete de **nodejs**:

![](/images/2014/Jan/salida.jpg)

es todo :)

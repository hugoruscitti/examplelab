---
layout: post
title: Cómo crear apuntes de referencia
date: '2021-03-29 00:00:00'
description: |
  Usando vim y un procesador de textos se pueden crear
  apuntes rápidos para tener como referencia la hora
  de programar.
cover: /images/2021/como-crear-apuntes-de-referencia/portada.jpg
---

Algo que me sirve mucho a la hora de programar es ir tomando
notas de aquellos nombres de funciones, módulos o ejemplos que
me resultan útiles. 

A estas notas las suelo compactar y reducir para que me sirvan
de apunte. Solo recolecto aquello que uso con frecuencia.

Después de todo, programar está lleno de símbolos a los que
tenemos que recurrir una y otra vez.

Si no tomo nota de estas cosas, me veo obligado a abrir un
navegador, ingresar a google y realizar búsquedas para encontrar
la respuesta a algo que ya hice con anterioridad.

Por ejemplo, al usar ember hay una serie de cosas a las que
suelo recurrir: de dónde se importan las funciones `tracked`, cómo
inyectar un servicio, cómo se llama a una acción desde una plantilla
etc.. 

Así que mi apunte se ve como este:

![](/images/2021/como-crear-apuntes-de-referencia/apunte1.jpg)

Sí, es un apunte en papel, porque prefiero que esté afuera de
la computadora y me sirva de referencia, algo que puedo poner en
el escritorio, mirar rápido y hacer anotaciones cuando encuentro
algo para añadir o corregir:

![](/images/2021/como-crear-apuntes-de-referencia/apunte2.jpg)


Otra ventaja de hacer los apuntes en papel es que tengo la
limitación física de hacerlos breves, dejando solo la información
indispensable, sin funciones raras ni largas explicaciones.

El apunte es muy personal, lo escribo para mí, evito colocar
cosas que ya sé de memoria y pongo ejemplos sabiendo que me
van a servir.

## Pasos para crear un apunte

Lo primero que hago para crear un apunte como estos es crear un
archivo de textos en vim e ir colocando las porciones de la API que
quiero incluir:

![](/images/2021/como-crear-apuntes-de-referencia/vim.png)

La razón por la que uso vim es porque me gusta imprimir el
apunte a color, con resaltado de sintaxis y formato.

Una vez que tengo una primera versión del apunte, suelo quitar
la numeración de líneas, poner un esquema de colores claro y exportar
todo como HTML así:

```
:set nonumber norelativenumber
:coloscheme xcodelight
:TOhtml
:!open %
```

![](/images/2021/como-crear-apuntes-de-referencia/exportado1.png)

Con el comando `TOhtml` vim genera un *split* con el código HTML
de nuestra nota. Este código html se puede guardar y abrir en
un navegador:

![](/images/2021/como-crear-apuntes-de-referencia/exportado2.png)

En este punto, lo que suelo hacer es copiar y pegar el contenido
del navegador en un procesador de textos, en donde puedo ajustar
la cantidad de columnas, márgenes, tamaño de textos y hasta agregar
imágenes:

![](/images/2021/como-crear-apuntes-de-referencia/final.png)

Obviamente se pueden saltar algunos pasos, pero por el momento
me siento cómodo usando las tres herramientas y asegurándome que
todo quede bien antes de imprimir.


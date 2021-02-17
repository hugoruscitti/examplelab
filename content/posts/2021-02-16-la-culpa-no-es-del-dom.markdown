---
layout: post
title: La culpa no es del DOM
date: '2021-02-16 00:00:00'
description: |
  Seguramente escuchaste a alguien sostener que usar frameworks
  JavaScript hace que las aplicaciones sean más rápidas porque 
  "el DOM es lento". Aquí te voy a contar por qué es una idea equivocada.
cover: /images/2021/la-culpa-no-es-del-dom/portada.jpg
---

Usar un Framework para escribir tu aplicación JavaScript tiene varias
ventajas, sin embargo, creo que hay que revisar una idea que vi en varias charlas
técnicas y algún que otro tutorial cuando se intenta justificar el
uso de un Framework que me parece incorrecta.

Se suele decir que cambiar [el DOM con las APIs nativas del navegador
es un proceso costoso](https://www.reddit.com/r/javascript/comments/6115ay/why_do_developers_think_the_dom_is_slow/)
(computacionalmente hablando) y que por ese motivo conviene usar virtualDom o una abstracción similar.

Lo cierto es que acceder al DOM no es lento, de hecho, la única forma
de hacer que ocurran cosas en la pantalla del navegador con JavaScript
es alterando el DOM, incluso si usas un Framework. 

Tal vez tu código de aplicación no esté accediendo directamente a los
nodos del DOM, sin embargo el Framework sí lo va a estar haciendo, ¡es la
única forma que existe de alterar la interfaz!

Entonces, ¿de donde proviene esa idea de que el DOM es lento?


# Es fácil escribir código ineficiente

Si escribimos código que accede al DOM directamente, sin saber
exactamente lo que estamos haciendo, podemos llegar a escribir
código ineficiente que va a poner a trabajar al navegador de más.

Tomemos como ejemplo esta situación: tienes una lista de productos en un
array y quieres convertirlo en una tabla para mostrarlos en el DOM del navegador.

Una forma sencilla de pensarlo es así:

> Comienzo capturando un nodo del DOM, en donde quiero colocar el listado, y luego voy
> insertando elementos al DOM a medida que leo el array de productos.

Que en código podría ser algo así:


```javascript
let tbody = document.getElementById("cuerpo");

for (let u of usuarios) {
  let tr = document.createElement("tr");
  let tdNombre = document.createElement("td");
  let tdEmail = document.createElement("td");

  tdNombre.innerText = u.name;
  tdEmail.innerText = u.email;

  tr.appendChild(tdNombre);
  tr.appendChild(tdEmail);

  tbody.appendChild(tr);
}
```

Ahora bien, el código va a funcionar bien, pero ese `tbody.appendChild(tr);` que
aparece al final va a obligar al navegador a trabajar más de lo necesario.

Resulta que cuando añadimos un elemento al DOM el navegador tiene que
recalcular el tamaño del documento, avisar a cualquier observador del cambio
del DOM, procesar nuevamente la disposición de los elementos, tal vez extender
la barra de desplazamiento vertical y algunas cosas más.

El problema aquí no es el DOM en sí, sino que nuestro algoritmo no tiene en
cuenta que el navegador prefiere que hagamos las cosas en lote.

Si queremos mostrar 100 elementos en una lista, ¿por qué no los mostramos todos juntos en lugar
de hacerlo uno a uno?. 

Esta optimización es muy fácil de hacer:

Primero tenemos que crear un
[DocumentFragment](https://developer.mozilla.org/es/docs/Web/API/DocumentFragment),
que es básicamente un nodo que no forma parte del documento:

```javascript
let df = document.createDocumentFragment();
```

Luego podemos añadir ahí todos los elementos de la tabla, uno a uno, en lugar
de añadirlos a la tabla.


```javascript
df.appendChild(tr);
```

Y por último, podemos agregar todos los elementos juntos a la tabla, produciendo
un solo cambio en el dom del documento:

```javascript
tbody.appendChild(df);
```

Tomando el algoritmo original, estos son todos los cambios que tendríamos
que hacer:

{{<figure src="/images/2021/la-culpa-no-es-del-dom/diff.png" caption="La versión anterior y la optimizada">}}


# Conclusión

Si tenemos en cuenta cómo trabaja el navegador hay un montón de oportunidades
para optimizar cosas.

Creo que las críticas que se hacen al DOM, y su rendimiento, muchas veces
están alentadas por desconocer alguno de estos detalles; o por escribir código
a la ligera. Después de todo, es mucho más fácil culpar a la herramienta, ¡todos hacemos eso de vez en cuando!.


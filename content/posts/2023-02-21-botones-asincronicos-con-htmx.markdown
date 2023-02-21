---
layout: post
title: Botones asincrónicos con HTMX
date: '2023-02-21 00:00:00'
description: |
  Cómo mejorar la apariencia de botones que demoran en responder.
cover: /images/2023/botones-asincronicos-con-htmx/portada.jpg
---

HTMX no deja de sorprenderme, me gusta mucho la simplicidad
que te proponer para resolver problemas comunes en todas las
aplicaciones web.

Esta semana, por ejemplo, mejoré la forma en la que funcionan los
formularios para crear transacciones en un software que estoy
escribiendo para manejar gastos personales.

Resulta que tenía un formulario que permitía registrar gastos en
el sistema, pero esa acción demoraba en ejecutarse en el servidor, así
que se me ocurrió agregar un botón asincrónico que se viera
así:

<<TODO: imagen de botón cargando >>

Es decir, yo quería hacer dos cosas:

- Desactivar el botón para prevenir doble clic.
- Mostrar un indicador tipo `spinner` hasta que termine la tarea.


Y aquí es donde encontré la forma que propone HTMX de hacer eso. Una
manera muy simple y sin necesidad de escribir JavaScript:

```html
<button type="submit" data-loading-disable>
  
  <div class="spinner dib f7" data-loading>
    <img src="/static/spinner-animado.svg">
  </div>

  Guardar
</button>
```

HTMX va a leer dos atributos dentro de este HTML, el primer atributo es
"data-loading-disable", que va a desactivar el botón mientras se realiza la
acción asincrónica. El segundo atributo que revisará es "data-loading", que se
va encargar de mostrar ese elemento `ìmg` (con el spinner) solamente cuando se
esté esperando la respuesta del servidor.

![](/images/2023/botones-asincronicos-con-htmx/button.gif)

Aquí hay una página que explica en detalle cómo usar esta extensión
de [htmlx](https://htmx.org/extensions/loading-states/)
 

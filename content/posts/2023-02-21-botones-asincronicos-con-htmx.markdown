---
layout: post
title: Botones asincrónicos con HTMX
date: '2023-02-22 00:00:00'
description: |
  Cómo mejorar la apariencia de botones que demoran en responder.
cover: /images/2023/botones-asincronicos-con-htmx/portada.jpg
tags:
- web
---

HTMX no deja de sorprenderme, me gusta mucho la simplicidad
que te propone para resolver problemas.

Esta semana, por ejemplo, mejoré la forma en la que funcionan los
formularios para crear transacciones en una aplicación web
de gastos personales que estoy escribiendo.

Resulta que tenía un formulario que permitía registrar gastos en
el sistema, pero esa acción demoraba en ejecutarse en el servidor, así
que se me ocurrió agregar esta funcionalidad:

- Desactivar el botón para prevenir doble clic.
- Mostrar un indicador tipo `spinner` hasta que termine la tarea.


Sin HTMX, tendría que escribir algo de JavaScript para
gestionar manualmente la petición al servidor y cambiar algo
de código del lado del servidor para que esto funcione
correctamente.

Pero con HTMX, es mucho más simple, no tengo que escribir
JavaScript, solamente agregar algunos atributos extra al
HTML que ya tengo:

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
va encargar de mostrar ese elemento `img` (con el spinner) solamente cuando se
esté esperando la respuesta del servidor.

![](/images/2023/botones-asincronicos-con-htmx/button.gif)

Es decir, logré implementar exactamente lo que quería, pero
de forma simple.

Por cierto, aquí hay una página que explica en detalle cómo usar esta extensión
de [htmx](https://htmx.org/extensions/loading-states/)
 

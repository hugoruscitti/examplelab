---
layout: post
title: Resaltando bloques en Pilas
date: '2021-02-24 00:00:00'
description: |
  Cuento cómo hice que los bloques de pilas
  se resalten cuando entran en ejecución.
cover: /images/2021/resaltando-bloques-en-pilas/portada.jpg
---

Pilas permite visualizar el código que se está ejecutando en todo momento.

La aplicación pinta con un color diferente las lineas de código que
efectivamente se ejecutaron:

![](/images/2021/resaltando-bloques-en-pilas/resaltado-de-codigo.png)

Este resaltado es útil incluso para los que programamos hace tiempo. Porque
sin esto te ves obligado a llenar el código de `console.log` para asegurarte
de qué está haciendo el programa.

Sin embargo, cuando empecé a jugar con la idea de [añadir bloques a Pilas](/posts/2021-02-19-bloques-y-codigo), noté
que el resaltado de código era algo que faltaba. Sin resaltado me veo obligado a tener
que imaginarme el programa ejecutando en mi cabeza, imaginando qué bloque se está ejecutando.

Claramente necesitaba poder resaltar bloques en pilas.

## El problema

La [biblioteca que estoy utilizando](https://developers.google.com/blockly/) para incorporar bloques tiene
una función dedicada
a resaltar bloques llamada `highlightBlock`:

![](/images/2021/resaltando-bloques-en-pilas/bloque-resaltado.png)

El problema es que el editor de pilas está dividido en varios componentes independientes entre
sí. Por ejemplo el área que visualiza el juego es un componente que a su vez tiene
un `iframe` dentro para independizar el `scope` de ejecución. Y a su vez, el área de bloques
también está en su propio componente con un `iframe`:

![](/images/2021/resaltando-bloques-en-pilas/iframes.png)

Así que para resaltar bloque tuve que seguir varios pasos.

## Instrumentando código

Al igual que como hice con el resaltado de código en el editor de texto, aquí tuve que
insertar automáticamente código de seguimiento para saber qué partes del
código resaltar.

Por suerte [Blockly](https://developers.google.com/blockly/) ya incluye algo para hacer
esto muy fácilmente, solamente hay que escribir algo como esto:

```javascript
Blockly.JavaScript.STATEMENT_PREFIX = `
  this.pilas.notificar_ejecucion_del_bloque(%1, this.id);
`;
```

[Blockly](https://developers.google.com/blockly/) se va a encargar de insertar esta llamada a pilas antes de cada una de las
sentencias, por ejemplo:

![](/images/2021/resaltando-bloques-en-pilas/comparativa.png)

Quienes usen pilas no van a notar que este código se agrega automáticamente, ya que
esta versión modificada el código se genera en memoria y se procesa justo antes de
poner en ejecución el juego.

## Almacenando información de ejecución

> TODO

## Avisando al editor qué se ejecutó

> TODO

## Añadiendo resaltado al modo pausa

> TODO

# Conclusión

> TODO

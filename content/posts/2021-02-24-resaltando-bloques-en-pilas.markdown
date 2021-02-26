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

[Blockly](https://developers.google.com/blockly/) se va a encargar de insertar 
esta llamada a pilas antes de cada una de las sentencias, por ejemplo:

![](/images/2021/resaltando-bloques-en-pilas/comparativa.png)

Quienes usen pilas no van a notar que este código se agrega automáticamente, ya que
esta versión modificada el código se genera en memoria y se procesa justo antes de
poner en ejecución el juego.

## Almacenando información de ejecución

Para saber qué bloques ir resaltando hice que la función `notificar_ejecucion_del_bloque`
simplemente almacene en un diccionario todos los bloques
a resaltar por actor.

![](/images/2021/resaltando-bloques-en-pilas/notificar.png)

Así, el diccionario `instrumentacion_de_bloques` se va llenando con
todos los bloques que se ejecutan en un solo ciclo del pilas.

Por ejemplo, en una escena donde hay dos actores con bloques
el diccionario puede quedar así:

```javascript
{
  1278: [
    "M.ujdyfst~C9SNlx%%~W",
    "n#Df-%|n/TtB*Qc([e(d"
  ],
  1585: [
    "Sux_IEGyGca,_Slu#R?!"
  ]
}
```

Los números `1278` y `1585` son los identificadores de actores, mientras
que las cadenas de texto como `"M.ujdyfst...` son los identificadores
de bloques.

## Resaltando bloques

Ahora, con este diccionario la tarea se volvió mucho más sencilla, porque
pude separar en dos lugares independientes "qué bloques colorear" vs "dónde colorearlos".

Pilas tiene un sistema de eventos similar al que comenté en 
[este otro post](/posts/2021-02-09-sistema-de-eventos-tipados), así que pude enviar
el diccionario a través de un evento que puede capturar el componente de Blockly.

Este es un ejemplo de cómo quedó la integración cuando se usa el modo
pausa:

![](/images/2021/resaltando-bloques-en-pilas/animacion.gif)

# Conclusión

Me quedé muy contento con la forma en la que se colorean los bloques. Pensé que iba
a ser mucho más sencillo de implementar, pero aún así creo que llegué a
una buena forma de resolverlo.

Más adelante voy a poner a prueba el rendimiento a ver si no afecta mucho
la velocidad del motor.


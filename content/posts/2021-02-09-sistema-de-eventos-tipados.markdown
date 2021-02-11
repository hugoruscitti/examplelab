---
layout: post
title: Haciendo un sistema de eventos tipado
date: '2021-02-09 00:00:00'
description: |
  Armé un sistema de eventos dentro de una aplicación
  realizada con TypeScript que previene algunos
  errores comunes gracias al sistema de tipos que trae el
  lenguaje.
cover: /images/2021/sistema-de-eventos-tipados/portada.jpg
---

Cuando empecé a investigar acerca de TypeScript no le vi
mucha utilidad. Declarar tipos de datos para
variables simples como number o string no me parecía nada
valioso.

Sin embargo, cuando se trata de estructuras de datos la cosa
se pone interesante. TypeScript nos permite describir la "forma"
que deberán tener ciertas estructuras de datos y eso hace
que nuestro código gane algo de consistencia adicional.

Después de todo, la pieza más importante de un programa son
sus estructuras de datos y ayuda mucho poder detectar inconsistencias
mientras estamos escribiendo el código.

# Un ejemplo para ilustrar todo esto

Me encontré con la necesidad de tener una forma de comunicar dos partes de una
aplicación; necesitaba tener un sistema de eventos, poder enviar
en mensaje de una sección de la aplicación a otra.

Esto es fácil de hacer dentro de un navegador, podemos crear un evento
personalizado, "conectarnos" a ese evento, y luego lanzarlo desde otra
parte de la aplicación.

Por ejemplo de esta forma:

```javascript
// Para disparar el evento
window.dispatchEvent(new CustomEvent("cambia-balance", { 
  detail: { 
    nuevoBalance: 4000, 
    cuentaID: 14
  }
})); 


// Para conectarnos al evento (desde otro componente)
window.addEventListener("cambia-balance", function(evento) {
  let { cuentaID, nuevoBalance} = evento.detail;
  console.log(`Ha cambiado la cuenta ${cuentaID}, el balance es ${nuevoBalance}`);
});
```

Aquí tenemos que identificar que las dos piezas tienen que tener algunas
cosas en común.

El evento `cambia-balance` se tiene que lanzar especificando el `nuevoBalance` y
la `cuentaID`, porque si se llama olvidando alguno de estos parámetros el sistema
puede llegar a comportarse raro en tiempo de ejecución:

![](/images/2021/sistema-de-eventos-tipados/bug.png)

Es decir, no va a fallar, pero ese `undefined` nos señala que algo no anda bien. ¿Será
que falta un argumento en el evento?, ¿En qué parte del sistema se lanza el evento?, ¿Me
quedó un renombrado de atributos por la mitad?.

A mí me produce mucha incertidumbre hacerme todas esas preguntas. ¡Ni hablar cuando
el código se vuelve complejo!. Ese `undefined` me molesta principalmente porque casi
siempre el motivo del error es muy tonto pero aún así me lleva mucho tiempo encontrarlo.

# Eventos bajo tipos

Otra forma de crear el sistema de eventos es comenzar definiendo
qué estructura deberán tener los eventos:

```typescript
type Eventos = {
  "cambia-balance": { cuentaID: number, nuevoBalance: number},
  // otros eventos
}

type Evento = keyof Eventos;
```

Con esto, TypeScript sabrá que cuando mencionemos el tipo
de dato `Evento`, en realidad nos estamos refiriendo a un `string`
que también tiene que ser una clave del diccionario Eventos.

Ahora, para asegurarnos de que el código que envía eventos
use el sistema de tipos hice esta función:

```typescript
function enviar<T extends keyof Eventos>(nombre: T, datos: Eventos[T]) {
  window.dispatchEvent(new CustomEvent(nombre, { detail: datos }));
}
```

Así, cuando queremos usar esta función para enviar un
evento el propio editor VIM nos ayuda reconociendo qué
datos necesitamos especificar en cada evento:

![](/images/2021/sistema-de-eventos-tipados/autocompletado.png)

Incluso, si cometemos un error, como el que mencioné más arriba, no hace falta
ejecutar el programa para darnos cuenta de que algo anda mal:

![](/images/2021/sistema-de-eventos-tipados/tip.png)

Luego, la función para conectar mensajes podría tener esta forma:

```typescript
function conectar<T extends keyof Eventos>(nombre: T, fn: (datos: Eventos[T], evento: CustomEvent) => void) {
  window.addEventListener(nombre, (e: CustomEvent) => {
    fn.call(this, e.detail, e);
  });
}
```

Esta función se puede mejorar para facilitar la desconexión de eventos, pero
preferí dejarla así solo para ilustrar cómo describir los tipos
de datos.

Y finalmente, así lo interpreta el editor, ayudándonos a detectar
inconsistencias en los eventos que recibimos:

![](/images/2021/sistema-de-eventos-tipados/conectar.png)

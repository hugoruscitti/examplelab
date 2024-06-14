---
layout: post
title: Apunte VanillaJS
date: '2024-06-14 00:00:00'
description: |
  Un artículo con recetas y apuntes para facilitar la creación de proyectos nuevos.
cover: /images/2024/apunte-vanilla-js/portada.jpg
---

Comencé a programar mis experimentos directamente en JavaScript, sin usar
frameworks e intentando lograr una estructura de proyecto simple, fácil de
mantener y transportar.

Así que me pareció útil crear este artículo con recetas y apuntes para facilitar
la creación de proyectos nuevos:

## ¿Cómo empezar?

El punto de entrada para una aplicación simple es un archivo `index.html`
similar a este:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Título</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="css/style.css">
    <script type="module" src="js/app.js"></script>
  </head>
  <body>
  </body>
</html>
```

Ojo, en este script se asume que el archivo `main.js` es un módulo, ver la
siguiente sección para más detalles.

## Módulos y componentes

Para dividir el código en archivos se puede tener un script principal llamado
`main.js` y cargarlo desde la página principal así:

```html
<script type="module" src="js/main.js"></script>
```

Y dentro de `main.js` se pueden cargar los otros archivos así:

```js
import Drop from "./components/drop.js";

customElements.define("x-drop", Drop);
```

Donde el archivo `drop.js` podría ser un *Web Component* como este:

```js
class Drop extends HTMLElement {

    constructor() {
        super();
        this.name = 'World';
    }

    static get observedAttributes() {
        return ['name'];
    }

    connectedCallback() {
        this.textContent = 'Hello World!';
    }

    attributeChangedCallback(property, oldValue, newValue) {
        console.log("attribute changed", {property, oldValue, newValue});
    }

    disconnectedCallback() {
    }

}

export default Drop;
```

Y si el archivo expone varias funciones, se pueden cargar así:

```js
import { log, test } from "./utils.js";
```

Y exponer de esta forma en el archivo `utils.js`:

```js
function log() {
}

function test(a) {
}

export default {log, test};
```


## Compilación para distribuir

Luego si se quiere hacer una unificación de los módulos en un único archivo se
puede ejecutar este comando:

```
npx rollup js/main.js --file bundle.js
```

Ojo, tener en cuenta que los navegadores suelen hacer un `cache` por nombre de
archivo, así que suele ser buena idea cargar el archivo `bundle.js` en el
archivo `html` usando algo como esto:

```html
<script src="bundle.js?version-hash-o-fecha=2"></script>
```

## Eventos

El evento más importante de una aplicación VanillaJs es `DOMContentLoaded`, y se
conecta así:

```html
<html>

<head>
  <script>
    window.addEventListener('DOMContentLoaded',function () {
        // Documento listo para usar.
    });
  </script>
</head>

</html>
```

## Detectar errores en JavaScript

Para generar un reporte de posibles errores se puede ejecutar este comando:

```
find ./js -name "*.js" -exec npx quick-lint-js "{}" \;
```

o una versión mucho más rápida si se instala la herramienta globalmente:

```
npm install -g quick-ling-js
find ./js -name "*.js" -exec quick-lint-js "{}" \;
```

y el resultado en pantalla debería ser como este:

```
./js/main.js:21:1: warning: assignment to undeclared variable [E0059]
./js/main.js:23:13: warning: use of undeclared variable: b [E0057]
./js/components/drop.js:34:5: warning: use of undeclared variable: drop_zone
```

Esta herramienta está buena porque solamente nos alertará los posibles bugs del
programa. No va a generar mensajes por temas de estilo, nombres de métodos ni
otras minucias.


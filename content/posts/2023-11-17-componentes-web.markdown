---
layout: post
title: Componentes web con vanilla JavaScript
date: '2023-11-17 00:00:00'
description: |
  Cómo crear componentes web sin usar frameworks o
  bibliotecas.
cover: /images/2023/componentes-web/portada.jpg
tags:
- web
---

Hoy es mucho más fácil crear componentes web para nuestras
aplicaciones, ya no se necesita una biblioteca para hacer
esto.

¿Cómo se hace?, simplemente tenes que inventarte un nombre
para el componente, por ejemplo **contador-de-clicks** y
comenzar a utilizarlo dentro de tus archivos *html* así:

```html
<contador-de-clicks></contador-de-clicks>
```

Luego, para que este componente tenga comporatamiento es
necesario escribir algo de código JavaScript para
representarlo:

```javascript
class ContadorDeClicks extends HTMLElement {

  constructor() {
    super();
  }
  
  connectedCallback() {
    this.contador = 0;
    this.innerHTML = `<button>Has hecho <span>${this.contador}</span> clicks</button>`;
    
    var boton = this.querySelector("button");
    boton.addEventListener("click", this.onClick.bind(this));
  }
  
  disconnectedCallback() {
    var boton = this.querySelector("button");
    boton.removeEventListener("click", this.onClick.bind(this));
  }
  
  onClick() {
    var boton = this.querySelector("button");
    var etiqueta = boton.querySelector("span");
    
    this.contador += 1;
    etiqueta.textContent = this.contador;
  }
  
}
```

y por último vincularlo al documento así:

  
```javascript
customElements.define("contador-de-clicks", ContadorDeClicks);
```

Este es un pequeño preview de cómo funciona:

![](/images/2023/componentes-web/clicks-2.gif)


Con esto, se puede lograr un nuevo elemento, aislarlo del
resto de la aplicación y mejorarlo como una pieza
individual. Sin compilación, dependencias ni gestores de
paquetes.

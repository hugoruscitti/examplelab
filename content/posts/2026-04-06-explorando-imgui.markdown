---
layout: post
title: Explorando ImGui
date: '2026-04-06 00:00:00'
description: |
  De qué se trata ImGui y por qué me gustaría usarlo en mis juegos.
cover: /images/2026/explorando-imgui/portada.jpg
---

Hace mucho tiempo que tengo la idea de volver a hacer juegos, así que me propuse
empezar con algunos experimentos, mi intención es contarte acá lo que voy
descubriendo.

## Un juego con interfaz de usuario

Una idea que quiero explorar es la de exponer controles que me permitan observar
y ajustar variables del juego en tiempo de ejecución, me gusta la idea de hacer
un juego que incluya controles para mí, que estoy haciendo el juego, algo así
como un editor incluido en el mismo juego.

Buscando formas de hacer esto di con una biblioteca llamada ImGui, que se ajusta
muy bien a este tipo de desafíos.

Te muestro un ejemplo de lo que pude armar hasta ahora:

<iframe id="ejemplo" src="/explorando-imgui/index-canvas.html" style="border: 0" width=512 height=256></iframe>

<div>
<script>
function reiniciar() {
  let ejemplo = document.querySelector("#ejemplo")
  ejemplo.contentWindow.location.reload();
}
</script>
<a href="#" onclick="reiniciar(); return false">Reiniciar ejemplo</a>
</div>


Si interactuás con el ejemplo que está más arriba, vas a notar que el movimiento
del pájaro cambia de acuerdo a la variable `amplitud` y que la `opacidad` te
permite generar un efecto visual con solo deslizar el control.

Probá con valores como `opacidad = 0.1` y mové la ventana.

## El modelo inmediato

Lo que más me sorprendió de ImGui, es que te permite crear una interfaz como esa
de forma muy simple, porque podés invocar a los componentes directamente en el
bucle del juego así:

```javascript
let cuadro = 0;
let amplitud = 50;
let opacidad = 1;

iniciar();

while (true) {
  borrar_el_fondo(opacidad);

  ImGui.Text(`Cuadro de animación ${cuadro}`);
  amplitud = ImGui.SliderFloat('amplitud', amplitud, 0, 100);
  opacidad = ImGui.SliderFloat('opacidad', opacidad, 0, 1);
  
  dibujar_pajaro();

  await esperar(1/60);
}
```

Claro, este código está simplificado, pero es solo para ilustrar que no se requiere
mucho trabajo "mental" armar la interfaz de usuario así.

La interfaz se dibuja "al vuelo", cuadro a cuadro, como una animación dentro del
bucle del juego.

Pienso que la idea central de ImGui es permitirnos usar una API inmediata, que nos hace
pensar en los componentes como funciones que dibujan nuestra UI y
gestionan la interacción del usuario en un solo frame.

## ¿Y ahora?


Bueno, para mí es un cambio de enfoque que me gusta, yo venía pensando
interfaces de usuario de otra forma, pensando que:

- suele haber un "momento de inicialización" y construcción de los componentes.
- luego un bloque de código dedicado a "conectar eventos con callbacks".
- y finalmente alguna función para "delegar y esperar" el resto a la biblioteca.


Pero acá, con ImGui, aparece algo más fácil de pensar e integrar, al menos para
mí. Si quiero controlar una variable simplemente puedo dibujar un deslizador en
pantalla y listo.

Otra cosa que me gusta mucho es que se puede entender "cómo funciona" la
aplicación mirando una porción de código muy breve, sin tener que navegar entre
funciones, clases o distintos archivos. Esto me recordó mucho a la idea del
autor de htmx sobre lo valioso de
[mantener las cosas juntas](/posts/2023-03-06-las-cosas-cerca/), del que
escribí hace un tiempo.

Y por supuesto me gusta mucho que tenga una demo web con todo lo que se puede
hacer: https://pthom.github.io/imgui_explorer/

Ahora me queda seguir jugando un poco más con estas ideas y ver qué sale de
estos experimentos divertidos.

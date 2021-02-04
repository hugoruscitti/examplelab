---
layout: post
title: El regocijo de usar VIM
date: '2021-02-03 00:00:00'
description: |
  VIM es un editor único, incorpora un lenguaje para hacer
  operaciones de manera muy directa y tal vez eso sea lo
  más interesante de todo.
cover: /images/2021/el-regocijo-de-usar-vim/portada.jpg
---

VIM es un editor de texto muy particular, para empezar: está
ligeramente orientado a facilitar operaciones como navegar y editar
texto en lugar de ser un editor principalmente para escribir. Esto
hace que toda la experiencia de usar la herramienta esté mediada
por este enfoque inicial.

Por ejemplo, cuando ingresas en VIM, el editor espera que ingreses
comandos pulsando teclas, en lugar de trasladar esas teclas en caracteres
y colocarlas en el archivo de texto como hacen la mayoría de los
editores de texto.

Esto tiene algo bueno y algo malo:

Lo bueno es que tu teclado se transforma en una especie de tablero
de control que te permite hacer casi cualquier cosa de manera
muy rápida y eficiente.

Lo malo es que todas esas perillas y comandos están ocultas, invisibles
hasta que sabes cómo usarlas.

# Comandos de alto nivel

Gran parte de las operaciones y cambios que hago en el código o
en los textos es de la forma "Quiero cambiar el contenido de este
string", "quiero mover este tag html a un template diferente", "Necesito
agregar otro parámetro a esta función" etc...

Vim tiene un lenguaje para hacer todas estas cosas, nunca te ves
obligado a hacer desplazamientos hacia arriba y abajo buscando cosas
o pulsando 20 veces `backspace` para sustituir una cosa por otra.

Por ejemplo, para cambiar el contenido de un string basta con
escribir `ci"` (que se puede interpretar como **c**hange **i**nner **"**).

Algo similar ocurre con los tags html, si queremos seleccionar una
región de etiquetas podemos invocar `vit` (**v**isual select **i**n **t**ag)
o `vat` (para seleccionar el tag completo, y no solo su contenido).

Y esta regla básica del lenguaje sirve para construir varias combinaciones
diferentes:

{{<figure src="/images/2021/el-regocijo-de-usar-vim/lenguaje.png" caption="Descomposición de una operación de selección en vim">}}

Y lo más interesante, es que en el momento en que tomas práctica te
das cuenta que ni siquiera necesitas seleccionar el texto antes de hacer
algo con él.

VIM me permite evitar las ceremonias antes de hacer cambios, si quiero
borrar algo no necesito seleccionarlo previamente. Por ejemplo `dap` sirve
para borrar un párrafo entero.

# Movimientos rápidos

Los movimiento del cursor también son importantes, no solo para navegar
el código, sino también para hacer ajustes rápidos.

Yo uso un montón el comando `/` y `?` que sirven para iniciar una búsqueda
rápida y mover el cursor. Además, uso mucho `c-o` para volver a la posición
anterior del cursor.

Es muy práctico moverse así, el editor recuerda todos nuestros movimientos.

Otro ejemplo, si estoy editando código Python es probable que ejecute
el comando `/def` para ir al primer método o función de un archivo, ahí puedo
pulsar `n` para ir al siguiente método e ir saltando entre funciones.

En otros editores que no tienen un lenguaje como este lo más fácil termina
siendo usar el mouse para seleccionar zonas particulares, o pulsar muchas
veces las flechas del teclado para movernos por el código.


# Sin distracciones

Otra cosa curiosa del editor es que su interfaz es mínima, casi todo
está disponible a unas pulsaciones de teclas y no necesita de iconos, menúes
o ventanas.

{{<figure src="/images/2021/el-regocijo-de-usar-vim/goyo.png" caption="Vim con el plugin Goyo activo para escribir">}}

A mí me resulta estéticamente atractivo, la pantalla está disponible al 100%
para lo que estoy haciendo, los caracteres se ven grandes, sin distracciones
y ninguna interrupción.

# Vine por la eficiencia pero me quedé por la diversión

El momento más importante para mí al usar Vim fue cuando comprendí las
reglas básicas del lenguaje y cómo se podían componer comandos. Antes
de ese ese momento, me movía como loco y pulsaba muchas veces la mismas
teclas para borrar o moverme por el texto.

Y aquí es donde creo que experimenté un "click" al momento de usar el
editor. No se si fue un "click" saludable, tal vez el "click" es el
sonido de un tornillo que se cayó o algo así... pero lo cierto es
que desde ese momento comencé a disfrutar mucho de este editor.

La sensación de poder expresar con pocas teclas operaciones casi a la
velocidad del pensamiento es muy atractiva, operar usando comandos
de bloques o crear macros es casi como armar rompecabezas en el aire
y verlos funcionar en la pantalla. 

Es cierto que este enfoque hace que seas más rápido a la hora de hacer
cambios, aunque para mí es más importante sentir que el proceso de usar
la herramienta es desafiante y se aprende algo nuevo cada tanto.

Me sigue sorprendiendo que después de tantos años siga
siendo divertido usar este editor para trabajar todos los días.

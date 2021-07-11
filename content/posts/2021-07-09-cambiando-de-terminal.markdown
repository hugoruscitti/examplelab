---
layout: post
title: Cambiando de terminal a Alacritty
date: "2021-07-09 00:00:00"
description: |
  Cambié de terminal y comencé a encontrar varias cosas
  interesantes para mencionar.
cover: /images/2021/cambiando-de-terminal/portada.jpg
---

Hace una semana comencé a utilizar un emulador de terminal llamado
[Alacritty](https://github.com/alacritty/alacritty) en lugar de [iterm2](https://iterm2.com/), el
terminal que venía usando hace años.

![](/images/2021/cambiando-de-terminal/terminal.png)

En realidad no tengo un motivo muy importante para dejar de usar [iterm2](https://iterm2.com/), pero
moverme a otro terminal es una excusa para revisar mis archivos de configuración
y buscar una forma más práctica de trabajar.

Algo curioso de Alacritty es que no tiene tabs, pantallas de configuración
o menús; se configura desde un archivo de texto y es muy minimalista. Además
promete ser más rápido que otros terminales porque dibuja en pantalla usando
aceleración de video.

No sé muy bien por qué, pero me gusta que el emulador de terminal tenga poca
funcionalidad, me da la sensación de que el proyecto puede
avanzar más rápidamente y lograr estabilidad.

Después de todo, mucha de la funcionalidad "extra" que pretendo de
un terminal se puede obtener usando [tmux](https://github.com/tmux/tmux/wiki).

# Configuración

Me gusta que la configuración de Alacritty esté en un archivo de texto, porque
fácilmente puedo recorrer las opciones, identificar qué quiero cambiar y
resguardar todo.

Además, que se trate de texto ayuda a copiar y tomar ideas de otras personas, por
ejemplo la configuración de colores que estoy usando simplemente la copié
y pegué del proyecto [dracula-theme](https://draculatheme.com/alacritty):

![](/images/2021/cambiando-de-terminal/colores.png)

Ah, y cualquier cambio que hagamos a la configuración se recargará
automáticamente, lo que hace que sea mucho más rápido ajustar y evaluar
cambios de configuración.


# Configurando los atajos de tmux

Hace tiempo que quiero habituarme a usar [tmux](https://github.com/tmux/tmux/wiki) todos
los días y con esta transición a Alacritty me vi forzado a hacerlo.

Con tmux ahora puedo tener tabs y splits:

![](/images/2021/cambiando-de-terminal/tabs.png)

Sin embargo, tuve que configurar algunas cosas para sentirme más cómodo a la
hora de trabajar.

Por ejemplo, para cambiar de tabs en tmux hay que pulsar una secuencia
de caracteres, como `ctrl-b` y luego el número de tab al que queremos ir. Mientras
que para mí, lo ideal sería pulsar simplemente `cmd-1` o `cmd-2` para ir a
un tab específico.

Además, tengo el hábito de crear tabs con `cmd-t` como hacía con [iterm2](https://iterm2.com/), y la
forma que me ofrece tmux de hacer lo mismo me resulta incómoda. En tmux tendría
que pulsar `ctrl-b` y luego la tecla `c`.

Por suerte estos atajos se pueden
personalizar desde el mismo archivo de configuración de alacritty `~/.alacritty.yml`:

```javascript
  # Abrir tabs nuevos con cmd-T
  - { key: T,        mods: Command,     chars: "\x05\x63" }

  # Acceder a los tabs con números
  - { key: Key1,     mods: Command,     chars: "\x05\x31" }
  - { key: Key2,     mods: Command,     chars: "\x05\x32" }
  - { key: Key3,     mods: Command,     chars: "\x05\x33" }
  - { key: Key4,     mods: Command,     chars: "\x05\x34" }
  - { key: Key5,     mods: Command,     chars: "\x05\x35" }
  - { key: Key6,     mods: Command,     chars: "\x05\x36" }
  - { key: Key7,     mods: Command,     chars: "\x05\x37" }
````

Las claves `key` y `mods` le indican a Alacritty qué teclas queremos
modificar, mientras que `chars` son los caracteres de escape que queremos
invocar.

Para generar esos caracteres de la forma `\x05\x31` seguí [las instrucciones
que aparecen en un artículo](https://arslan.io/2018/02/05/gpu-accelerated-terminal-alacritty/) sobre
alacritty. Básicamente hay que usar el comando `xxd -psd`, pulsar el atajo de teclado que
nos gustaría invocar y anotar la secuencia de caracteres que aparece en pantalla.

Por ejemplo, si ejecuto `xxd -psd` y pulso la secuencia de caracteres
`ctrl-b` y luego `c`, el número que se imprime en pantalla es este:

```
→ xxd -psd
^Bc
02630a
```

De donde `02` simboliza `ctrl-b`, `63` a `c` y por último `0a` simboliza
la tecla `enter`.

# Soporte TrueColor

Para que los colores se vean correctamente dentro de tmux y vim tuve que
cambiar algunas cosas más.

Lo primero que hice fue ejecutar [unos
scripts](https://gist.github.com/XVilka/8346728) para imprimir colores en
la terminal y verificar si se veía correctamente.

Noté que los colores se veían perfectos en Alacritty, pero no se veían bien
dentro de tmux:

![](/images/2021/cambiando-de-terminal/comparativa.png)

Luego edité la configuración de tmux agregando esto:

```
set-option -ga terminal-overrides ",*256col*:Tc"
set -g default-terminal "screen-256color"
```

y esta otra configuración dentro de vim:

```
"Agrega soporte para truecolor
if exists('+termguicolors')
  let &t_8f = "\<Esc>[38;2;%lu;%lu;%lum"
  let &t_8b = "\<Esc>[48;2;%lu;%lu;%lum"
  set termguicolors
endif
```

¡Y listo!

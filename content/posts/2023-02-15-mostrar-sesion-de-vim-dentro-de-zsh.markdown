---
layout: post
title: Mostrar si estamos dentro de vim en zsh
date: '2023-02-13 23:00:00'
description: "Mi configuración de zsh para indicar si estamos en el shell de VIM."
cover: "/images/2023/mostrar-sesion-de-vim-dentro-de-zsh/portada.jpg"
tags:
- vim
---

Vim tiene un comando llamado `:shell` que te permite abrir
un terminal, ejecutar algunos comandos y regresar nuevamente
al editor escribiendo `exit`.

En cierta forma, es similar a pausar VIM, ponerlo en segundo
plano, ejecutar algunos comandos y luego volver al editor.

Este comando me resulta muy práctico, pero tiene un
problema: a veces permanezco en esa sesión de terminal por
unos cuantos minutos y luego no recuerdo si estaba en VIM o
no.

¿Por qué esto es un problema para mí?, bueno... digamos que
a veces escribo 'exit' en el terminal esperando regresar a
VIM y no, termino saliendo por completo de mi sesión.


## ¿Cómo identificar si estamos dentro del shell de vim?

Busqué cómo resolver esto y noté que VIM coloca una variable
de entorno llamada VIM cuando abrimos el comando `shell`:

```
→ env | grep VIM=
VIM=/opt/homebrew/share/vim
```

Entonces, para poder identificar si estamos en una sesión
del `shell` de VIM podemos simplemente consultar si esa
variable existe o no.

Lo siguiente, es la configuración que estoy usando para
cambiar el `prompt` de `zsh`:


```
export EN_VIM=""
[[ -v VIM ]] && export EN_VIM="(en vim shell)"

export PS1=$'... ➖ ${EN_VIM}\n→%f '

```

y así es como se ve en funcionamiento:

![](/images/2023/mostrar-sesion-de-vim-dentro-de-zsh/prompt.png)


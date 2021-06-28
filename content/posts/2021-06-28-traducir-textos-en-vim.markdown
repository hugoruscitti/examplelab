---
layout: post
title: Traducir textos en vim
date: '2021-06-28 00:00:00'
description: |
  Cómo traducir cadenas de textos desde VIM muy rápidamente.
cover: /images/2021/traducir-textos-en-vim/portada.jpg
---

Estoy trabajando en una aplicación web que tiene que soportar
tres idiomas diferentes: inglés, español y portugués.

Tenemos tres archivos con los mensajes de la aplicación separados, un
archivo por cada idioma así:

```javascript
{
[...]
  cargarNuevamente: "Seus dados já foram enviados. Não é {NAME}?",
  cargarNuevamenteLink: " Clique aqui.",
  cerrar: "Fechar",
  ciudad: "Cidade",
  comienzo: "Começo do projeto",
  completeDatos: "Registre-se e obtenha as informações das oportunidades.",
[...]
}
```


El tema es que cada vez que agregamos mensajes o pantallas tengo que
salir del editor, y traducir los mensajes a todos los idiomas. Para
esto tengo que abrir Google Translate, buscar, copiar y pegar.

Hacer esto por cada texto es incómodo, sin bien no me lleva mucho tiempo, el
problema es que me obliga a hacer un "cambio de contexto" que podría evitarlo.

Así que me puse a buscar herramientas y di con un complemento para vim
llamado [vim-translator](https://github.com/voldikss/vim-translator).

Este complemento me permite traducir textos directamente desde el editor, sin
tener que salir ni abrir un navegador. Además, viene con varios comandos para
traducir texto selecciona o el contenido del archivo completo.

Ahora en mi caso, como los textos están generalmente enmarcados entre comillas,
hice tres atajos para agilizar las cosas.

```
map ttn vi":'<,'>TranslateR --target_lang=en<cr>
map tte vi":'<,'>TranslateR --target_lang=es<cr>
map ttp vi":'<,'>TranslateR --target_lang=pt<cr>
```

Así, cuando estoy posicionado sobre un texto y pulso `ttn` el texto se traduce
al inglés, cuando estoy sobre un texto y pulso `tte` se traduce a español y con
`ttp` se traduce al portugués.

El complemento detecta el lenguaje de origen, así que alcanza con indicarle a qué
idioma queremos traducir el texto y listo.

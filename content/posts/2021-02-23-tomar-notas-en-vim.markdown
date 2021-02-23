---
layout: post
title: Tomar notas en VIM
date: '2021-02-23 00:00:00'
description: |
  Estuve experimentando en tomar notas en VIM en lugar
  de la aplicación Bear que uso a diario.
cover: /images/2021/tomar-notas-en-vim/portada.jpg
---

Tomar notas está bueno, te da mucha claridad sobre lo que estás haciendo
día a día y es una buena oportunidad para hacer una pausa, reflexionar y
tomar alguna que otra decisión.

Uso una aplicación llamada [Bear](https://bear.app/) para tomar todas
mis notas, algunas notas se convierten en bocetos de artículos que me
interesan, resúmenes
de libros e incluso algunas notas van dedicadas a una especie de diario
personal que uso para reflexionar.

Sin embargo, una cosa que no me gusta de [Bear](https://bear.app/) es que
no es una herramienta que puedo tener en mi poder; Bear tiene su propio
modelo de negocio, sus "features" adicionales y un sistema de
suscripción que me gustaría abandonar.

Al principio me resultaba atractivo usar la herramienta y ver cómo crecía, pero
desde hace un buen tiempo reconocí que uso una parte muy pequeña de su
funcionalidad, en particular estas tres:

- Me permite colocar imágenes fácilmente, solo arrastrar y soltar.
- Tiene un motor de búsquedas.
- Me permite poner tags, para poder diferenciar los tipos de notas.

# ¿Y Markdown no hace todo eso?

Bueno sí, en realidad si, pero aún así me faltaría alguna herramienta
para cargar imágenes en las notas y que sea sencillo exportar.

Así que me puse a investigar si podía reemplazar Bear con VIM. Obviamente
no quiero el 100% de la funcionalidad de Bear, solamente las cosas que
uso a diario.

# Cómo visualizar notas en VIM

Una opción rápida es poner todas las notas en un directorio y generar
un sitio web usando algo como [Jekyll](https://jekyllrb.com/) o [Hugo](https://gohugo.io/).

Sin embargo noté que muy rara vez quiero ver las notas en HTML, me
alcanza con navegarlas directamente desde VIM y verlas en su
formato original, en markdown.

En los únicos momentos que quiero ver la nota es formato HTML es
cuando tiene imágenes.

Para esos casos, hice un atajo en VIM para generar una versión
`.html` de la nota y verla en el navegador:

```
map <leader>P :!pandoc % -o ./tmp.html --standalone --metadata title="nota"; open tmp.html<CR>
```

El atajo es bastante rudimentario, pero es un buen comienzo, si veo que me resulta útil puedo
mejorarlo, y sino descartarlo por otra cosa.

# Cómo agregar imágenes a las notas

Para incoporar imágenes lo más práctico que encontré es un plugin
llamado [md-img-paste](https://github.com/ferrine/md-img-paste.vim).

Este plugin permite "pegar" la imagen que tengamos en el portapapeles
del sistema directamente en el buffer de VIM. 

El plugin se encarga de generar un archivo .png con la imagen, nos
consulta qué nombre queremos ponerle al archivo y también nos genera
el código markdown dentro del buffer.

Esto me resultó super útil, incluso noté [que la aplicación que uso
para capturar imágenes](https://monosnap.com/) automáticamente pone en el portapapeles del
sistema la imagen que captura. Así que para poner imágenes en un
documento simplemente: tomo la captura, activo la ventana de VIM y pulso
`<leader>i`.

Por cierto, también agregué esta configuración a mi archivo `vimrc`:

```
nmap <buffer><silent> <leader>i :call mdip#MarkdownClipboardImage()<CR>
```

Ahora me queda pendiente la tarea de migrar todas mis notas a VIM
y dar de baja Bear :P

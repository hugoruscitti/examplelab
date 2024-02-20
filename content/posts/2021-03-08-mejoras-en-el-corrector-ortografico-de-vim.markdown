---
layout: post
title: Mejoras en el corrector ortográfico de VIM
date: '2021-03-08 00:00:00'
description: |
  Vim puede funcionar junto a un corrector ortográfico
  que detecta errores gramaticales que se llama LanguageTool.
cover: /images/2021/mejoras-en-el-corrector-ortografico-de-vim/portada.jpg
tags:
- vim
---

VIM incluye un corrector ortográfico que se puede activar con estos comandos:

```
set spell
set spelllang=es
```

Sin embargo, este corrector solamente puede ayudarnos a detectar *typos* y
algunas faltas de ortografía simples.

Lo bueno es que VIM puede usar un corrector más
completo llamado [LanguageTool](https://languagetool.org/es), que además de detectar errores ortográficos
también detecta otros tipos de errores, como usos incorrectos de artículos, frases
complejas y más.

## ¿Qué es LanguageTool?

[LanguageTool](https://languagetool.org/es) es una herramienta que puede analizar textos
y realizar sugerencias para mejorar ortografía, gramática y estilo. La herramienta tiene
un modelo de negocio y planes, pero también está disponible para descargar y utilizar
bajo la licencia LGPL como indican en el repositorio de [github](https://github.com/languagetool-org/languagetool)

Una forma de verificar lo que puede hacer esta herramienta es visitar su sitio
web y jugar con el editor de texto que aparece en la pantalla:

![pagina](/images/2021/mejoras-en-el-corrector-ortografico-de-vim/pagina.png)

Una de las correcciones que me sorprendió es cómo reconoce el uso incorrecto de
preposiciones y concordancia.


## ¿Cómo se integra a VIM?

Para usar esta herramienta lo primero que tenemos que hacer es instalar
un *plugin* llamado [vim-grammarous](https://github.com/rhysd/vim-grammarous).

En mi caso, como uso un gestor de paquetes llamado [vim-plug](https://github.com/junegunn/vim-plug) lo
que tuve que hacer es agregar esta línea dentro de mi archivo `vimrc`:

```
Plug 'rhysd/vim-grammarous'
```

y luego ejecutar el comando:

```
:PlugInstall
```

Luego de ejecutar esos comandos, necesitamos activar el análisis de un
texto por primera vez para se descarguen algunos archivos más:

```
:GrammarousCheck --lang=es
```

Resulta que *LanguageTool* funciona como una herramienta externa que incluye
diccionarios y varios componentes internos, así que en la primera invocación
va a necesitar instalar todo esto para continuar. En mi caso, la instalación
consumió unos 300 MB.

## Unas pruebas

Cuando activamos la corrección la pantalla de VIM se divide en dos partes, por
un lado nuestro texto y por el otro un detalle de cada error.

![fecha](/images/2021/mejoras-en-el-corrector-ortografico-de-vim/fecha.png)

En la captura de arriba se vé que la herramienta incluso interpreta fechas, y
describe con claridad por qué considera que hay algo mal.

## Configuraciones adicionales

Al igual que sucede con otros complementos, podemos configurar algunos atajos
para activar esta extensión fácilmente.

En mi caso, hice que el editor active la corrección pulsando `<space>`
y luego `s`:

```
noremap <leader>s :GrammarousCheck --lang=es<CR>
noremap <leader>a :GrammarousReset
```

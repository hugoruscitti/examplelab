
---
layout: post
title: Eliminar palabras en VIM
date: '2021-03-30 00:00:00'
description: |
  Algunos consejos sobre cómo eliminar palabras
  en VIM y configuraciones útiles.
cover: /images/2021/eliminar-palabras-en-vim/portada.jpg
---

Uno de los comandos que uso mucho en *vim* es `change`. Este comando
que se puede combinar con un movimiento para cambiar párrafos, palabras, texto
delimitado entre comillas y más.

Una vez que te acostumbras a los comandos de *vim* ya ni pensás en ellos, `cw` cambia
una palabra, `cap` un párrafo y `ci"` el contenido entre comillas etc..

Poder navegar entre palabras y hacer cambios rápidos está muy
bueno cuando tenés código como este, donde hay delimitadores como
las comillas, espacios y tags:

![texto](/images/2021/eliminar-palabras-en-vim/texto.png)

Sin embargo, hay algo que hace tiempo que me resultó sorpresivo y
luego de investigar me di cuenta que se puede configurar: para *vim*, el
guion medio es un separador de palabras.

Por ejemplo, aquí *vim* identificará 7 palabras dentro de las comillas:

![palabras](/images/2021/eliminar-palabras-en-vim/palabras.png)

Pero si estamos editando clases en un elemento, el guion del medio no es
un separador, el guion es parte del nombre de la clase.

Si pulsamos `cw` sobre la clase `bg-light-gray` *vim* pensará que queremos
cambiar la palabra `bg` en lugar del nombre completo de la clase.

Por suerte *vim* tiene un parámetro para cambiar este comportamiento:

```
set iskeyword+=-
```

Colocando esta configuración en el archivo `.vimrc` ahora los nombres de
clases se pueden cambiar como si fueran solo 3 palabras:

![palabras conciderando guiones](/images/2021/eliminar-palabras-en-vim/palabras2.png)

Obviamente *vim* está repleto de estos detalles configurables, pero este es uno de
los que quería mencionar hoy porque estuve editando clases css como un loco :P


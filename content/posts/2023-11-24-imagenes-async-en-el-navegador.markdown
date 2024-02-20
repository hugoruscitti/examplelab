---
layout: post
title: Imágenes "Lasy" en el navegador
date: '2023-11-24 00:00:00'
draft: false
description: |
 Cómo hacer que la carga de imágenes se haga bajo demanda
 en html.
cover: /images/2023/imagenes-async-en-el-navegador/portada.jpg
tags:
- web
---

Esta semana aprendí algo nuevo sobre la etiqueta **img**:

Resulta que podemos indicarle al navegador si en nuestro
sitio se pueden cargar las imágenes bajo demanda, a medida
que el usuario desplaza el contenido.

Lo único que tenemos que hacer es armar la etiqueta *img* de esta forma:

```javascript
<img loading="lazy" src="/images/2013/pilas/portada.jpg"/>
```

# Probando el cambio en mi blog

Para aprovechar la ocasión se me ocurrió mejorar la forma en
la que se cargan las imágenes en este blog, a ver si notaba
algún resultado.


Hace unos días, cuando se ingresaba a este blog el navegador
cargaba todas las portadas de artículos juntas:

![](/images/2023/imagenes-async-en-el-navegador/antes.png)

Es decir, hacía 111 peticiones para cargar todas las
imágenes.

Ahora, cambiando las etiquetas *img* para que se carguen
bajo demanda el navegador solamente solicita las imágenes a
medida que las necesita.

Esta es una captura de pantalla de las peticiones que hace
el navegador al ingresar al blog:

![](/images/2023/imagenes-async-en-el-navegador/despues.png)



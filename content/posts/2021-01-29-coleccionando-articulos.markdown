---
layout: post
title: Coleccionado artículos web
date: '2021-01-29 00:00:00'
description: |
  La web es un espacio espectacular para aprender pero
  las cosas no duran mucho, muchos sitios se mudan, cambian
  los contenidos o desaparecen por
  completo. ¿Cómo podemos salvar aquello que es valioso
  para nosotros?
cover: /images/2021/coleccionando-articulos/portada.jpg
---

Hace unos meses vi un artículo llamado [This Page is Designed to Last](https://jeffhuang.com/designed_to_last/)
que me hizo pensar en lo efímera que es la web.

El artículo describe cómo va cambiando la web con los años: y como los
artículos, foros, tutoriales y recursos dejan de existir de un día para otro.

Y esto no es algo que solo afecta a quienes publican contenido en la web, también afecta
a quienes leemos, aprendemos y queremos compartir lo que nos gusta de la web con otras
personas:

Imagina que tenes un link a un artículo que te impactó, mejoró tu vida profesional y
expresa algo tan valioso para vos que quisieras preservar y recomendar a tus amigos:

- https://steve-yegge.blogspot.com/2008/09/programmings-dirtiest-little-secret.html

¿Cuántos años seguirá funcionando ese link?, ¿qué tal si el dueño de ese blog pierde el interés en
su blog?, ¿qué pasará si la plataforma blogspot.com deja de existir como ocurrió con [geocities](https://es.wikipedia.org/wiki/GeoCities)?

Lo más probable es que pase esto:

{{<figure src="/images/2021/coleccionando-articulos/404.png" caption="Lo que antes era un baúl de sabiduría...">}}

De hecho, esa captura de pantalla no es casual, el link que intenté abrir corresponde
a un proyecto de traducción enorme en donde había mucho conocimiento y textos
que fueron muy importantes para mí. <sup>1</sup>

# Una solución: Descargar y guardar

Creo que una forma de cuidar y preservar estos recursos es descargar y guardar, tan simple como eso... los dominios pueden vencer, los servidores se pueden apagar o cambiar de lugar, sin embargo una copia del contenido en nuestro poder está... bueno.. en nuestro poder.

La copia que podemos hacer de un artículo no tiene por qué tener imágenes, cabeceras
o el estilo del sitio original; se puede tener un buen archivo de materiales
descargando:

* 1 - El texto del artículo, con títulos y párrafos.
* 2 - El nombre del artículo
* 3 - (opcional) Un detalle con la fecha en que se hizo el archivo.
* 4 - (opcional) La url original para consultar la versión original, si es que aún existe.


Por ejemplo, el artículo que cité antes se podría descargar y conservar para que
se vea así:


# Automatizando el proceso

Descargar un artículo directamente con el navegador es fácil, sin embargo mi idea no
es solo descargar sino descargar, almacenar, clasificar y formar una buena colección
de artículos fácilmente, con un solo comando.

Para eso hice una nueva página en mi blog llamada ["links"](/links), en donde voy
a colocar todos los artículos descargados.

Además, para hacer más sencillo el proceso armé un script en python
que me permite agregar páginas en ese archivo:

- [código del script descargar](https://github.com/hugoruscitti/dotfiles/blob/master/bin/descargar) 


Para usar este script simplemente hay que ejecutar el siguiente comando
en una consola:

```
./descargar URL
```

El script se encarga de descargar el artículo, lo convierte en markdown, agrega
un link dentro de ["links.md"](/links) y deja todo listo para que puedas revisar los
archivos y volver a subir el blog.

### Notas

1 - Puede muy sonar dramático, sin embargo en este caso puntual los artículos de Joel siguen existiendo [gracias a una copia](https://web.archive.org/web/20170505143403/http://local.joelonsoftware.com/mediawiki/index.php/Espa%C3%B1ol) que
realizó el proyecto [Internet Archive](https://archive.org/).

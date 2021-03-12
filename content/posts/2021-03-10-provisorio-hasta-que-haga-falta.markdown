
---
layout: post
title: Provisorio hasta que haga falta
date: '2021-03-10 00:00:00'
description: |
  ¿Conviene hacer las cosas bien o esperar a que sea realmente
  necesario?
cover: /images/2021/provisorio-hasta-que-haga-falta/portada.jpg
---

Hace más de dos años hice una *API* para que los usuarios de
[pilas-engine](https://www.pilas-engine.com.ar) puedan guardar
y compartir sus juegos a través de una *url* pública.

![](/images/2021/provisorio-hasta-que-haga-falta/exportar.png)

Esto funcionó a la perfección por más de dos años... pero ayer empezó
a dar problemas: El equipo en donde estaba corriendo esta aplicación se quedó sin
espacio disponible y cuando me puse a investigar encontré que una de
las bases de datos había crecido un montón.

Mirando por arriba, noté que algo andaba mal, porque para mí una base de
datos que solamente tiene que guardar juegos hechos con *pilas-engine* no
podía ser demasiado grande.

Lo peor de todo es que yo sabía que iba a dar problemas, cuando hice esa
*api* hace unos años pensé que sería buena idea guardar el juego serializado, en
[base64](https://en.wikipedia.org/wiki/Base64), de modo que sea sencillo guardar y leer los juegos.

Es decir, sin compresión, sin archivos, todo en la base de datos para que
sea rápido de implementar.

Ahora, después de dos años, estoy un poco arrepentido de no haberlo hecho mejor
al principio. Me hubiera ahorrado un par de horas y algo de incertidumbre por
la falta de espacio en el disco, investigar y tener que *ponerme a arreglar las cosas*.

Sin embargo, este problema me dio la posibilidad de descubrir algunas
cosas que no sabía:

Cuando noté que el problema podía ser a causa de la base de datos, me puse
a mirar algunos registros, y me sorprendió
ver que el problema de espacio no era tanto un problema de programación, sino
que ¡La *api* de *pilas* realmente está siendo utilizada!.

Al principio no creía que hacer un mini servicio para guardar y compartir juegos
podría ser útil, pero hoy me
doy cuenta de que sí. Me resulta más gratificante hacerle mejoras al código sabiendo
que se utiliza, y que cualquier mejora que le haga va a servirle a los usuarios.

Esta es una captura de varios de los juegos que me encontré:

![](/images/2021/provisorio-hasta-que-haga-falta/capturas.jpg)

## Arreglando el problema

Mejorar la *api* para que no ocupe tanto espacio me llevó varias horas, el primer
paso fue bajar la base de datos a mi equipo y modificar el esquema para que los datos del
proyecto se guarden como archivos `.zip`. Luego tuve que migrar todos los registros
con un script, para generar un `.zip` con cada proyecto y luego eliminar los campos
que ya no se utilizarán.

Ah, y en el camino aprendí que *PostgreSQL* te permite listar el tamaño de las
tablas más grandes ejecutando este *query*:

```
SELECT relname AS "Table",
       Pg_size_pretty(Pg_total_relation_size(relid)) AS "Size",
       Pg_size_pretty(Pg_total_relation_size(relid) - Pg_relation_size(relid)) AS "External Size"
FROM   pg_catalog.pg_statio_user_tables
ORDER  BY Pg_total_relation_size(relid) DESC;
```

Además, existe un comando llamado `VACUUM FULL` que libera espacio luego
de que cambiamos el esquema o reducimos la cantidad de datos.

En fin, lo que para mí empezó como una clásica historia de deuda técnica y código
provisorio, resultó ser algo más que eso... me quedé pensando que tal vez no
me hubiera dado cuenta de lo útil que es esa *api* si la cosa no hubiera fallado.

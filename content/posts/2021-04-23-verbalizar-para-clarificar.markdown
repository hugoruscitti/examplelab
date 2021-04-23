
---
layout: post
title: Verbalizar para clarificar
date: '2021-04-23 00:00:00'
description: |
  Cómo se pueden resolver algunos problemas cambiando de enfoque y clarificando.
cover: /images/2021/verbalizar-para-clarificar/portada.jpg
---

Hoy pude terminar de resolver un problema que tenía
en un proyecto hace días.

Básicamente tenía que lograr que dos sistemas se hablen
entré si, a través de una *api*, pero la única forma que tenía
de hacer pruebas era mediante una interfaz web que no me
daba mucha información:

![](/images/2021/verbalizar-para-clarificar/webapi.png)

No veía si efectivamente se llamaba a la *api*, si se estaban
enviando los parámetros correctamente, si había algún tipo
conversión de datos en el medio, o si la respuesta tenía algún
tipo de incongruencia.

Cuando me encuentro haciendo cosas de esta manera me cuesta
tener claridad, puedo pasar un buen rato  peleando conmigo mismo
haciendo pruebas tras pruebas sin dar con la solución como en esta
imagen (pero con menos pelo):

![](/images/2021/verbalizar-para-clarificar/meme.jpg)

El punto es que todo se vuelve peor cuando no tengo claridad, sigo abriendo
pestañas en el navegador intentando dar con la respuesta a algo que ni
siquiera comprendo.

# Cambiando de enfoque

Lo que me ayudó a resolver el problema fue cambiar de enfoque, en lugar de
seguir probando cosas comencé a verbalizar:

Verbalizar consiste en hacerse 
preguntas tontas como las siguientes: ¿Qué problema tengo?, ¿cómo
se lo explicaría a alguien desde el principio? o ¿qué pruebas estoy haciendo y
qué conclusiones puedo sacar de ellas?.

Insisto en que son preguntas tontas, porque obviamente sé qué problema tengo: ¡la cosa no
funciona y no veo el error!. Sin embargo, cuando me pongo a verbalizar empiezo
a construir un modo de pensar distinto; si tuviera que explicarle a alguien el
problema en voz alta no le diría "es que no anda, y no sé por qué". Me esfuerzo
por ser más claro y detallado.

Cuando verbalizo un problema me resulta natural empezar por el principio, separo las
cosas importantes de las que no lo son, me doy cuenta de que mis ideas y las frustraciones
son cosas distintas y busco ser objetivo sobre las cosas que estoy probando.

Así que hoy hice ese ejercicio, comencé a escribir un documento con el detalle del
problema, algunas capturas de pantalla para describir las pruebas que estaba haciendo y
mientras escribía logré darme cuenta de dónde estaba el problema.


Esto no es nuevo, de hecho hace un tiempo escuché que algunas personas usan
un método llamado [Rubber Duck Debugging](https://en.wikipedia.org/wiki/Rubber_duck_debugging) que
simplemente consiste en tratar de explicar el problema en voz alta para clarificar ideas.

Claro, el truco no está en el patito de goma o el documento que escribís, sino en el ejercicio
de sacar cosas de la cabeza, ordenarlas y poder clarificarlas.

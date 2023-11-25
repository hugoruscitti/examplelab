---
layout: post
title: Simplificando por un motivo accidental
date: '2023-11-24 00:00:00'
description: |
  Cambié la forma de hacer releases en pilas, usando menos
  herramientas y haciendo todo más simple.
cover: /images/2023/simplificando-por-un-motivo-accidental/portada.jpg
---

Me propuse publicar una nueva versión de pilas, pero como no
hacía esto hace tiempo aparecieron problemas.

El mecanismo para publicar versiones estaba automatizado,
con *tests*, integración continua, generación automática de
binarios en circle-ci y publicación.

Lamentablemente, mucha de la automatización que tenía
funcionando para hacerme la vida más fácil dejó de
funcionar: el sistema de CI me
informó que mis imágenes de docker estaban en desuso, github
cambió unas llaves por un tema de seguridad así que el
servidor no pudo actualizar los binarios y los
*tests* dejaron de iniciar (y aún no se por qué).

Obviamente me puse a investigar e intentar corregir las
cosas pero llegué a este punto: "no anda nada"

![](/images/2023/simplificando-a-la-fuerza/fails.png)

Sentí que toda la estructura que funcionaba perfecto se vino
"abajo" sin una causa directa. Así que en lugar de seguir
intentando arreglarlo me puse a pensar en el "sistema
completo" y si quería seguir manteniendo todo eso.


Por una lado, es razonable que la automatización deje de
funcionar con el paso del tiempo. Mucho de lo que hice
depende de servicios externos; las empresas actualizan su
software, las versiones nuevas sustituyen las anteriores,
aparecen otras herramientas, la gente deja de usar lo
anterior, lo viejo deja de funcionar etc..

Elegí automatizar para "facilitar" mi trabajo, y todo
funcionaba bien, pero el resultado fue algo complejo y
frágil.

## Esperado vs resultado

Entiendo que las cosas técnicas funcionen de esta forma, es
una filosofía de desarrollo: hacer pequeños cambios,
balancear desarrollo y mantenimiento, ir pagando la *deuda
técnica* poco a poco tiene sentido.

Sin embargo, mi mirada del problema venía por otro lado, mis
expectativas eran muy diferentes. Me vi teniendo preguntas
de este tipo:

- ¿Por qué tengo que arreglar algo que funcionaba perfecto?

- ¿Por qué algo que debería resolver un problema puntual se
  vuelve tan frágil y requiere intervenciones manuales?

- ¿Estoy obligado a reparar el sistema de *tests* y
  automatización por culpa de esto y aquello?


## Simplificando las cosas

Decidí hacer esto:

Voy a borrar todo lo que hice de automatización, voy a
generar los binarios de pilas desde mi computadora, correr
los *tests* de forma local y subir los binarios a mano.

Se que no es la mejor solución de todas, pero me gustaría
sentir autonomía para que mis herramientas hagan lo que yo
quiero, y no se rompan solas.

Pilas es muy particular, ya que solamente yo estoy dedicando
tiempo a desarrollarlo, le dedico poco tiempo y espero que
cada contribución llegue a los usuarios.

La filosofía de mantenerme actualizado con las dependencias
y pagar deuda técnica poco a poco no se ajusta a este
proyecto.

# Resultado

Ahora mis *scripts* son locales, más simples y fáciles de
mantener. Lo más automatizado que tengo es este
[makefile](https://github.com/pilas-engine/pilas-engine/blob/master/Makefile):

![](/images/2023/simplificando-a-la-fuerza/make.png)

y para cada cosa que tengo que hacer suelo dedicar un
comando de Make para simplificar una tarea.

Por ejemplo, para subir binarios ejecuto este comando:

![](/images/2023/simplificando-a-la-fuerza/binarios.png)

Claro, seguramente voy a tener que ajustar cosas en el
futuro, pero siento que este enfoque más artesanal y sólido
puede darme menos problemas en el futuro.

---
layout: post
title: La documentación no muerde
date: "2018-12-15 14:11:38"
description: "Una historia personal que me recuerda investigar, leer y comprender en lugar de explorar rápidamente una solución en stackoverflow."
cover: "/images/2018/12/portada.jpg"
---

Sé que suena un poco fuerte, pero no te ofendas... esta leyenda es para mí, y la escribo acá como una forma de no olvidarme lo que pasó hoy y seguir aprendiendo.

Si sos como yo, y programas hace algunos años, seguramente recurrís con urgencia a google o stack overflow cuando algo no sale bien, ya sea por un error imprevisto o un desafío que parece trivial, es fácil recurrir rápidamente a Internet como una herramienta auxiliar.

Pero hoy hice las cosas un poco diferente, leí la documentación, y el resultado de lo que tenía que hacer mejoró notablemente.

Te cuento con un ejemplo lo que pasó:

## Primer intento: cómo formatear números

Hoy me encontré en la necesidad de mostrar un número grande (float con valor 52000.32) dentro de una aplicación web. Pero quería que el número se vea de manera legible, separado por milésimas. Algo así:

52.000,32

Naturalmente esto no parece difícil, pero es una de esas "cosas" que no se hacer "de memoria", ni me parece muy importantes como para aprender a hacerlas... así que por impulso fui directo a stack overflow y encontré esto:

"How to print a number with commas as thousands separators in JavaScript"

![image-20181211172619832](/images/2018/12/image-20181211172619832.png)

y más abajo vi esto, aparentemente mejor por la cantidad de votos:

![image-20181211172703438](/images/2018/12/image-20181211172703438.png)

## Segundo intento: cómo formatear números

Incluso encontré en google rápidamente que alguien mencionó la existencia de una biblioteca javascript para resolver esto llamada numeral.js:

![image-20181211172850568](/images/2018/12/image-20181211172850568.png)

## mmm ... un momento ...

Si llegaste acá atentamente, y no hiciste alt+tab o multitasking frenéticamente como yo. Seguramente habrás notado algo.

Convertir un número a un formato legible con Javascript se vuelve un horror... o bien implica agregar una función rara de por ahí, o incluir una dependencia llamada numeral.js que seguro hace mil cosas que ni se necesitan (y va por la versión 2.0.6 !!).

En este punto casi dejo todo a un lado y me conformo con ver los números tal y como son... no me gustan ninguna de las cosas que intenté hasta ahora para mostrar los números formateados.

Sin embargo, hice una pausa, me preparé un café y recordé algo...

## Nacho, hay que aprender más de vos

Hace unas semanas nos reunimos a experimentar usando "Go" junto a unos amigos. Programar con otras personas en grupo deja algunas cosas curiosas. Por ejemplo, notamos que Nacho no se lanzaba directamente a escribir código y realizar pruebas de las cosas tan rápido; en lugar de eso: Nacho hacía una pausa, abría la documentación y leía, analizaba y trataba de llegar al fondo de las cosas.

Al poco tiempo de trabajar juntos, se notaba que nacho iba por buen camino. Ya que podía dar paso seguro sobre las cosas que iba haciendo y podía explicar sus pasos fácilmente.

Claramente Nacho hacía las cosas de una forma diferente a mí: mi forma de hacer las cosas daba muchos fallos y era desgastante, hasta frustrante en algunos casos... yo estaba mas preocupado por escribir código lo antes posible y "tener algo que funcione" en lugar de comprender y luego implementar.

## La solución: cómo formatear números

Así que recordando ese día, se me ocurrió cerrar stack overflow, google y simplemente leer la documentación de Javascript. ¡Fue lo mejor que hice esta tarde!

Los números en Javascript se representan con un tipo de objeto llamado Number, y tienen asociados una serie de funciones:

- https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number

y para mi sorpresa, leer la documentación fue mucho mas productivo que cualquier cosa... existe un método especialmente diseñado para el caso que yo quería resolver (toLocaleString)

![image-20181211174816305](/images/2018/12/image-20181211174816305.png)

## Conclusión

Creo que lo importante en este punto no es exactamente cómo convertir números, sino qué proceso o estrategia elijo a la hora de resolver un desafío.

Parece una tontería señalar esto, pero creo que no lo es: "la documentación no muerde", la documentación debería ser la fuente de información principal a la que deberíamos recurrir cada vez que algo no anda bien.

Y no solo eso, comprender no es lo mismo que explorar rápidamente. Lleva tiempo leer y comprender un manual, y está bien, se compensa rápidamente.

Y, nuevamente, esto es un recordatorio para mí... la documentación no muerde.

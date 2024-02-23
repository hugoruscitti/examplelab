---
layout: post
title: Fechas importantes y aniversarios
date: '2024-02-23 00:00:00'
description: |
  Armé un script para visualizar fechas importantes y
  recordar aniversarios.
cover: /images/2024/fechas-importantes-y-aniversarios/portada.jpg
---

Hay varios eventos que me gustaría recordar y celebrar, como
el cumpleaños de mis sobrinos, el día que nos conocimos con
mi novia o el día que adoptamos a nuestras mascotas.

También hay otras fechas que me gustaría tener presentes, no
como aniversarios, pero sí como fechas importantes para mí:
cómo el día que comencé a trabajar o hace cuánto tiempo
obtuve la licencia de conducir.

Así que me pareció una buena idea comenzar a registrar todos
esos eventos en la computadora y así tener una forma de
recordarlos y apreciar todo lo que estoy viviendo.

Comencé con una idea básica, quiero almacenar estas fechas
en un formato de texto, durable y simple:

```
Aniversarios:

2023-12-06: Adoptamos a las perritas.
2009-06-03: Cumpleaños de Mati.
2015-08-06: Cumpleaños de Agus.
[etc ...]

Otras fechas:

2023-07-21: Obtuve la licencia de manejo.
[etc ...]
```

Ahora, para que estas fechas sean fáciles de reconocer hice
un [script](https://github.com/hugoruscitti/dotfiles/blob/master/bin/fechas_relativas.py) que me genera una representación visual de la
fecha, cuántos meses transcurrieron desde el último
aniversario y algunas otras ayudas más:

![](/images/2024/fechas-importantes-y-aniversarios/captura-2024-02-23-jcyvt.png)

El
[script](https://github.com/hugoruscitti/dotfiles/blob/master/bin/fechas_relativas.py) se encarga de obtener la fecha de hoy y calcular
cuánto tiempo transcurrió de cada uno de esos eventos.
Además, cuándo hace el cálculo de fechas también agrega un
emoji si la fecha está cerca de cumplir otro año (o un
aniversario).

El formato lo diseñe pensando en un caso de uso muy
frecuente, quiero abrir este archivo con VIM y visualizar
rápidamente las fechas en pantalla.

Esta es una infografía del formato de archivo que diseñé:

![](/images/2024/fechas-importantes-y-aniversarios/captura-2024-02-23-l4l26.png)

Hay dos partes importantes en cada una de estas lineas. La
parte que está a la izquierda del token (`#`) es las que
puedo editar desde `vim`, mientras que la parte derecha del
token es la información que escribe automáticamente por el
[script](https://github.com/hugoruscitti/dotfiles/blob/master/bin/fechas_relativas.py).

## El script que genera la visualización

Para crear el
[script](https://github.com/hugoruscitti/dotfiles/blob/master/bin/fechas_relativas.py) comencé con casos de uso muy directos,
escribí las llamadas a las funciones y los resultados
esperados, al mejor estilo TDD.

Por ejemplo, sé que entre estas dos fechas: `2022-01-01` y
`2022-05-06` transcurrieron 4 meses y 5 días, así que armé
los tests antes de comenzar a programar:

```python
assert obtener_diferencia("2022-01-01", "2022-05-06") == (0, 4, 5)
```

Para implementar esta función separé la fecha en tres
partes, `año`, `mes` y `dia`, tanto de la fecha de hoy como
la fecha del evento, y luego hice una resta entre las dos.

![](/images/2024/fechas-importantes-y-aniversarios/image20240221104031.png)

Al hacer esta función me encontré con la necesidad de
conocer la cantidad de días que tiene un mes determinado, si
es bisiesto o no, y otras particularidades.

Me encantó programar esta parte del programa, logré
comprender exactamente qué estaba haciendo y no usé ninguna
biblioteca de fechas de python ni de terceros.

Luego hice algo similar con la función que dibuja la
representación visual de meses. Comencé por escribir los
tests, enumeré los casos más importantes y luego escribí la
implementación:

```python
assert graficar_barra((0, 4, 5)) == "■■■■□□□□□□□□"
assert graficar_barra((0, 0, 5)) == "□□□□□□□□□□□□"
assert graficar_barra((0, 9, 0)) == "■■■■■■■■■□□□"
```

Para escribir estos tests solo tuve que usar la palabra
reservada `assert` y comparar la llamada de la función con
el resultado esperado.

## Datos, cálculos y acciones

Al hacer el
[script](https://github.com/hugoruscitti/dotfiles/blob/master/bin/fechas_relativas.py) también tuve en cuenta la forma de
programar que sugiere Eric Normand en su libro ["Grokking
Simplicity"](https://www.manning.com/books/grokking-simplicity):

Busqué clasificar las funciones en dos grupos: `actions` y
`calculatios` (o `funciones puras`  y `funciones impuras`
respectivamente).

`calculations` son funciones que solamente actúan sobre los
parámetros de entrada, y siempre van a devolver el mismo
valor ante los mismos argumentos. Son funciones que no
tienen ningún efecto colateral, ni dependen del tiempo ni de
dónde se llamen. En cambio `actions` son las funciones que
toman algún dato externo o modifican estado externo (como
imprimir en pantalla, sobre-escribir archivos etc...)

Con esta separación en mente, busqué escribir la mayor parte
del código usando `calculations`, que son más fáciles de
diseñar, escribir y poner a pruebas. Luego, donde necesité
escribir `actions` busqué controlarlas y reducirlas al
mínimo, haciéndolas menos importantes y muy concretas.

Con respecto a los datos, me ayudó mucho tener claras las
estructuras de datos desde el principio, en lugar de diseñar
usando objetos diseñe las estructuras de datos muy simples y
fáciles de observar. Para diferencias de fechas usé tuplas
(de la forma `(años, meses, días)`) y para fechas usé
`strings` de la forma `YYYY-MM-DD`.

Por cierto, hace unos meses escribí sobe esta distinción de
`actions`, `calculations` y `data` en otro post del blog,
este es el link para referencias si te resulta útil:
https://www.examplelab.com.ar/posts/2021-03-03-replanteando-la-programacion-funcional/

## Integración con VIM

Una vez que finalicé el
[script](https://github.com/hugoruscitti/dotfiles/blob/master/bin/fechas_relativas.py), busqué integrarlo a VIM para
que me sirva como interfaz de usuario.

La integración fue muy sencilla, agregué estos dos eventos
dentro de la configuración de VIM:

```vim
au BufRead fechas.wiki silent exec "%!fechas_relativas.py %"
au BufWritePost fechas.wiki silent exec "%!fechas_relativas.py %"
```

La primer linea le indica a VIM que tiene que procesar el
archivo cuando se abre, mientras que la segunda hace lo
mismo cuando se guarda el archivo.

De esta forma, cada vez que miro el archivo desde VIM me
puedo asegurar que va a estar mostrando las fechas
correctamente, sin necesidad de ejecutar ningún comando por
mi cuenta.

## Cierre

Me siento muy conforme con el resultado de experimento que
inicié, no solo pude crear algo útil para mí, sino que
también pude poner en práctica ideas para escribir software
de forma más simple, como la distinción de `actions` y
`calculations`.


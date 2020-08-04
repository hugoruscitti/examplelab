---
layout: post
title: Creando intérpretes interactivos con python
date: '2010-07-22 15:00:00'
tags:
- interprete
description: En este artículo veremos algunas herramientas para que podamos crear nuestro propio intérprete de comandos....
cover: /images/2013/Oct/portada-interpretes.jpg

---

Python, al ser un lenguaje dinámico, facilita mucho la creación de intérpretes.

En este artículo veremos algunas herramientas para que podamos crear nuestro propio intérprete de comandos.
Algo básico con readline


`Readline` es una biblioteca muy popular en GNU/Linux, se puede integrar a casi cualquier programa y permite crear auto-completados de comandos, historiales y búsquedas.

Por ejemplo, el interprete de comandos Bash utiliza `readline` y por lo tanto se puede auto-completar comandos con TAB, recorrer el historial pulsado ARRIBA en el teclado y mas...

Para crear un programa interactivo de python usando `readline` se puede usar el módulo `readline`:


```
import readline

nombres = ['pepe', 'pedro']

def completer(text, state):
    options = [x for x in nombres if x.startswith(text)]

    try:
        return options[state]
    except IndexError:
        return None

readline.set_completer(completer)
readline.parse_and_bind("tab: complete")

while 1:
    print ""
    nombre = raw_input("Escriba un nombre: ")
    print "Ha ingresado el nombre:", nombre

    if nombre in nombres:
        print "\t(ya existia este nombre en la lista de autocompletado)."
    else:
        nombres.append(nombre)
        print "\t(agregandolo a la lista de autocompletado)."
```


## Autocompletado inteligente con rlcompleter

Ahora bien, con lo que hemos visto ya podemos crear auto-completado de palabras personalizados. Pero si lo que buscamos es auto-completar código python, necesitarías inspeccionar objetos, módulos o bibliotecas.

Un módulo conveniente para hacer esta tarea es `rlcompleter`, que se encarga de hacer todo este trabajo de sugerencias por nosotros.

Esto es interesante para hacer interpretes python personalizados, por ejemplo el siguiente intérprete se puede usar para hacer pruebas sobre dos conjuntos:

```
import rlcompleter
import readline
readline.parse_and_bind("tab: complete")

grupo_a = set([1, 2, 3])
grupo_b = set([3, 4, 5])

cmd = None

while cmd not in ['quit', 'exit']:
    cmd = raw_input('>> ')
    exec(cmd)
```

Inicie el script, escriba `grup` y luego TAB, en pantalla se tienen que mostrar las referencias que comienzan con `grup`. Luego, si escribe grupo_a. y luego TAB puede ver los atributos del objeto señalado por la referencia

Internamente, `rlcompleter` hace todo el trabajo de instronspección por nosotros.


## Atajos de teclado

Por último, ten en cuenta que `readline` viene con muchos atajos de teclado.

Tener en mente esto te permite usar mas eficientemente el módulo readline y cualquier aplicación que utilice la biblioteca, por ejemplo bash o ipython.



<table>
<thead>
<tr>
<th>Atajo</th>
<th>Acción</th>
</tr>
</thead>
<tbody>
<tr>
<td>CTRL+f</td>
<td>Mover el cursor un caracter a la derecha.</td>
</tr>
<tr>
<td>CTRL+b</td>
<td>Mover el cursor un caracter a la izquierda.</td>
</tr>
<tr>
<td>CTRL+a</td>
<td>Ir al principio de la linea.</td>
</tr>
<tr>
<td>CTRL+e</td>
<td>Ir al final de la linea.</td>
</tr>
<tr>
<td>CTRL+w</td>
<td>Borrar la última palabra que se escribió.</td>
</tr>
<tr>
<td>↑, ↓</td>
<td>Navegar por el historial de textos ingresados.</td>
</tr>
<tr>
<td>CTRL+r</td>
<td>Buscar en el historial de textos (hacia atrás).</td>
</tr>
<tr>
<td>CTRL-l</td>
<td>Limpiar la pantalla (sin borrar el texto actual).</td>
</tr>
<tr>
<td>TAB</td>
<td>Autocompletar</td>
</tr>
</tbody>
</table>

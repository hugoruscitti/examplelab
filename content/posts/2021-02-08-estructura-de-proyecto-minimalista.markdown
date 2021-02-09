---
layout: post
title: Una estructura de proyecto minimalista en TypeScript
date: '2021-02-08 00:00:00'
description: |
  Empezar a desarrollar un proyecto web se puede convertir
  en una tarea compleja, con dependencias y archivos
  de configuración. En este post intentaré mostrar
  una alternativa modesta.
cover: /images/2021/estructura-de-proyecto-minimalista/portada.jpg
---

Hace algunos meses me empecé a interesar en formas simples
en hacer proyectos en JavaScript, leí el libro [Modest JS Works](https://modestjs.works/book/part-1/intro/)
y también empecé a usar algunas ideas de [The VanillaJS Toolkit](https://vanillajstoolkit.com/).

Realmente extraño la sensación de hacer aplicaciones completas por mi mismo,
sin depender de cientos de megabytes en dependencias, frameworks
sofisticados y un ecosistema de herramientas que están cambiando
todo el tiempo.

# ¿Por qué?

Hace unos años, podías escribir un sistema completo por tu propia cuenta,
necesitabas Apache, PHP, un editor de textos y ganas de programar. 

Incluso si recién estabas aprendiendo a programar, las herramientas hacían
muy poquito por vos, pero aún así podías concentrarte en tu aplicación y no tanto
por todo lo demás.

Hoy la historia es un poco diferente, hubo un cambio de cultura muy grande
entre los desarrolladores web; no se muy bien por qué, pero ahora parece
que la forma más aceptada de iniciar un proyecto web es elegir un framework, instalar
dependencias con npm, configurar tu IDE y algunas cosas más. 

Pienso que la forma en la que trabajan las empresas grandes y los equipos altamente
capacitados lograron influenciar a todo el mundo. Como si sus ideas se hubieran vuelto
el "nuevo estándar" a la hora de hacer software.

# Un enfoque simple

Estrictamente hablando, al navegador no le importa cómo vas a construir tu aplicación
web, el navegador interpreta HTML, CSS y JavaScript, independientemente de cómo
lo escribas.

A mí me gusta la idea de no tener demasiadas dependencias, sobre
todo si soy el único desarrollador y cada actualización o problema de configuración
lo tengo que arreglar por mí mismo.

De hecho, me parece razonable que mi equipo tenga ciertas herramientas
instaladas de forma global: typescript, python, make, vim, uglify-js etc... asumir
que un proyecto tiene que poder "auto-instalarse" en cualquier equipo usando `npm install`
desde cero no me gusta sinceramente.

Entonces, un proyecto se puede iniciar con 3 archivos, "index.html", "app.js" y "app.css":

```
→ ls 
app.css     app.js      index.html
```

Y conforme necesite más, puedo ser consciente de qué piezas me conviene
agregar y si realmente me benefician a no.

# Un webserver en modo desarrollo

Una de las piezas que me gusta tener a la hora de programar es un servidor
web que actualice el navegador cada vez que realizo cambios en los archivos
del proyecto.

Para eso utilizo [este comando](https://www.npmjs.com/package/live-server) que
instalé de forma global en mi sistema:

```
live-server
```

Esto es un "chiche" en realidad, porque solamente me ahorra cambiar
de ventana y pulsar `cmd+r` para recargar la página. 

Sin embargo para mí esto añade algo de diversión y comodidad, porque puedo
permanecer en el editor y asegurarme que el navegador siempre me muestra
la versión más reciente de la aplicación.

![](/images/2021/estructura-de-proyecto-minimalista/split.png)

# TypeScript

Obviamente se puede escribir el proyecto directamente en JavaScript
para que lo interprete el navegador, sería más sencillo hacerlo así. Sin
embargo aquí es donde se puede dar un pequeño paso hacia la
complejidad sin comprometer demasiadas cosas.

TypeScript es un lenguaje que añade tipos de datos a JavaScript y
una serie de herramientas para análisis de código estático que
ayudan un montón.

Además, usando TypeScript tenemos la facilidad de poder separar
el proyecto en diferentes archivos y tener un solo comando
para empaquetar todo y llevarlo al navegador.

Por ejemplo, los archivos de código los suelo guardar en un directorio
como `src` así:

```
→ ls src/
app.ts  tsconfig.json  utils.ts
```

El archivo `tsconfig.json` simplemente describe que queremos convertir
todos esos archivos `.ts` en un único archivo `app`:

```
{
  "compilerOptions": {
    "outFile": "../dist/app.js",
    "sourceMap": true,
    "target": "es6",
    "module": "amd",
    "paths": {
      "~*": ["./*"]
    }
  },
  "include": ["**/*.ts"]
}
```

Luego, para compilar todo, uso este comando:

```
tsc -b src
```

o si quiero compilar automáticamente ante un cambio
en alguno de los archivos de código fuente:

```
tsc -b src -w
```

ok, igual... se que suena complejo, mi idea de minimalismo en un proyecto
no consiste en deshacerse de la estructura y rechazar todas las herramientas. 

Mi idea de un entorno minimalista es "volar liviano", quitando las cosas
que no aportan tanto valor y preservar aquellas que son realmente valiosas, esenciales
para trabajar en la forma que me gusta; y eso es muy subjetivo.

Para mí TypeScript aporta valor, el suficiente valor para tener instalado el comando
`tsc` de forma global (`npm install -g typescript`) en mi equipo, y usarlo como
una herramienta más dentro de este proyecto y otros.

# Autocompletado con vim

Otra ventaja de usar TypeScript es que el propio editor de textos
puede autocompletar y detectar inconsistencias en nuestro código.

No hace falta configurar algo adicional dentro del proyecto, tener
dependencias locales en un archivo `package.json` o configurar un entorno
virtual:

![](/images/2021/estructura-de-proyecto-minimalista/autocompletado.png)

Para tener este autocompletado en vim estoy utilizando una extensión
llamada [ale](https://github.com/dense-analysis/ale), pero
creo que también hay otras alternativas.


# ¡Pero necesito componentes web!

Si hay algo que adopté de usar frameworks es el concepto de componentes
web. Creo que poder construir aplicaciones pensando en pequeños componentes que
se pueden combinar entre sí es una muy buena idea.

Por suerte hoy se pueden utilizar 
[componentes web](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_custom_elements) de 
forma nativa en cualquiera de los navegadores web modernos, no hace falta
usar una herramienta adicional. Incluso existen 
[pollyfills](https://www.webcomponents.org/polyfills/) por si quieres dar
soporte a navegadores antiguos.

El único desafío que encontré en usar [web components](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_custom_elements) 
es que necesitamos escribir más código, hay menos magia, pero 
aún así creo que es fácilmente abordable.


---
layout: post
title: Simplificando imports en svelte
date: '2022-02-06 00:00:00'
description: |
  Cómo mejorar la importación de módulos en un proyecto svelte.
cover: /images/2022/simplificando-imports-en-svelte/portada.jpg
---

Hace unas semanas comencé a migrar un proyecto personal
a [sveltekit](https://kit.svelte.dev/), en parte porque quiero
retomar ese proyecto y en parte porque quiero aprender una herramienta
nueva como [svelte](https://svelte.dev/).

Sin embargo a la hora de programar me encontraba escribiendo
código como este:

```javascript

import BotonCrearTransaccion from '../../../../components/botones/crear-transaccion.svelte';
import BotonIniciarPresupuesto from '../../../../components/botones/crear-presupuesto.svelte';
import store from "../../../../stores";

```

Observa todos esos `../` que aparecen delante de las rutas.

Estas rutas relativas no solo hacen que el código se vea muy feo, sino
que también me impiden mover archivos dentro del proyecto, por ejemplo
si quiero poner un componente dentro de una carpeta nueva o algo así. Cada
archivo que muevo puede "romper" esas rutas relativas.

Así que me puse a investigar este problema y encontré que existe una
solución, incluso tiene un nombre: *module import aliases*.


La idea es bastante simple, en lugar de especificar las rutas
usando `imports` relativos, podemos especificarlos de esta forma:

```javascript
import BotonCrearTransaccion from '@components/botones/crear-transaccion.svelte';
```

Donde ese símbolo `@components` es algo que podemos configurar por
nuestra cuenta. Podría ser `@components`, `@c`, `@src`, lo que nos
resulte más conveniente.

Lo único que hay que hacer para que esto funcione es editar el
archivo `svelte.config.js` y definir estas rutas una sola vez:


```js
# [...]
import { resolve } from 'path';

const config = {
  # [...]

  kit: {
    target: '#svelte',
    vite: {
      resolve: {
        alias: {
          '@components': resolve('./src/components')
        }
      }
    }
  }
};
```

Y listo.

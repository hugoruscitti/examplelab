---
layout: post
title: Un ajuste mínimo al Dock
date: '2021-08-28 00:00:00'
description: |
  ¿Te molestan los íconos que saltan en el Dock de Osx?, ¿no?, ¡a mí sí!
cover: /images/2021/un-ajuste-minimo-al-dock/portada.jpg
tags:
- reflexión
---

Hace tiempo que no escribo en el blog, así que se me
ocurrió que una forma de retomar el ritmo es explicar
este pequeño truco.

Resulta que Osx tiene un Dock en donde las aplicaciones
"saltan" si hay un mensaje importante para atender. Por
ejemplo si inicias la descarga de un archivo y el navegador
quiere saber dónde guardar el archivo el navegador va a
interrumpirte.

A mí no me gustan las interrupciones, así que busqué por
todos lados como desactivar esos íconos saltarines.

Por suerte solo hay que ejecutar este comando:

```
defaults write com.apple.dock no-bouncing -bool TRUE
killall Dock
```

Y listo, con eso los íconos ya no se ponen a "saltar" buscando
llamar tu atención.

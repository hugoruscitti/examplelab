---
layout: post
title: Emails con Django en modo desarrollo
date: '2021-06-03 00:00:00'
description: |
  Cómo configurar un servidor de emails para hacer pruebas locales mientras se programa una aplicación web con Django.
cover: /images/2021/emails-con-django-en-modo-desarrollo/portada.jpg
---

> Nota: Este artículo lo escribí originalmente en Abril del 2020 y se publicó en otra web.

Es un práctica común configurar e implementar envío de emails desde un sistema
web. Casi todas las empresas llegan a tener la necesidad de informar a sus
usuarios sobre eventos del sistema como las notificaciones o recuperación de
contraseñas.

En este artículo queremos contarte la forma que encontramos en enjambre-bit
para implementar esas tareas de forma segura y sencilla.

# ¿Por qué configurar pensando en modo desarrollo?

Realizar un circuito que involucre enviar emails en un sistema web parece muy
sencillo al principio. Enviar emails desde un framework como Django es la parte
más sencilla de todas.

Sin embargo, integrar emails a una aplicación web no consiste solamente en
enviar un email.

Mientras estamos programando necesitamos realizar varias pruebas que pueden ser
incómodas y repetitivas.

Por ejemplo, imaginemos un requerimiento común en varias aplicaciones web:
"crear un sistema para registrar usuarios nuevos":

Como mínimo necesitamos que una persona pueda cargar su dirección de email en
un formulario para iniciar el proceso de creación de cuenta, y luego deberíamos
entrar en este circuito:

- Necesitamos emitir el mail a una dirección de correo real.
- Deberíamos validar que la persona logra recibir el email con una URL para
iniciar el proceso de creación de cuenta.
- Al ingresar en la URL, tiene que poder cargar su contraseña inicial y
confirmar.
- El sistema tiene que enviar un segundo email de bienvenida informando que la
cuenta se creó correctamente.  Y si bien con esto alcanzaría para decir
"tenemos implementado el circuito de creación de cuentas en modo desarrollo",
el paso siguiente es llevar eso a un entorno de producción con la menor
cantidad de cambios posibles.

Además, ¿qué sucedería si queremos cambiar algo de este circuito en el futuro?,
¿cómo podemos asegurar que no vamos a enviar correos a usuarios reales
mientras hacemos pruebas?


# ¿Entonces?, ¿qué enfoque podemos utilizar?

Primero, veamos el desafío de probar los circuitos de envío de email de forma
local:

En lugar de configurar un servidor de SMTP real, se puede descargar una
aplicación llamada "maildev" para iniciar un servidor de mails local:

- https://danfarrelly.nyc/MailDev/

Lo interesante de maildev es que se puede instalar muy fácilmente con npm y se
puede ejecutar para lanzar un servidor de mails local con una interfaz web que
simula un cliente de webmail.

Para instalarlo, se puede ejecutar:

```
npm install -g maildev
```

y para ejecutarlo maildev:

![](/images/2021/emails-con-django-en-modo-desarrollo/ima.png)

Una vez que se ejecuta, si abrís un navegador con esa dirección 1080 se puede
ver cómo sería la bandeja de entrada de quién recibirá nuestros emails en modo
desarrollo:

![](/images/2021/emails-con-django-en-modo-desarrollo/mail.png)

Ahora bien, desde Django, para emitir los emails a este servidor de prueba
simplemente hay que configurar la variable EMAIL_PORT en el archivo
settings.py:

```
EMAIL_PORT = 1025
EMAIL_HOST = localhost
```

Y por último, cada vez que emitamos un email, aparecerá en nuestro maildev
directamente:

![](/images/2021/emails-con-django-en-modo-desarrollo/a.png)

¡ Yep !

![](/images/2021/emails-con-django-en-modo-desarrollo/jerris.png)

# Separando entornos de desarrollo y producción

El siguiente paso para tener una buena implementación de este flujo es hacer
que el servicio de emails funcione de manera diferente en producción y
desarrollo.

Siguiendo las recomendaciones de [12 factor](https://12factor.net/es/), si
colocamos la configuración de nuestros entornos de ejecución en variables de
entorno, podemos hacer que la aplicación automáticamente use un SMTP local si
está en modo desarrollo o un servidor real si está en producción.

Por ejemplo, si tenemos un archivo de configuración (`backend/settings.py`)
así:

```
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', '')
```

Es fácil hacer que en nuestro entorno local se utilice el servidor STMP de
maildev, simplemente tenemos que colocar en el archivo `.env` (que lee pipenv)
el puerto de pruebas de SMTP:

```
DATABASE_URL="postgres://post..."
DISABLE_COLLECTSTATIC=1
EMAIL_PORT=1025
```

y en producción, si usamos dokku podemos simplemente especificar un SMTP real
usando `dokku config`:

```
> ssh dokku@enjam... config app-backend | grep EMAIL
EMAIL_HOST_PASSWORD:      f6TYtNv***
EMAIL_PORT:               587
EMAIL_HOST_USER:          hu****
EMAIL_USE_TLS:            True
EMAIL_HOST:               smtp.sendgrid.net
```

# Alternativas

Maildev nos dá buenos resultados, sin embargo, si en tu caso no te resulta
útil, hay alternativas como mailtrap (que funciona como servicio), MailSlurper
o incluso el minimalista dsmtpd.

Y si solamente quieres ver un log para certificar que el correo sale
correctamente, también podrías ejecutar esto comando sin necesidad de instalar
nada:

```
python -m smtpd -n -c DebuggingServer localhost:1025
```

Otra alternativa, muy similar a la anterior. Es especificar la variable
`"EMAIL_BACKEND"` en la configuración de Django:

```
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

Esta configuración hace que Django emita por consola el contenido de los emails
en lugar de enviarlos al servidor smtp.

¡Gracias Agus por comentarnos esta última alternativa!

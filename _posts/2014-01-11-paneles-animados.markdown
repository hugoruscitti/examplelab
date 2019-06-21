---
layout: post
title: Paneles animados
date: '2014-01-11 17:15:41'
---

Hace unos dias, implementé animaciones en los paneles de **huayra-stopmotion**. Al principio opté por usar la forma mas rudimentaria de mostrar y ocultar paneles, pero luego descubrí como implementarlo usando css3 y un poquito de javascript:

![](/images/2014/Jan/stopmotion.gif)


En este post me gustaría contarte cómo lo implementé, ya que puede resultarte útil a la hora de hacer algo similar.

Acá está la versión completa en jsfiddle:


<iframe width="100%" height="300" src="http://jsfiddle.net/hugoruscitti/TVBHC/embedded/result,js,html,css" allowfullscreen="allowfullscreen" frameborder="0"></iframe>

## El layout

Para mantener el maquetado lo mas sencillo posible, vamos a crear tres contenedores:

- Un contenedor superior para el botón "alternar panel".
- Un panel principal.
- Un panel alternativo que se pueda ocultar.

Así queda:

![](/images/2014/Jan/estado_1.png)

Luego, si el usuario pulsa el botón "alternar panel", se debería ocultar el panel derecho:

![](/images/2014/Jan/estado_2.png)

Básicamente, armé los contenedores como bloques ``div``:

```prettyprint lang-html
<body>
		
		<div id='botones'>
			<a href='' id='alternar' class='boton'>alternar panel</a>
		</div>
		
		<div id='contenedor' class='contenedor'>Panel principal</div>
		<div id='panel' class='panel'>Panel Alternativo</div>		
</body>
```
	
y en la hoja de estilos asigné posicionamiento absoluto y tamaño fijo a la clase ``panel``:

```prettyprint lang-css
	<style>
    
	.panel {
    	border: 1px solid #ff175e;
    	position: absolute;
    	top: 30px;
    	bottom: 0;
    	right: 0;
    	width: 300px;
    	text-align: center;
	}
			
	.contenedor {
		margin-top: 30px;
		text-align: center;
		margin-right: 300px;
		border: 1px solid gray;
	}
    
	</style>
```

Por cierto, también me aseguré de hacer que el contenedor principal tenga un margen derecho para que no se solape con el panel lateral.

## Controles de visibilidad

Para ocultar y mostrar paneles podemos simplemente usar css.

Podemos crear una clase para representar el panel invisible (desplazado hacia la izquierda) y aplicarselo a un elemento del dom usando javascript.

Por ejemplo, para el panel lateral, hay dos clases importantes:

```prettyprint lang-css
.panel {
    width: 300px;
}

.panel-invisible {
	right: -300px;
}
```

Es decir, ocultar el panel es simplemente moverlo a la izquierda, tantos pixeles como tenga de ancho, así queda fuera de la pantalla completamente.

Luego, para mostrar y ocultar dinámicamente, agregué un botón que asigna o quita la clase "panel-invisible":

```prettyprint lang-javascript
var botonAlternar = document.getElementById('alternar');

botonAlternar.onclick = function() {
    var panel = document.getElementById('panel');
    panel.classList.toggle('panel-invisible');
    return false;
}
```

## Animaciones al ocultar y mostrar

Hasta ahora el panel debería ocultarse o mostrarse inmediatamente, sin animación alguna.

Este comportamiento produce un aspecto un poco extraño, no se puede percibir que el panel se oculta por la parte derecha de la pantalla, desaparece de manera abrupta.

Acá es donde podemos aplicar una transición css3:

![](/images/2014/Jan/interpolaciones.png)

## ¿De donde viene esta idea?

En realidad, de dos lados:

Por un lado, cuando empecé a probar **xcode** noté que los paneles se podían mostrar y ocultar con un selector muy simple:

![](/images/2014/Jan/botones.png)

Básicamente tienes estos tres botones para alternar los paneles auxiliares. Acá los podés ver en acción:

![](/images/2014/Jan/xcode.gif)

El otro lugar que me invitó a pensar un poco sobre animaciones en interfaces de usuario, es este video video:

<iframe width="560" height="315" src="//www.youtube.com/embed/TMe0WnkF1Lc" frameborder="0" allowfullscreen></iframe>

Creo que el video es impresionante, muy recomendable.

## Links recomendados

- [Mozilla: Using CSS transitions](https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Using_CSS_transitions)
- [How to create a web app that looks like a iOS 7 native app - Part 2](http://mir.aculo.us/2013/10/10/how-to-create-a-web-app-that-looks-like-a-ios-7-native-app-part-2-behavior/)

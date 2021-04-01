Todo está bien con JavaScript
=============================

- Artículo extraído desde:
  - [https://macwright.com/2016/10/04/everything-is-fine-with-javascript.html](https://macwright.com/2016/10/04/everything-is-fine-with-javascript.html)
- Traducción por Hugo Ruscitti

![](/images/link-files/everything-is-fine-with-javascript-1.jpg)

> Este es el único diario dispuesto a decir la verdad: todo está bien.

<!--There’s a sort of blog post you’ve probably read - a sarcastic stab at-->
<!--JavaScript and `npm` and frameworks. There are too many, it’ll say, and-->
<!--it’s confusing, and how did we make such complicated things? It’ll grab-->
<!--names from the ecosystem and present them as equal choices in a comic-->
<!--attempt to construct decision paralysis. Everything moves too fast, and-->
<!--there is too much of it.-->

Hay una serie de blog posts que seguramente has leído - una puñalada sarcástica
sobre JavaScript, `npm` y frameworks. Estos artículos mencionan que hay demasiadas
opciones, que es confuso, y sobre lo complicadas que parecen las cosas. También
toman montones de nombres del ecosistema y los presentan como opciones equivalentes
en un intento cómico por construir un escenario de parálisis de decisión. Todo se
mueve muy rápido y hay demasiado de todo.

<!--I think it’s a decent time to review some principles-->

Pienso que es tiempo de revisar algunos principios.

La obsesión con las cosas nuevas es un problema personal y no tecnológico
-------------------------------------------------------------------------

<!--I occasionally hang out on guitar forums. They have a name for this-->
<!--thing: **Gear Acquisition Syndrome**, or GAS. It is what it sounds like-->
<!--- when you’re more concerned with getting an OCD Fuzz pedal to round out-->
<!--your rig than you are with learning how to play the instrument.-->

Ocasionalmente paso el rato en foros sobre guitarras. Ahí, tienen nombre
para esto: **Síndrome de la adquisición de pedal**, o simplemente *GAS*. Y es
como suena, es cuando estás más preocupado por conseguir ese pedal Fuzz OCD para
manipular tus sonidos en lugar de aprender a tocar el instrumento.


<!--GAS with guitars works the same way as with programming: you start-->
<!--asking whether you’re using the *best possible* distortion pedal, start-->
<!--your research, and a few weeks later you own $2,000 worth of distortion-->
<!--pedals.-->

Esto que sucede con las guitarras funciona de la misma manera con la programación: comienzas
preguntándote si estás usando el *mejor pedal de distorsión*, comienzas a investigar, y
unas semanas después tienes un gasto de $2.000 en pedales de distorsión.

<!--Coding is a craft, for which you need tools. Some of them are shiny,-->
<!--some are new, some are old. They all basically work. Change your tools-->
<!--if they aren’t working for you, and otherwise don’t. Heck, for many-->
<!--startups and almost all early-stage startups, [the choice of technology-->
<!--stack really doesn’t-->
<!--matter](https://www.codingvc.com/why-startup-technical-diligence-is-a-waste-of-time/).-->

Programar es un oficio, para los cuales necesitas herramientas. Algunas de
esas herramientas son relucientes, otras nuevas y algunas viejas. Todas básicamente
funcionan. Solo cambia tus herramientas cuando dejan de funcionarte, si no no las
cambies. Demonios, para muchas startups y casi todas las empresas que recién
comienzan [la decisión del stack de tecnología ni siquiera importa](https://www.codingvc.com/why-startup-technical-diligence-is-a-waste-of-time/)

Tienes que usar diferentes herramientas para diferentes problemas
-----------------------------------------------------------------

<!--Creating a data visualization? Probably use d3. An application? React-->
<!--and Redux. A library? You might not need any framework.-->

¿Estás creando una visualización de datos?, probablemente puedas usar
d3. ¿Haces una aplicación?, react y redux. ¿Haces una biblioteca?, tal vez
no necesites ningún framework.

<!--This is pinned on the JavaScript ecosystem, somehow. If you look at the-->
<!--context, though, it’s what you have to do when you create literally-->
<!--anything. If you’re a Python developer, do you use Twisted or asyncio?-->
<!--If you’re an architect, do you use wood or brick? Do you use pen or-->
<!--pencil?-->

De alguna forma, esto está anclado al ecosistema de JavaScript. Si miras
a través del contexto, esto es algo que tienes que afrontar para crear
casi cualquier cosa. Si eres un desarrollador Python, ¿vas a usar Twisted
o asyncio?. Si eres un arquitecto, ¿usarás madera o ladrillo?, ¿vas a elegir
una lapicera o un lápiz?.

<!--Sometimes materials are best-in-class for what they do: now that there’s-->
<!--[lodash](https://lodash.com/), there are relatively few reasons to use-->
<!--[underscore](https://underscorejs.org/). Other times they’re still-->
<!--duking it out to see what’s best - browserify or webpack, for example,-->
<!--fix the same problem. But a lot of the time they’re clearly for-->
<!--different purposes: I, for instance, use React when writing a large-->
<!--application like Mapbox Studio, but don’t use a framework writing-->
<!--libraries that need to be small.-->

Algunos materiales son mejores que otros en ciertas áreas: ahora
que existe [lodash](https://lodash.com/) hay muy pocas razones
para usar [underscore](https://underscorejs.org/). Otras veces hay
que sumergirse para ver cuál es la mejor. Webpack o browserify es un
ejemplo de dos herramientas que intentan solucionar el mismo problema. Pero
muchas veces las herramientas están claramente resolviendo diferentes
propósitos: Yo, por ejemplo, uso React cuando escribo una aplicación
grande como Mapbox Studio, sin embargo no uso ningún framework cuando
escribo bibliotecas que necesito que sean pequeñas.

<!--As you learn and grow, you’ll acquire a go-to list of technology for-->
<!--each task. It isn’t the same as an exhaustive list: at most you might-->
<!--know 5 systems thoroughly. You mainly become capable by mastering these-->
<!--systems, not by tinkering with every alternative.-->

A medida que aprendes, vas adquiriendo una lista de tecnologías para resolver
cada tarea. Esta no es una lista exhaustiva de herramientas, como mucho puede
que conozcas 5 sistemas por completo. Posiblemente te vuelvas productivo
conociendo estos sistemas, no por juguetear con cada alternativa.

Si alguien es más apasionado que vos sobre decisiones tecnológias, está equivocado y deberías ignorarlo
-------------------------------------------------------------------------------------------------------

<!--If you read the snark, it sounds like you’re required to switch-->
<!--frameworks as soon as a new one accrues more stars on GitHub. Or that-->
<!--you *must* use functional programming. This may be the case in San-->
<!--Francisco - I don’t live there - but in the rest of the world, that’s-->
<!--nonsense. There are successful companies using every stack, from PHP to-->
<!--Haskell.-->

Si lees entre líneas, suena como si tuvieras que cambiar de framework
cada vez que surge una nueva herramienta que consigue más estrellas
en GitHub. O cambiar porque ahora muchos dicen que *tienes* que usar programación
funcional. Tal vez ese sea el caso en San Francisco, pero yo no vivo ahí, y
sé que en el resto del mundo es un sin-sentido cambiar de herramientas así. 
Además, hay modelos de empresas exitosas en cada stack, desde PHP hasta
Haskell.

------------------------------------------------------------------------

<!--So enjoy the rants, if you do, but when you read [How it feels to learn-->
<!--JavaScript in-->
<!--2016](https://hackernoon.com/how-it-feels-to-learn-javascript-in-2016-d3a717dd577f#.ima7p0eob),-->
<!--ask yourself: is the problem with the technology, or is it the unnamed-->
<!--antagonist with that judgmental snark? Or is it that the conversation is-->
<!--never driven by a problem that needs to be solved, but instead organized-->
<!--as a grand tour of all possible tools?-->

Así que disfruta leyendo cómo las personas despotrican contra todas las opciones
que existen, pero cuando leas 
[Cómo se siente aprender JavaScript en 2016](https://hackernoon.com/how-it-feels-to-learn-javascript-in-2016-d3a717dd577f#.ima7p0eob)
pregúntate a vos mismo: ¿este es un problema de la tecnología?, ¿es acaso
el hecho de que existen tantas opciones? ¿o en realidad el problema es que este
tipo de miradas nunca está dirigida por un problema concreto a resolver?

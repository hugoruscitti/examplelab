La complejidad es el enemigo
============================

- Artículo extraído desde: [https://neugierig.org/software/blog/2011/04/complexity.html](https://neugierig.org/software/blog/2011/04/complexity.html)
- Traducción por Hugo Ruscitti

23 de Abril de 20211

<!--
I'm almost through my seventh year working at Google(!). I have learned
many things there, more than I could ever write down. I thought I would
at least share with you something that's only come to me with more
experience.
-->

Estoy cerca de cumplir 7 años trabajando en Google. Aprendí muchas cosas aquí,
muchas más de las que podría escribir. Y pensé que podría compartir con vos algo
que solo vino a mí a través de la experiencia.

<!--
Complexity is the death of software. It's hard to quantify the cost of,
and it tends to creep in slowly, so it's a slow boil of getting worse
that's hard to see until it's too late. On the other side, frequently
it's easy to see a benefit of increasing complexity: a new layer of
indirection allows new feature X, or splitting a process that ran on one
machine into two allows you to surmount your current scaling hurdle. But
now you must keep another layer of indirection in your head, or
implement an RPC layer and manage two machines.
-->

La complejidad es mortal para el software. Es difícil medir su costo y tiende a
introducirse muy lentamente, así que crece volviéndose peor al punto que es
difícil verlo hasta que es muy tarde. Por otro lado, es fácil ver los beneficios
de incrementar la complejidad: Una nueva capa intermedia permite la
característica X, o dividir un proceso que corría en una computadora para que se
ejecute en dos te permitiría superar el obstáculo de escalabilidad. Pero ahora
deberías mantener otra capa de indirección en tu cabeza o implementar un nuevo
mecanismo de comunicación entre dos computadoras.



<!--
The above is hopefully just as obvious to a new programmer as it is to a
veteran. What I think I've learned through my few years in the industry
is a better understanding of how the balance works out; when complexity
is warranted and when it should be rejected. I frequently think back to
a friend's comment on the [Go compiler](http://golang.org/) written by
[Ken Thompson](http://en.wikipedia.org/wiki/Ken_Thompson): it's fast
because it just doesn't do much, the code is very straightforward.
-->

Esto que mencioné es evidente tanto para los nuevos programadores como
para los veteranos. Lo que logré durante mis años en la industria es un
mejor entendimiento sobre cómo balancear estas cosas. Cuándo se justifica la
complejidad y cuando no. Recuerdo con frecuencia un comentario de un amigo
sobre el [compilador de Go](http://golang.org/) creado por [Ken Thompson](http://en.wikipedia.org/wiki/Ken_Thompson):
este compilador es rápido porque no hace demasiado, el código es muy simple.

<!--
It turns out that, much like it's easier to write a long blog post than
it is to make the same point succinctly, it's difficult to write
software that is straightforward. .
-->

Resulta que, al igual es que más fácil escribir un artículo largo que escribir
uno breve que señale lo mismo de manera concisa, es difícil escribir software que
sea sencillo y breve. 

<!-- This is easiest to see in programming
langauge design; new languages by novices tend to have lots of features,
while few have the crisp clarity of C. -->

Esto se puede ver con facilidad en el diseño de lenguajes de programación,
los lenguajes nuevos suelen tener un montón de características, mientras muy
pocos logran tener la simpleza y claridad de C.

<!-- In today's programs it's
frequently related to how many objects are involved; in distributed
systems it's about how many moving parts there are.
-->

En los programas de hoy en día, se suele pensar más en la cantidad de objetos
que están involucrados que en otra cosa. En los sistemas distribuidos pasa lo
mismo, solo que se piensa en cuantas piezas móviles hay.


<!--
Another word for this problem is cleverness: to quote another one of the
C hackers, "Debugging is twice as hard as writing the code in the first
place. Therefore, if you write the code as cleverly as possible, you
are, by definition, not smart enough to debug it."
-->

Otra palabra para este problema es "inteligencia". Esto se decía otro de los hackers
de C: "Depurar un programa es el doble de difícil que escribir el código en
primer lugar. Después de todo, si escribes el código lo más "inteligente" que
puedas, estás, por definición, condenándote a no poder depurar ese programa, ya
que no serás doblemente inteligente al momento de depurarlo."



<!--
What helps? I wonder if it maybe just comes down to experience — getting
bitten by one too many projects where someone thought metaprogramming
was cool.-->

¿Qué ayuda?, me pregunto si esto se reduce solamente a la experiencia: haber
sido mordido por tantos proyectos donde alguien pensó que la meta-programación
era lo mejor y cosas similares.



<!--

But I've found having specific design goals to evaluate new
code by can help. It's easier to reject new code if you can say "this
does not help solve the initial goals of the project". Within Google the
template document for describing the design of a new project has a
section right at the top to list *non-goals*: reasonable extensions of
the project that you intend to reject.
-->

Encontré que tener objetivos específicos para evaluar el código nuevo es de
mucha ayuda. Es más fácil rechazar código nuevo si puedes decir algo cómo "Esto
no ayuda a resolver nuestro objetivo inicial del proyecto". 

Dentro de Google
usamos una plantilla para describir el diseño de los proyectos nuevos, en esa
plantilla tenemos una sección llamada "no-objetivos", donde se enumeran
extensiones o mejoras razonables al proyecto que se intentarán evitar.



<!--
Ironically, I've found that using *weaker* tools can help with
complexity. It's hard to write a complicated C program because it can't
do very much. C programs tend to use lots of arrays because that's all
you get, but it turns out that arrays are great — compact memory
representation, O(1) access, good data locality. I'd never advocate
intentionally using a weak tool, though. Instead, my lesson has been:
write Python code like it was C.
-->

Irónicamente, encontré que usar las herramientas *menos sofisticadas* pueden
ayudar con la complejidad. Es difícil escribir un programa complicado en C
porque no puede hacer demasiado. Los programas en C suelen tener un montón de
`arrays` porque es todo lo que tienes, y eso está bíen, porque los datos ocupan
poco lugar, los accesos a los elementos son directos, la información está
alocada en la misma página de memoria, etc. Sin embargo, nunca recomendaría usar una
herramienta rudimentaria porque sí, en lugar de eso, mi lección ha sido:
"Escribe código python como si fuera C."



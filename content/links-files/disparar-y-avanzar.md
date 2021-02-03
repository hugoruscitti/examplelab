Disparar y avanzar
==================

### From The Joel on Software Translation Project

Artículo original:
<a href="https://web.archive.org/web/20160629045135/http://www.joelonsoftware.com/articles/fog0000000339.html" class="external text">Fire And Motion</a>

Hay veces en las que no me sale nada.

Fijo. Llego a la oficina, doy un par de vueltas, veo si hay correo cada
diez segundos, navego por la red y tal vez haga algunas tareas tontas
como pagar la factura de la American Express. Pero lo de volver a
escribir código con fluidez no ocurre.

Estas lagunas de improductividad por lo general duran uno o dos días,
pero ha habido veces en mi carrera como desarrollador que me ha pasado
semanas enteras sin ser capaz de hacer nada. Como se suele decir, no
estás inspirado. No estás en lo que estás. No estás en ningún sitio.

Todos tenemos cambios de estado de ánimo. Para algunos, son suaves, pero
en otras personas pueden ser más pronunciados, incluso patológicos. Y
los periodos improductivos parecen estar relacionados con los estados de
ánimo más abatidos.

Esto me recuerda a los investigadores que afirman que, básicamente, la
gente no puede controlar lo que come, de manera que cualquier intento de
hacer una dieta está condenado a ser efímero y siempre terminan
rebotando hasta volver a su peso natural. Tal vez no puedo, como
desarrollador de software, controlar cuándo soy productivo: simplemente
he de asumir las épocas espesas con las épocas de rápido avance y
esperar que, en término medio, pueda escribir suficientes líneas de
código como para hacer que quieran contar con mis servicios.

Lo que me inquieta es que desde mi primer trabajo me he dado cuenta de
que, como desarrollador, en término medio sólo puedo escribir código
productivamente durante dos o tres horas al día. Cuando tuve una beca de
verano en Microsoft, un compañero becario me dijo que en realidad sólo
iba a trabajar de doce a cinco. Cinco horas (menos el almuerzo) y aún
así su equipo lo veneraba porque aún se las apañaba para hacer mucho más
que la media de los demás. Y yo creo que así ha de ser. Me siento un
poco culpable cuando veo cómo los demás trabajan tanto y yo sólo tengo
dos o tres horas de calidad al día y aún así siempre he sido uno de los
miembros más productivos del equipo. Quizá por eso, cuando Peopleware y
XP (Extreme Programming) insisten en eliminar las horas extras y las
jornadas de 40 horas semanales lo hacen con la completa seguridad de que
esto no implica una reducción en el rendimiento del equipo.

Pero los días que me preocupan no son en los que "sólo" trabajo dos o
tres horas. Son aquellos días en los que no puedo rendir nada.

Le he dado muchas vueltas a esto. He tratado de recordar cuál ha sido la
vez en mi carrera que más trabajo he sacado adelante. Probablemente fue
cuando Microsoft me cambió a un nuevo y bonito despacho enmoquetado con
grandes ventanas que dominaban un lindo patio empedrado, lleno de
cerezos en flor. Todo latía. Durante meses trabajé sin parar,
despachando la especificación detallada de Excel Basic: una montaña de
papeles que abarcaban un gigantesco modelo de objetos y todo un entorno
de programación. Literalmente: no podía parar. Cuando tuve que ir a
Boston al MacWorld me llevé un portátil y documenté las clases de
Windows sentado en una agradable terraza en el HBS \[Harvard Business
School\].

Una vez que te pones manos a la obra no es tan difícil seguir a buen
ritmo. Muchos de mis días transcurren de esta manera: (1) ir al trabajo
(2) leer el correo, navegar por la red, etc. (3) decidir que voy a ir a
almorzar antes de ponerme a trabajar (4) volver de la comida (5) leer el
correo, navegar por la red, etc. (6) decidir por fin que debería empezar
(7) leer el correo, navegar por la red, etc. (8) decidir otra vez que
debería ponerme a trabajar (9) lanzar el maldito editor y (10) escribir
código casi sin parar hasta que no me doy ni cuenta de que ya son las 7
y media de la tarde.

En alguna parte entre los pasos 8 y 9 parece haber un bug, porque no
siempre puedo dar ese salto.

Para mí, ponerme manos a la obra es lo único difícil: un objeto
en reposo tenderá a permanecer en reposo. Hay en mi cerebro algo que
pesa muchísimo y es difícil hacer que alcance la velocidad de crucero;
pero una vez que la alcanza no cuesta ningún trabajo hacer que siga.
Como una bicicleta preparada para atravesar un país entero: cuando
comienzas a pedalear en una bici con todo ese material es difícil de
creer cuánto cuesta arrancar, pero luego es tan sencillo como ir con una
bicicleta sin carga alguna.

Quizá sea esta la clave de la productividad: ponerse en marcha. Tal vez
cuando la programación por parejas funciona es porque cuando organizas
una sesión de programación en pareja con tu compañero, ambos os estáis
forzando a poneros en marcha.

Cuando fui paracaidista en el ejército israelí un general nos dió un
pequeño discurso acerca de la estrategia. En las batallas de infantería,
según nos contó, sólo hay una única estrategia: Disparar y Avanzar. Uno
se mueve hacia el enemigo mientras a la vez dispara sus armas. El fuego
obliga al enemigo a agachar la cabeza de modo que no puede dispararte
(eso es lo que quieren decir los soldados cuando gritan "¡cubridme!",
que significa: "Dispárale al enemigo de forma que se tenga que esconder
y no pueda dispararme mientras cruzo la calle". Y funciona). El avance
te permite capturar territorio y acercarte a tu enemigo, donde es más
probable que tus disparos den en el blanco. Si no avanzas, el enemigo
decide lo que ocurre, lo cual no es bueno. Si no disparas el enemigo te
disparará, teniendo un objetivo fácil.

Recordé esto durante mucho tiempo. Me di cuenta de que casi todas las
estrategias militares, desde los combates aéreos a las maniobras navales
a gran escala, están basadas en la idea de Disparar y Avanzar. Tardé
otros quince años en darme cuenta de que el principio de Disparar y
Avanzar es la forma en que se hacen las cosas en esta vida. Tienes que
avanzar un poquito cada día. No importa si tu código está mal escrito y
tiene errores y nadie lo quiere. Si avanzas, escribiendo código y
arreglando los errores continuamente, el tiempo está de tu parte. Presta
atención cuando la competencia te dispara. ¿No querrán mantenerte
ocupado, reaccionando a sus boleas, de forma que no puedas avanzar?
Recordemos la historia de las estrategias de acceso a bases de datos que
han surgido de Microsoft. ODBC, RDO, DAO, ADO, OLEDB, y ahora ADO.NET
¡Todas novísimas! ¿Acaso todas son imperativos tecnológicos? ¿O son el
resultado de un grupo de diseño incompetente que necesita reinventar el
acceso a base de datos cada año? (Es probable que, en realidad, sea esto
último) Pero el resultado final es que únicamente se trata de fuego de
cobertura. La competencia no tiene otra opción que perder todo su tiempo
portando y manteniéndose al día, tiempo que no pueden dedicar a
desarrollar nuevas prestaciones. Examinemos de cerca el panorama del
software. Las compañías que funcionan son las que dependen menos de
compañías grandes y no tienen que perder todos sus ciclos de desarrollo
poniéndose al día, reimplementando y arreglando errores que sólo se
manifiestan bajo Windows XP. Las compañías que se tambalean son las que
pasan demasiado tiempo leyendo hojas de té para vaticinar el próximo
movimiento de Microsoft. La gente se preocupa por .NET y decide
re-escribir todo su código porque creen que tienen que hacerlo.
Microsoft te dispara, y sólo es fuego de cobertura de forma que ellos
puedan avanzar y tú no, porque así es como se juega a este juego,
muchachos. ¿Vas a añadir soporte para Hailstorm? ¿SOAP? ¿RDF? Lo vas a
soportar porque tus clientes lo necesitan, o porque alguien te está
disparando y te sientes obligado a responder? Los equipos comerciales de
las grandes compañías, que conocen lo que es el fuego de cobertura, van
a sus clientes y les dicen: "Está bien, no tienes que comprarnos a
nosotros. Cómprale al mejor vendedor. Pero asegúrate de que compras un
producto que soporta (XML / SOAP / CDE /J2EE) porque si no estarás
atrapado en el software propietario" Luego, cuando las compañías
pequeñas intentan venderle algo a ese cliente, se encuentran con
gerentes obedientes que repiten como cotorras: "¿Tienes J2EE?" Y lo
único que hacen es perder todo el tiempo desarrollando con J2EE incluso
aunque eso no te de más ventas, y no les da ninguna oportunidad para
diferenciarse de los demás. Es una prestación de catálogo; la
implementas porque necesitas el recuadro que dice que lo tienes, pero
nadie la va a usar ni la necesita. Y es fuego de cobertura.

Para las compañías pequeñas como la mía disparar y avanzar significa dos
cosas. Tienes que tener el tiempo de tu parte y tienes que avanzar cada
día. Tarde o temprano ganarás. Lo único que logré hacer ayer fue mejorar
un poquitín el esquema de colores de FogBUGZ. Eso está bien. Está
mejorando continuamente. Cada día nuestro software es mejor y mejor y
tenemos más y más clientes, eso es todo lo que nos importa. Hasta que
seamos una compañía tan grande como Oracle, no tenemos que pensar en
grandes estrategias. Únicamente hay que venir cada mañana y, de algún
modo, arrancar el editor.


# -*- coding: utf-8 -*-



class Model:
    """Representa un modelo de objeto en el diagrama."""

    def __init__(self, name, superclass):
        self.name = name
        self.superclass = superclass
        self.attributes = []
        self.methods = []

    def add(self, value):
        """Agrega un elemento que puede ser atributo o metodo."""
        if self._it_seems_like_a_method(value):
            self.methods.append(value)
        else:
            self.attributes.append(value)

    def _it_seems_like_a_method(self, word):
        """Indica si la palabra representa un nombre de metodo."""
        if ':' in word or '(' in word:
            return True






def get_identation_width(line):
    "Reporta la longitud de una identacion."
    i = 0
    line = line.replace("\t", "    ")

    for c in line:
        if c == ' ':
            i += 1
        else:
            break

    return i

def is_empty(line):
    "Informa si la linea no tiene caracteres."
    return bool(line.strip())


# Enumeraciones
STATE_STARTING, STATE_POPULATING = range(2)

identation_column = 0
previous_identation_column = 0


file_handler = open('parser_ejemplo.txt')
state = STATE_STARTING
models = []
model = None
actual_father = []
minimum_width = 4

for line in file_handler.readlines():
    if not is_empty(line):
        continue

    identation_column = get_identation_width(line)

    # Intenta determinar el tamano de tabulacion que usa el usuario.
    if identation_column > 0:
        minimum_width = min(identation_column, minimum_width)

    if identation_column > previous_identation_column:
        print ">> (tabulaciones) 1"
        previous_identation_column = previous_identation_column
        print actual_father
        print "----------------"

        # Encuentra una subclase mientras carga el modelo.
        if state == STATE_POPULATING:
            #actual_father.append(previous_line)

            if model:
                models.append(model)
                state = STATE_STARTING

        # Comienza a definir los atributos de la clase.
        if state == STATE_STARTING:
            state = STATE_POPULATING

            # Determina la superclase del modelo actual.
            if model:
                if actual_father:
                    print "para superclase de", previous_line, "hay:",
                    print actual_father
                    superclass = actual_father[-1]
                else:
                    superclass = None
            else:
                superclass = None

            model = Model(previous_line, superclass)

        actual_father.append(previous_line)

    elif identation_column < previous_identation_column:

        if state == STATE_POPULATING:
            model.add(previous_line)

        # determina la cantidad de identacion que ha eliminado
        print "<< (tabulaciones)",
        i = (previous_identation_column - identation_column) / minimum_width
        print i

        for n in range(i):
            a = actual_father.pop()
            print "Haciendo pop de:", a

    else:

        if state == STATE_POPULATING:
            model.add(previous_line)

    print "- \t" + line,
    previous_identation_column = identation_column
    previous_line = line.strip()
        

if state == STATE_POPULATING:
    model.add(previous_line)

models.append(model)
file_handler.close()


for m in models:
    print vars(m)

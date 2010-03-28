# -*- encoding: utf-8 -*-

def create_separarator(widths, char):
    """Genera una linea para separar filas de una tabla.

    El parametro `widths` es un lista indicando el ancho de cada
    columna. En cambio el argumento `char` es el caracter que se
    tiene que utilizar para imprimir.

    El valor retornado es un string.

    Por ejemplo::

        >>> create_separarator([2, 4], '-')
        '+----+------+'
    """

    line = []

    for w in widths:
        line.append("+" + char * (w + 2))

    line.append("+")
    return ''.join(line)


def create_line(columns, widths):
    """Crea una fila de la tabla separando los campos con un '|'.

    El argumento `columns` es una lista con las celdas que se
    quieren imprimir y el argumento `widths` tiene el ancho
    de cada columna. Si la columna es mas ancha que el texto
    a imprimir se agregan espacios vacíos.

    Por ejemplo::

        >>> create_line(['nombre', 'apellido'], [7, 10])
        '| nombre  | apellido   |'
    """
    
    line = zip(columns, widths)
    result = []

    for text, width in line:
        result.append("| " + text.ljust(width) + " ")

    result.append("|")
    return ''.join(result)

def create_table(content):
    """Imprime una tabla en formato restructuredText.

    El argumento `content` tiene que ser una lista
    de celdas.

    Por ejemplo::

        >>> print create_table([['software', 'vesion'], ['python', '2.6'], ['vim', '7.2']])
        +----------+--------+
        | software | vesion |
        +==========+========+
        | python   | 2.6    |
        +----------+--------+
        | vim      | 7.2    |
        +----------+--------+
    """

    # obtiene las columnas de toda la tabla.
    columns = zip(*content)
    # calcula el tamano maximo que debe tener cada columna.
    widths = [max([len(x) for x in i]) for i in columns]

    result = []

    result.append(create_separarator(widths, '-'))
    result.append(create_line(content[0], widths))
    result.append(create_separarator(widths, '='))

    for line in content[1:]:
        result.append(create_line(line, widths))
        result.append(create_separarator(widths, '-'))

    return '\n'.join(result)

print create_table([['software', 'vesion'], ['python', '2.6'], ['vim', '7.2']])

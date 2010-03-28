python << end
# -*- encoding: utf-8 -*-
import vim
import re





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



def are_in_a_table(current_line):
    "Indica si el cursor se encuentra dentro de una tabla."
    return "|" in current_line or "+" in current_line

def get_table_bounds(current_row_index):
    """Obtiene el numero de fila donde comienza y termina la tabla.

    Retorna ambos valores como una tupla.
    """

    bottom = 0
    top = 0
    buffer = vim.current.buffer
    max = len(buffer)

    for a in range(current_row_index, 0, -1):
        if not are_in_a_table(buffer[a]):
            top = a
            break

    for b in range(current_row_index, max):
        if not are_in_a_table(buffer[b]):
            bottom = b
            break

    return top + 1, bottom - 1

def remove_spaces(string):
    "Elimina los espacios innecesarios de una fila de tabla."
    return re.sub("\s\s+", " ", string)

def extract_cells_as_list(string):
    "Extrae el texto de una fila de tabla y lo retorna como una lista."
    string = remove_spaces(string)
    return [item.strip() for item in string.split('|') if item]

def extract_table(buffer, top, bottom):
    content = []
    full_table_text = buffer[top:bottom]
    # selecciona solamente las lineas que tienen celdas con texto.
    only_text_lines = [x for x in full_table_text if '|' in x]
    # extrae las celdas y descarta los separadores innecesarios.
    return [extract_cells_as_list(x) for x in only_text_lines]


def copy_to_buffer(buffer, string, index):
    lines = string.split('\n')
    for line in lines:
        buffer[index] = line
        index += 1

def remove_table(current_row_index):
    """Elimina la tabla que contiene la celda indicada
    por argumento.

    `initial_row` es un numero entero que indica en que
    linea se encuenta el cursor."""

    r1, r2 = get_table_bounds(current_row_index)

    #vim.current.buffer[r1] = "comienza"
    #vim.current.buffer[r2] = "termina"

    table_as_list = extract_table(vim.current.buffer, r1, r2)
    table_content = create_table(table_as_list)
    copy_to_buffer(vim.current.buffer, table_content, r1)


(row, col) = vim.current.window.cursor
line = vim.current.buffer[row-1]

if are_in_a_table(line):
    remove_table(row-1)
else:
    print "No estoy en una tabla. Terminando..."





end

python << end
import vim
import re

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


def remove_table(current_row_index):
    """Elimina la tabla que contiene la celda indicada
    por argumento.

    `initial_row` es un numero entero que indica en que
    linea se encuenta el cursor."""

    r1, r2 = get_table_bounds(current_row_index)

    #vim.current.buffer[r1] = "comienza"
    #vim.current.buffer[r2] = "termina"

    table = extract_table(vim.current.buffer, r1, r2)
    print table


(row, col) = vim.current.window.cursor
line = vim.current.buffer[row-1]

if are_in_a_table(line):
    remove_table(row-1)
else:
    print "No estoy en una tabla. Terminando..."





end

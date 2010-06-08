if has('python')
python << EOF
# -*- encoding: utf-8 -*-
import vim
import re
import string
 
DEFAULT_MARK = '☐'
MARKS = ['☐', '☑', '[_]', '[X]', '☒', '✗']
INDENT_WIDTH = 4
TO_DONE_DICT = {
                '☐': '☑', 
                '[_]': '[X]',
                 '☒': '☑',
               }
TO_EMPTY_DICT = {
                 '☑': '☐', 
                 '[X]': '[_]',
                 '☒': '☐',
                }
TO_CANCEL_DICT = {
                '☐': '☒', 
                '[_]': '[X]',
                '☑': '☒',
               }


def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text

def get_current_line():
    (row, col) = vim.current.window.cursor
    return vim.current.buffer[row-1]
    
def set_current_line(line):
    (row, col) = vim.current.window.cursor
    vim.current.buffer[row-1] = line

def have_any_of_this_charactes(string, words):
    for w in words:
        if w in string:
            return True

def MarkDone():
    line = get_current_line()
    new_line = replace_all(line, TO_DONE_DICT)
    set_current_line(new_line)

def MarkCancel():
    line = get_current_line()
    new_line = replace_all(line, TO_CANCEL_DICT)
    set_current_line(new_line)

def CreateTask():
    line = vim.current.line

    if have_any_of_this_charactes(line, MARKS):
        new_line = replace_all(line, TO_EMPTY_DICT)
    else:
        if re.match("(\S+)", line):
            new_line = re.sub("(\S+)", "%s \\1" %(DEFAULT_MARK), line, count=1)
        elif re.match("^(\s+)", line):
            new_line = re.sub("^(\s+)", "\\1%s " %(DEFAULT_MARK), line, count=1)
        else:
            new_line = DEFAULT_MARK + " .."

    vim.current.line = new_line

def tlConvertToOTL():
    size = len(vim.current.buffer)

    for i in range(0, size):
        vim.current.buffer[i] = vim.current.buffer[i] = "hola"

#a = vim.current.line
#(row, col) = vim.current.window.cursor


def CreateTaskIndent(extra_indent=0):
    "Genera una tarea en el mismo nivel de indentacion que la linea actual."


    # Genera la identacion de espacios que se le pida.
    indent = " " * INDENT_WIDTH * extra_indent

    if DEFAULT_MARK in vim.current.line:
        # Copia la linea actual para preservar la identación.
        vim.command("normal yyp")

        # Preserva la identación y coloca la marca de tarea sin texto.
        vim.current.line = re.sub("\S.*", indent + DEFAULT_MARK + " ", vim.current.line)
    else:
        CreateTask()

EOF


imap ,c <ESC>:python CreateTask()<CR>
map ,c a,c



imap ,d <ESC>:python MarkDone()<CR>A
map  ,d :python MarkDone()<CR>

imap ,s <ESC>:python MarkCancel()<CR>A
map  ,s :python MarkCancel()<CR>


map ,1 :python tlConvertToOTL()<CR>


map ,a :python CreateTaskIndent()<CR>A
imap ,a <ESC>,a


au BufRead,BufNewFile *.tl\= set ft=tl


endif

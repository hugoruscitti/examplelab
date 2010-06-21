# -*- coding: utf-8 -*-
# El objetivo de este ejemplo es procesar un archivo
# de texto con identación.



def get_identation_width(line):
    i = 0
    line = line.replace("\t", "    ")

    for c in line:
        if c == ' ':
            i += 1
        else:
            break

    return i



identation_column = 0
previous_identation_column = 1




file_handler = open('parser_ejemplo.txt')


<<<<<<< .mine

=======
d = {}
items = []
father_node = None


>>>>>>> .r40
for line in file_handler.readlines():

    identation_column = get_identation_width(line)

    if identation_column > previous_identation_column:
        previous_identation_column = previous_identation_column
<<<<<<< .mine
        #print "identacion ->"
        pass
=======

        if father_node:
            d[father_node] = items
            items = []
            father_node = None


        print "identacion ->"
>>>>>>> .r40
        father_node = previous_line
    elif identation_column < previous_identation_column:
        #print "end ident <-"
        pass
    else:
        items.append(previous_line)


    previous_identation_column = identation_column
<<<<<<< .mine
    #print "\t" + line.strip()
=======
    print line.rstrip()
    previous_line = line


>>>>>>> .r40
        
file_handler.close()
print d

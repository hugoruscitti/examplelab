import lxml.etree

file = file('ejemplo.xml')
document = lxml.etree.parse(file)

print "Contenido bajo root:"
root = document.getroot()

for element in root:
    print "\t", element
    for x in element:
        print "\t\t", x.tag, "\t\t", x.text

file.close()

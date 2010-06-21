import ConfigParser
import os

config = ConfigParser.ConfigParser()
files_to_read = ['options.ini', os.path.expanduser('~/.myconfig')]
config.read(files_to_read)

print "Sections"
print config.sections()
print ""

print "Ejecutando: get('buscadores', 'google')"
print config.get('buscadores', 'google')

import zipfile
import os

filename = 'compressed.zip'
zip = zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED)

for file in os.listdir('./'):

    if file.endswith('.py'):
        zip.write(file)

zip.close()
print "creado el archivo", filename

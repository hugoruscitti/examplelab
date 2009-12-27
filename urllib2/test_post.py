# Accede a un sitio web y obtiene una lista
# con todos los links.
import urllib
import urllib2

model = """
Name
    attr
    ---
    method
"""

url = "http://localhost:8080/"
post = {'diagram_code': model}
data_post = urllib.urlencode(post)
response = urllib2.urlopen(url + 'draw', data_post)

if response.code == 200:
    print url + response.read()
else:
    print "Imposible acceder al recurso '%s'" %(url)

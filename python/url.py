import urllib2

URL = "http://www.losersjuegos.com.ar"

try:
    file = urllib2.urlopen(URL)
    content = file.readlines()

    for line in content:
        print line[:10], "..."

    file.close()

except urllib2.URLError:
    print "Imposible acceder a %s" %(URL)


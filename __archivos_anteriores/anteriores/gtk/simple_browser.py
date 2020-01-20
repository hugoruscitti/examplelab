import gtkhtml2
import gtk
import urllib
import urlparse

opener = urllib.FancyURLopener()
currentUrl = None

def is_relative_to_server(url):
    parts = urlparse.urlparse(url)
    if parts[0] or parts[1]:
        return 0
    return 1

def open_url(url):
    uri = resolve_uri(url)
    return opener.open(uri)

def resolve_uri(uri):
    if is_relative_to_server(uri):
        return urlparse.urljoin(currentUrl, uri)
    return uri

def request_url(document, url, stream):
    f = open_url(url)
    stream.write(f.read())

def load_url(document, link):
    global currentUrl

    try:
        f = open_url(link)
    except OSError:
        print "failed to open", link
        return

    currentUrl = resolve_uri(link)
    document.clear()
    headers = f.info()
    mime = headers.getheader('Content-type').split(';')[0]

    if mime:
        document.open_stream(mime)
    else:
        document.open_stream('text/plain')

    print "mimetype is:", mime

    document.write_stream(f.read())
    document.close_stream()

#document.connect('request_url', request_url)
#document.connect('link_clicked', link_clicked)

def open_map(document):
    text = """<iframe style='border: 1px solid black;' width="425"
    height="350" frameborder="0" scrolling="no" marginheight="0"
    marginwidth="0"
    src="http://maps.google.com/maps/ms?ie=UTF8&amp;hl=en&amp;s=AARTsJrW0G61FhPmfcDOS-5oywYLf42PFg&amp;msa=0&amp;msid=100782103439917143396.000448ebf1bfed25857df&amp;ll=3.162456,-48.515625&amp;spn=104.451773,149.414063&amp;z=2&amp;output=embed"></iframe><br
    /><small><a
    href="http://maps.google.com/maps/ms?ie=UTF8&amp;hl=en&amp;msa=0&amp;msid=100782103439917143396.000448ebf1bfed25857df&amp;ll=3.162456,-48.515625&amp;spn=104.451773,149.414063&amp;z=2&amp;source=embed"
    style="color:#0000FF;text-align:left">View Larger Map</a></small>"""

    document.clear()
    document.open_stream('text/html')
    document.write_stream(text)
    document.close_stream()

def request_object(*args):
    print 'request object', args


if __name__ == '__main__':
    view = gtkhtml2.View()
    document = gtkhtml2.Document()
    #load_url(document, "http://www.losersjuegos.com.ar")
    open_map(document)

    view.set_document(document)
    view.connect('request_object', request_object)

    sw = gtk.ScrolledWindow()
    sw.add(view)

    window = gtk.Window()
    window.add(sw)
    window.set_default_size(400, 400)

    window.show_all()

    gtk.main()

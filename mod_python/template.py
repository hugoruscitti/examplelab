from Cheetah.Template import Template

keys = {'name': 'hugo', 'lastname': 'ruscitti'}


t = Template(file='templates/hi.html', searchList=keys)
print t

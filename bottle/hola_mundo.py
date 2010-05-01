from bottle import route, run

@route('/')
def home():
    return "Hola mundo !!"

run(reloader=True)

from bottle import route, run, static_file


@route('/')
def home():
    return static_file('index.html', root='public')


@route('/<filename>')
def server_static(filename):
    return static_file(filename, root='public')


run(host='localhost', port=8080, debug=True)

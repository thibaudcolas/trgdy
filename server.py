from bottle import route, run, static_file

@route('/')
def home():
    return static_file('index.html', root='')

@route('/<filename>')
def server_static(filename):
    return static_file(filename, root='')

run(host='localhost', port=8080, debug=True)

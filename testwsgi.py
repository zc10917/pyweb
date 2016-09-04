from wsgiref.simple_server import make_server


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')

    return [body.encode('UTF-8')]


httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
httpd.serve_forever()

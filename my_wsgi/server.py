import json
from wsgiref.simple_server import make_server
def application(environ, start_response):
    start_response('200 ok', [('Content-Type','application/json')])
    return [json.dumps(dict(result='hello world')).encode('utf-8')]

httpd = make_server('', 80, application)
print('Serving HTTP on port 80')
httpd.serve_forever()
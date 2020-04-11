def hello(environ, start_response):
    file = environ.get('wsgi.input')
    body_request = open(file).read()
    body_response = body_request[:2].split('&')
    status = '200 OK'
    headers = [
    ('Content-Type', 'text/plain')
    ]
    start_response(status, headers )
    return body_response

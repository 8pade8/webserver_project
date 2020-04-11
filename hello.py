def hello(environ, start_response):
    querystring = environ.get('QUERY_STRING')
    body_response = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
    status = '200 OK'
    headers = [
    ('Content-Type', 'text/plain')
    ]
    start_response(status, headers )
    return body_response

from gunicorn.http import wsgi

class Response(wsgi.Response):
    """Class used for altering or forwarding response info such as headers"""
    def default_headers(self, *args, **kwargs):
        headers = super(Response, self).default_headers(*args, **kwargs)
        return [h for h in headers if not h.startswith('Server:')]

wsgi.Response = Response

errorlog = '-'
loglevel = 'info'
accesslog = '-'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
secure_scheme_headers = {'X-FORWARDED-PROTOCOL': 'ssl',
                         'X-FORWARDED-PROTO': 'https',
                         'X-FORWARDED-SSL': 'on'}

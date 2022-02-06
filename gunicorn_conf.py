bind = ':8001'
worker_class = 'sync'
loglevel = 'debug'
accesslog = '/var/www/flasket.net/logs/flasket_access.log'
acceslogformat ="%(h)s %(l)s %(u)s %(t)s %(r)s %(s)s %(b)s %(f)s %(a)s"
errorlog =  '/var/www/flasket.net/logs/flasket_error.log'

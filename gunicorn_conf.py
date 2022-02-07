bind = ':7000'
worker_class = 'sync'
loglevel = 'debug'
accesslog = '/srv/www/flasket-app/logs/flasket_access.log'
acceslogformat ="%(h)s %(l)s %(u)s %(t)s %(r)s %(s)s %(b)s %(f)s %(a)s"
errorlog =  '/srv/www/flasket-app/logs/flasket_error.log'


import sys
import signal
import time
import os
import logging
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from gevent.pywsgi import WSGIServer
from flask import Flask
from flask_restful import Api
from flasgger import Swagger
from werkzeug.middleware.proxy_fix import ProxyFix

from myproject.utils import JsonDateTimeEncoder
from myproject.utils.configuration import Configuration
from myproject.utils.webcfg import config

# adding 15 seconds delay to force first scheduled job run
sched_now = datetime.now() + timedelta(0, 15)

scheduler = BackgroundScheduler()
logging.getLogger('apscheduler.executors.default').setLevel(logging.WARNING)

START = time.time()
log = logging.getLogger("web")

filename = os.path.expanduser('~')
configuration = os.path.join(filename, ".myproject", "configuration.yaml")
c = Configuration(filename=configuration)

webapp = None
swagger = None
restful = None


def init_webapp():
    global webapp
    global swagger
    global restful
    log.debug("Init & Configure Flask")
    path_rest = os.path.join(os.path.dirname(__file__), "rest")

    webapp = Flask(
        __name__,
        root_path=path_rest
    )
    for c in config:
        if c.startswith('flask_'):
            v = c.replace('flask_', '').upper()
        else:
            v = c
        webapp.config[v] = config[c]

    webapp.config['TEMPLATES_AUTO_RELOAD'] = True
    webapp.wsgi_app = ProxyFix(
        webapp.wsgi_app,
        x_port=0,
        x_host=1,
        x_proto=1
    )
    # TODO: ma tutta questa roba non si può mettere in un file?!

    log.debug("Init Swagger")
    webapp.config['SWAGGER'] = {
        "title": config.name + " " + config.get_version(),
        "uiversion": 2,
        'ignore_verbs': ['OPTIONS']
    }
    webapp.config['RESTFUL_JSON'] = {
        'cls': JsonDateTimeEncoder
    }
    webapp.config['uwsgi'] = {
        'enable-threads': True
    }

    swagger = Swagger(webapp, template={"info": {"title": config.name, "version": config.api}})
    log.debug("Init Flask-restful")
    restful = Api(webapp)


def api_importer():
    import importlib
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "rest")
    init_webapp()
    for f in os.listdir(path):
        if f.endswith(".py") and not f.startswith("__"):
            modulename = ".rest.%s" % f.split(".py")[0]
            log.info("Importing%s" % modulename.replace(".", " "))
            importlib.import_module(modulename, "myproject")


class HTTPServer(object):

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self._http_server = WSGIServer((config.server, int(config.port)), webapp, log=self.logger)
        self._start = time.time()
        self._stop = 0

    @property
    def config(self):
        return config

    @property
    def http_server(self):
        return self._http_server

    def stop(self):
        self._http_server.stop(config.stop_timeout)

    def run(self):
        self._stop = time.time()
        self.logger.critical('Startup in ' + "{:1.5f}".format(self._stop - START) + "s")
        self.logger.critical('Listening on %s:%d', config.server, int(config.port))
        self._http_server.serve_forever()


def sig_handler(signum, stack):
    if signum in [1, 2, 3, 15]:
        log.warning('Caught signal %s, exiting.', str(signum))
        app.stop()
        sys.exit()
    return stack


def set_sig_handler(funcname, avoid=('SIG_DFL', 'SIGSTOP', 'SIGKILL')):
    for i in [x for x in dir(signal) if x.startswith("SIG") and x not in avoid]:
        try:
            signum = getattr(signal, i)
            signal.signal(signum, funcname)
        except (OSError, RuntimeError, ValueError) as m:  # OSError for Python3, RuntimeError for 2
            log.warning("Skipping {} {}".format(i, m))


def server():
    global app
    api_importer()
    set_sig_handler(sig_handler)
    log.info("Loading web server")
    app = HTTPServer()
    scheduler.start()
    app.run()

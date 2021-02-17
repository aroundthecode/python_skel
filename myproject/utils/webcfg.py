import os
import logging
import time

import pkg_resources

LOG_LEVELS = {
    'FATAL': logging.FATAL,
    'CRITICAL': logging.CRITICAL,
    'ERROR': logging.ERROR,
    'WARNING': logging.WARNING,
    'INFO': logging.INFO,
    'DEBUG': logging.DEBUG
}

VALID_PROPERTIES = {
    'server': '',
    'port': '5000',
    'log_level': 'INFO',
    'stop_timeout': '1',
    "cache_timeout": '60',
    'docker_master': 'unix://var/run/docker.sock',
    'backend': "k8",
    'prometheus': "https://prometheus.preprod.k8.facilitylive.int",
    'tiller_host': "auto",
    'tiller_timeout': 300,
    'user': "",
    'password': "",
    'spark_namespace': "spark",
    'debug_server': False,
    'stop_token': "QW4gaW52YWxpZCByZXNwb25zZSB3YXMgcmVjZWl2ZWQgZnJvbSB0aGUgdXBzdHJlYW0gc2VydmVyLgoK",
    'profile': 'local'
}


class Config(object):
    """
        This is the main configuration class
        is thread safe 'cause you cannot write new values :)
    """

    def __init__(self):

        self.logger = logging.getLogger(self.__class__.__name__)

        self._props = dict()
        self._props['name'] = "myproject"
        self._props['version'] = "1.0.0"
        self._props['api'] = 'v1'
        self._props['startup'] = time.time()
        self.__load_env_vars()

        if self.log_level.upper() == "DEBUG":
            lformat = "%(asctime)s | %(levelname)9s | %(name)12s | %(filename)s:%(lineno)d | %(message)s"
        else:
            lformat = "%(asctime)s | %(levelname)9s | %(name)12s | %(message)s"
        logging.basicConfig(format=lformat, level=LOG_LEVELS[self.log_level.upper()])

    @staticmethod
    def get_version():
        return pkg_resources.require("myproject")[0].version

    @staticmethod
    def get_profile():
        return VALID_PROPERTIES.get("profile")

    def __load_env_vars(self):
        name = "{}_".format(str.upper(self._props['name']))
        for v in os.environ:
            if v.startswith(name):
                k = v.replace(name, '').lower()
                if k in VALID_PROPERTIES or k.startswith('flask_'):
                    VALID_PROPERTIES[k] = os.environ[v]
                else:
                    print("Unknown property: [{}]".format(k))

        for p in VALID_PROPERTIES:
            self._props[p] = VALID_PROPERTIES[p]

    def __iter__(self):
        for p in self._props:
            yield p

    def __str__(self):
        return str(self._props)

    def __getitem__(self, item):
        if item not in self._props:
            raise KeyError
        return self._props[item]

    def __getattr__(self, item):
        if item in self._props:
            return self._props[item]

    def __setitem__(self, key, value):
        self._props[key] = value
        return self._props[key]


config = Config()

if config.debug_server:
    import ptvsd
    logging.critical("Loading debug server on 0.0.0.0:5678")
    ptvsd.enable_attach(('0.0.0.0', 5678), redirect_output=True)


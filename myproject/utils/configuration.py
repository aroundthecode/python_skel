import os
import logging
import yaml

log = logging.getLogger("configuration")
configuration = {}


class Configuration:

    def __init__(self, filename=""):

        global configuration

        if os.path.isfile(filename):
            log.debug("Reading credentials from [%s]" % filename)
            config_file = filename

            try:
                with open(config_file) as fp:
                    configuration = yaml.load(fp, Loader=yaml.FullLoader)
            except OSError as e:
                log.error("Unable to open file [%s]: %s" % (config_file, e))

    @staticmethod
    def credential(credential=""):

        base = "MYPROJECT_"

        cred_key = base + credential.upper() + "_USER"
        cred_pwd = base + credential.upper() + "_PASSWORD"

        username = os.getenv(cred_key)
        password = os.getenv(cred_pwd)

        if username is not None and password is not None:
            pass
        elif 'credentials' in configuration and credential in configuration['credentials']:
            username = configuration['credentials'][credential]['user']
            password = configuration['credentials'][credential]['pass']
        else:
            username = os.getenv("MYPROJECT_USER")
            password = os.getenv("MYPROJECT_PASSWORD")

        log.debug("Using user [%s]" % username)
        return username, password

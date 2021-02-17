from myproject.web import webapp, log, config, swagger, c
from myproject.utils.web import generate_response
from myproject.utils.webcfg import config
from flask import url_for, redirect, session, render_template, request
import os
import logging

webapp.secret_key = os.urandom(12)

logger = logging.getLogger("web_api")


@webapp.route('/health', methods=["GET", "HEAD"])
@webapp.route('/healthz', methods=["GET", "HEAD"])
def health():
    return generate_response()


@webapp.route('/info')
def info():
    """
       Basic info
       ---
       parameters: {}
       responses:
         200:
          description: "Return a json with some internal info"
    """
    ret = dict()
    import time
    ret['app'] = {'name': config.name, 'ver': Config.get_version(), 'profile': Config.get_profile()}
    ret['api'] = {
        'ver': config.api,
        'docs': url_for('flasgger.apidocs'),
        'spec': url_for('flasgger.apispec_1')
    }
    ret['uptime'] = "%0.0f" % (time.time() - config.startup)
    ret['status'] = 'OK'

    return generate_response(ret, 200)


log.debug(str(webapp.config))
log.debug(str(swagger.config))


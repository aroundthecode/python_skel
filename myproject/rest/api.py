from myproject.web import webapp, log, config, swagger, c
from myproject.utils.web import generate_response
import os
import logging

webapp.secret_key = os.urandom(12)

logger = logging.getLogger("web_api")


@webapp.route('/health', methods=["GET", "HEAD"])
@webapp.route('/healthz', methods=["GET", "HEAD"])
def health():
    return generate_response()


log.debug(str(webapp.config))
log.debug(str(swagger.config))


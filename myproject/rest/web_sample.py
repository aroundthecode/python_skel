from myproject.web import webapp
from myproject.utils import web as wutils
from myproject.backend.sample import hello


@webapp.route('/sample/<string:name>/', methods=["GET"])
def get_sample(name):
    """
    view Pages json data
    ---
    parameters:
      - in: path
        name: name
        required: true
        schema:
          type: string
        description: "Name to wave"

    responses:
      200:
        description: "hello sample"
    """

    ret = hello(
        name=name
    )
    return wutils.generate_response(
        data=ret
    )
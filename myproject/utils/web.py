from flask import make_response, send_file
import json
from myproject.utils import JsonDateTimeEncoder

CONTENT_TYPE = str('application/json; charset=utf-8')


def generate_response(data=None, code=200, headers=None, content_type=CONTENT_TYPE):
    if data:
        if "json" in content_type:
            data = json.dumps(data, cls=JsonDateTimeEncoder)
        resp = make_response(data, code)
    else:
        resp = make_response("", code)

    resp.mimetype = content_type
    resp.headers.set("content-type", content_type)
    resp.headers.extend(headers or {})

    return resp


def generate_attachment(data=None, filename="data.json"):
    resp = make_response(data)
    resp.headers.set("content-type", 'text/plain; charset=UTF-8')
    resp.headers.set("Content-Disposition", 'attachment; filename=' + filename)
    return resp

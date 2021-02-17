import hashlib
import json
import typing
from datetime import datetime


def hash_md5(content: typing.Hashable) -> str:
    j = json.dumps(content).encode("UTF-8")
    return hashlib.md5(j).hexdigest()


class JsonDateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        # raise typeerror when is not date (but not serializable anyway)
        return json.JSONEncoder.default(self, o)

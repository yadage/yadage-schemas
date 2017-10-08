import json
import jsonref

class WithJsonRefEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, jsonref.JsonRef):
            return {k: v for k, v in obj.items()}
        elif type(obj)==map:
            return list(obj)
        try:
            super(WithJsonRefEncoder, self).default(obj)
        except TypeError:
            return obj.json()

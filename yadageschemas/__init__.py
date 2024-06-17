import json

try:
    from importlib.resources import files
except ImportError:
    # Support Python 3.8 as importlib.resources added in Python 3.9
    # https://docs.python.org/3/library/importlib.resources.html#importlib.resources.files
    from importlib_resources import files

from . import dialects
from .utils import WithJsonRefEncoder
from .validator import validate_spec

schemadir = files("yadageschemas")

def load(spec, specopts, validate = True, validopts = None, dialect = 'raw_with_defaults'):
    data = dialects.handlers[dialect](spec, specopts)
    if validate:
        validate_spec(data,validopts)
    return json.loads(json.dumps(data, cls=WithJsonRefEncoder))

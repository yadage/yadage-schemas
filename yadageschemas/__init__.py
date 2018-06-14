import json
import pkg_resources

schemadir = pkg_resources.resource_filename('yadageschemas','')

from .utils import WithJsonRefEncoder
from . import dialects
from .validator import validate_spec

def load(spec, specopts, validate = True, validopts = None, dialect = 'raw_with_defaults'):
    data = dialects.handlers[dialect](spec, specopts)
    if validate:
        validate_spec(data,validopts)
    return json.loads(json.dumps(data, cls=WithJsonRefEncoder))

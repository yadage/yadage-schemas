import os
import json
import jsonref
import jsonschema
from . import schemadir as default_schemadir

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

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

def schemabase_uri(schemadir):
    schemabase = None
    if schemadir == None:
        schemabase = 'file://'+os.path.abspath(default_schemadir)
    elif schemadir=='from-github':
        schemabase = 'https://raw.githubusercontent.com/lukasheinrich/cap-schemas/master/schemas'
    else:
        schemabase = 'file://'+os.path.abspath(schemadir)
    return schemabase

def schema_and_refresolver(schema_name,schemadir):
    schemabase = schemabase_uri(schemadir)

    abspath = '{}/{}.json'.format(schemabase,schema_name)
    refrelpath = abspath.rsplit('/',1)[0]+'/'

    schema   = json.loads(urlopen(abspath).read().decode('utf-8'))
    resolver = jsonschema.RefResolver(refrelpath, schema)
    return schema, resolver

def handler_decorator():
    handlers = {}

    def decorator(name):
        def wrap(func):
            handlers[name] = func
            return func
        return wrap
    return handlers, decorator

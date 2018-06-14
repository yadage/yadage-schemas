import pkg_resources
import os
import json

from .utils import urlopen, schema_and_refresolver

from .dialects import raw_with_defaults
from jsonschema import Draft4Validator

def validator(schema_name,schemadir):
    schema, resolver = schema_and_refresolver(schema_name,schemadir)
    return Draft4Validator(schema, resolver = resolver)

def validate_spec(data, validopts):
    return validator(**validopts).validate(data)

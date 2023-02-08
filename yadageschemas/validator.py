
from .utils import schema_and_refresolver

from .dialects import raw_with_defaults
assert raw_with_defaults
from jsonschema import Draft6Validator

def validator(schema_name,schemadir):
    schema, resolver = schema_and_refresolver(schema_name,schemadir)
    return Draft6Validator(schema, resolver = resolver)

def validate_spec(data, validopts):
    return validator(**validopts).validate(data)

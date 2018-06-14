import yadageschemas
import json

def test_load_jsondump():
    spec, specopts = 'workflow.yml', {
        'toplevel': 'tests/testspecs/local-helloworld-jsonref',
        'schema_name': 'yadage/workflow-schema',
        'schemadir': yadageschemas.schemadir,
        'load_as_ref': False,
    }
    validopts = {
        'schema_name': 'yadage/workflow-schema',
        'schemadir': yadageschemas.schemadir,
    }
    data = yadageschemas.load(spec,specopts,validopts = validopts)
    json.dumps(data)

def test_load_default_unwrap():
    spec, specopts = 'workflow.yml', {
        'toplevel': 'tests/testspecs/mapreduce',
        'schema_name': 'yadage/workflow-schema',
        'schemadir': yadageschemas.schemadir,
        'load_as_ref': False,
    }
    validopts = {
        'schema_name': 'yadage/workflow-schema',
        'schemadir': yadageschemas.schemadir,
    }
    data = yadageschemas.load(spec,specopts,validopts = validopts)
    json.dumps(data)

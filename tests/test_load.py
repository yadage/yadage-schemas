import yadageschemas
import json

def test_load_jsondump():
    data = yadageschemas.load('workflow.yml','tests/testspecs/local-helloworld-jsonref', 'yadage/workflow-schema')
    json.dumps(data)

def test_load_default_unwrap():
    data = yadageschemas.load('workflow.yml','tests/testspecs/mapreduce', 'yadage/workflow-schema')
    json.dumps(data)

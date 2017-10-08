import yadageschemas
import json

def test_load_jsondump():
    data = yadageschemas.load('workflow.yml','tests/testspecs/local-helloworld-jsonref', 'yadage/workflow-schema')
    json.dumps(data)

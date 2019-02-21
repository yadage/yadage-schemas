from . import dialect

import os
import jsonref
import requests
import yaml
import logging
from jsonschema import Draft4Validator, validators
from ..utils import urlopen, schema_and_refresolver

log = logging.getLogger(__name__)

def extend_with_default(validator_class):
    validate_properties = validator_class.VALIDATORS["properties"]

    def set_defaults(validator, properties, instance, schema):
        if schema.get('title',None)=='Yadage Stage':
            if 'dependencies' in instance and type(instance['dependencies'])==list:
                log.debug('dependencies provided as list, assume jsonpath_ready predicate')
                instance['dependencies'] = {
                    "dependency_type" : "jsonpath_ready",
                    "expressions": instance["dependencies"]
                    }

        if "Scheduler" in schema.get('title','') and instance['scheduler_type'] in ['singlestep-stage','multistep-stage']:
            if(type(instance['parameters'])==dict):
                asarray = []
                for k,v in instance['parameters'].items():
                    if type(v) == dict and any(k in v for k in ['steps','stages','step']):
                        v['expression_type'] = 'stage-output-selector'
                    asarray.append({'key':k,'value':v})

                instance['parameters'] = asarray


        errors_found = False
        for error in validate_properties(
            validator, properties, instance, schema,
        ):
            errors_found = True
            yield error

        if errors_found: return

        for prop, subschema in properties.items():
            if "default" in subschema and type(instance) == dict:
                # Note not clear why this is the case, appeared in py3.X
                # intermittently on Travis
                instance.setdefault(prop, subschema["default"])

    validator = validators.extend(
        validator_class, {"properties" : set_defaults},
    )
    def validate(self, *args, **kwargs):
        for error in self.iter_errors(*args, **kwargs):
            pass
    validator.validate = validate
    return validator

DefaultValidatingDraft4Validator = extend_with_default(Draft4Validator)
DefaultValidatingDraft4Validator

FROMGITHUB_LOADBASE = 'https://raw.githubusercontent.com/lukasheinrich/yadage-workflows/master'
import json

def generic_gitlab_cern_url(toplevel):
    fields = toplevel.split(':')[1:]

    if len(fields) > 1:
        repo, subpath = fields
    else:
        repo = fields[0]
        subpath = ''

    repo = repo.split('@')
    if len(repo) > 1:
        repo, branch = repo
    else:
        repo = repo[0]
        branch = 'master'

    url = 'https://gitlab.cern.ch/{repo}/raw/{branch}'.format(repo = repo, branch = branch)
    if subpath:
        url += '/'+subpath
    return '{}___yadage___'.format(json.dumps({
        'repo': repo,
        'ref': branch,
        'subpath': subpath
    }))
    return url

def generic_github_url(toplevel):
    # format is github:<username/repo[@branch]>[:subpath]

    fields = toplevel.split(':')[1:]

    if len(fields) > 1:
        repo, subpath = fields
    else:
        repo = fields[0]
        subpath = ''

    repo = repo.split('@')
    if len(repo) > 1:
        repo, branch = repo
    else:
        repo = repo[0]
        branch = 'master'

    url = 'https://raw.githubusercontent.com/{repo}/{branch}'.format(
        repo = repo,
        branch = branch,
    )
    if subpath:
        url += '/'+subpath
    return url

import six.moves.urllib as urllib
def loader(toplevel):
    base_uri = None

    if toplevel.startswith('from-cap'):
        def caploader(uri):
            recordnr = toplevel.split('/')[1]
            import requests
            data = requests.get('https://analysis-preservation-qa.cern.ch/api/records/{}'.format(recordnr),verify=False).json()
            workflowinfo = {x['name']:x['workflow'] for x in data['metadata']['_metadata']['workflows']}
            return workflowinfo[uri]
        return caploader

    if toplevel.startswith('from-github'):
        within = toplevel.split('/',1)[-1]
        base_uri = '{}/{}'.format(FROMGITHUB_LOADBASE,within)
    elif toplevel.startswith('http'):
        base_uri = toplevel
    elif toplevel.startswith('github'):
        base_uri = generic_github_url(toplevel)
    elif toplevel.startswith('gitlab-cern'):
        base_uri = generic_gitlab_cern_url(toplevel)
    else:
        base_uri = 'file://' + os.path.abspath(toplevel) + '/'

    if not base_uri.endswith('/'):
        base_uri = base_uri + '/'

    def yamlloader(uri):
        if '__yadage__' in uri:
            d, path = uri.split('___yadage___')
            d = json.loads(d)
            uri = 'https://gitlab.cern.ch/api/v4/projects/{repo}/repository/files/{path}/raw?ref={ref}'.format(
                repo = urllib.parse.quote(d['repo'],safe=''),
                path = urllib.parse.quote(d['subpath']+path, safe=''),
                ref = urllib.parse.quote(d['ref'],safe='')
            ) 
        try:
            log.debug('trying to get uri %s',uri)
            if 'YADAGE_SCHEMA_LOAD_TOKEN' in os.environ:
                kwargs = {'headers': {'PRIVATE-TOKEN':os.environ['YADAGE_SCHEMA_LOAD_TOKEN']}}
            else:
                kwargs = None
            r = requests.get(uri,**kwargs)
            assert r.ok
            data = r.content
            return yaml.load(data)
        except:
            try:
                data = urlopen(uri).read()
                return yaml.load(data)
            except:
                log.exception('loading error: cannot find URI %s',uri)
                raise RuntimeError

    def load(source,load_as_ref):
        full_uri = '{}{}'.format(base_uri,source)
        log.debug('trying to load rel: %s full uri: %s base %s',source,full_uri,base_uri)
        if not load_as_ref:
            return jsonref.load_uri(full_uri, base_uri = base_uri, loader = yamlloader)
        else:
            return jsonref.JsonRef.replace_refs({'$ref':source}, base_uri = base_uri, loader = yamlloader)
    return load

def extend_with_defaults(data, schema_name, schemadir):
    schema, resolver = schema_and_refresolver(schema_name, schemadir)
    DefaultValidatingDraft4Validator(schema, resolver = resolver).validate(data)

@dialect('raw_with_defaults')
def raw_dialect(spec, specopts):
    load = loader(specopts['toplevel'])
    load_as_ref = specopts['load_as_ref']
    data = load(spec, load_as_ref)
    extend_with_defaults(data, specopts['schema_name'], specopts['schemadir'])
    return data

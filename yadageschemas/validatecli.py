#!/usr/bin/env python
import os
import click
import jsonschema
import logging
import yadageschemas
import json
from .utils import WithJsonRefEncoder


logging.basicConfig(level=logging.ERROR)
log = logging.getLogger(__name__)


@click.command()
@click.argument('workflow')
@click.option('--toplevel','-t',default='')
@click.option('--schemadir','-d', default='')
@click.option('--stdout', '-s', default=False, is_flag=True)
@click.option('--dialect', default = 'raw_with_defaults')
@click.option('--plugins', default = '')
@click.option('--load_as_ref', default = False)
def main(workflow, toplevel, schemadir, stdout, dialect,plugins,load_as_ref):
    if plugins:
        for p in plugins.split(','):
            import importlib
            importlib.import_module(p)
    rc = 3
    if not toplevel:
        toplevel = os.getcwd()
    if not schemadir:
        schemadir = yadageschemas.schemadir
    try:
        spec, specopts = workflow, {
            'toplevel': toplevel,
            'load_as_ref': load_as_ref,
            'schemadir': schemadir,
            'schema_name': 'yadage/workflow-schema'
        }
        validopts = {
            'schemadir': schemadir,
            'schema_name': 'yadage/workflow-schema'
        }

        data = yadageschemas.load(spec, specopts, validate = True, validopts = validopts, dialect = dialect)
        if stdout:
            print(json.dumps(data, cls=WithJsonRefEncoder))
        else:
            click.secho('workflow validates against schema', fg='green')
        rc = 0
    except jsonschema.exceptions.ValidationError as e:
        rc = 1
        log.exception(e)
        click.secho('workflow does not validate against schema', fg='red')
    except:
        rc = 2
        log.exception('hm')
        click.secho('this is not even wrong (non-ValidationError exception)', fg='red')

    if rc != 0:
        exc = click.exceptions.ClickException(
            click.style("validation failed", fg='red'))
        exc.exit_code = rc
        raise exc

if __name__ == '__main__':
    main()

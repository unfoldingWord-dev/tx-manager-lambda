# Method for handling the registration of conversion modules

from __future__ import print_function

from tx_manager.tx_manager import TxManager


def handle(event, context):
    try:
        # Get all params, both POST and GET and JSON from the request event
        module = {}
        if 'data' in event and isinstance(event['data'], dict):
            module = event['data']
        if 'body-json' in event and event['body-json'] and isinstance(event['body-json'], dict):
            module.update(event['body-json'])

        env_vars = {}
        if 'vars' in event and isinstance(event['vars'], dict):
            env_vars = event['vars']

        return TxManager(**env_vars).register_module(module)
    except Exception as e:
        print(e)
        raise Exception('Bad request: {0}'.format(e.message))

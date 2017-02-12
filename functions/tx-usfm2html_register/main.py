from __future__ import unicode_literals, print_function
import json
from lambda_handlers.register_module_handler import RegisterModuleHandler


def handle(event, context):
    """
    Called through API Gateway to register the usfm2html converter
    :param dict event:
    :param context:
    :return dict:
    """
    with open('module.json') as data_file:
        event['data'] = json.load(data_file)
    return RegisterModuleHandler().handle(event, context)

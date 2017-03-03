from __future__ import unicode_literals, print_function
import os
import json
from lambda_handlers.register_module_handler import RegisterModuleHandler


def handle(event, context):
    """
    Called through API Gateway to register the md2html converter
    :param dict event:
    :param context:
    :return dict:
    """
    json_file = os.path.join(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))), 'module.json')
    with open(json_file) as data_file:
        event['data'] = json.load(data_file)
    RegisterModuleHandler().handle(event, context)

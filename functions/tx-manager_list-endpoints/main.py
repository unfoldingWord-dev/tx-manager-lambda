# Method for handling the registration of conversion modules

from __future__ import print_function
import logging
from lambda_handlers.list_endpoints_handler import ListEndpointsHandler
from aws_tools.dynamodb_handler import DynamoDBHandler

logger = logging.getLogger()
logger.setLevel(logging.INFO)


# noinspection PyUnusedLocal
def handle(event, context):
    """
    Triggered by adding a file to the cdn.door43.org/temp S3 folder
    :param dict event:
    :param context:
    """
    global logger
    ListEndpointsHandler.handle_list_endpoints(event, context, DynamoDBHandler, logger)

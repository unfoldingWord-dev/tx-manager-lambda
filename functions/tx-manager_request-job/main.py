from __future__ import unicode_literals
import logging
from lambda_handlers.request_job_handler import RequestJobHandler
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
    RequestJobHandler.handle_request_job(event, context, DynamoDBHandler, logger)
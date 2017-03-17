from __future__ import unicode_literals, print_function
from lambda_handlers.convert_handler import ConvertHandler
from converters.md2html_converter import Md2HtmlConverter


def handle(event, context):
    """
    Called through API Gateway to convert a given archive from MD to HTML
    :param dict event:
    :param context:
    :return dict:
    """
    return ConvertHandler(Md2HtmlConverter).handle(event, context)

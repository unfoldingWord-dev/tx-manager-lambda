import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(f_name):
    return open(os.path.join(os.path.dirname(__file__), f_name)).read()

setup(
    name="tx-manager-lambda",
    version="0.2.3",
    package_dir={
        'client_callback': 'functions/client_callback',
        'client_webhook': 'functions/client_webhook',
        'convert_md2html': 'functions/convert_md2html',
        'convert_usfm2html': 'functions/convert_usfm2html',
        'door43_deploy': 'functions/door43_deploy',
        'list_endpoints': 'functions/list_endpoints',
        'register_module': 'functions/register_module',
        'request_job': 'functions/request_job',
        'start_job': 'functions/start_job'
    },
    packages=[
        'client_callback',
        'client_webhook',
        'convert_md2html',
        'convert_usfm2html',
        'door43_deploy',
        'list_endpoints',
        'register_module',
        'request_job',
        'start_job'
    ],
    author="unfoldingWord",
    author_email="unfoldingword.org",
    description="Lambda functions for tX Manager",
    license="MIT",
    keywords="tX manager lambda",
    url="https://github.org/unfoldingWord-dev/tx-manager-lambda",
    long_description=read('README.rst'),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    install_requires=[
        'tx-manager>=0.2,<0.3'
    ]
)

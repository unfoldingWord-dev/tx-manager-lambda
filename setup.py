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
    version="0.2.1",
    package_dir={
        'list-endpoints': 'functions/tx-manager_list-endpoints',
        'register-module': 'functions/tx-manager_register-module',
        'request-job': 'functions/tx-manager_request-job',
        'start-job': 'functions/tx-manager_start-job',
        'md2html-register': 'functions/tx-usfm2html_register',
        'md2html-convert': 'functions/tx-md2html_convert',
        'usfm2html-register': 'functions/tx-usfm2html_register',
        'usfm2html-convert': 'functions/tx-usfm2html_convert',
        'webhook': 'functions/client_webhook',
        'callback': 'functions/client_callback',
        'deploy': 'functions/door43_deploy'
    },
    packages=[
        'list-endpoints',
        'register-module',
        'request-job',
        'start-job',
        'md2html-register',
        'md2html-convert',
        'usfm2html-register',
        'usfm2html-convert',
        'webhook',
        'callback',
        'deploy'
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
        'tx-manager==0.2.1'
    ]
)

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
    package_dir={'list-endpoints': 'functions/tx-manager_list-endpoints',
                 'register-module': 'functions/tx-manager_register-module',
                 'request-job': 'functions/tx-manager_request-job',
                 'start-job': 'functions/tx-manager_start-job'},
    packages=['list-endpoints', 'register-module', 'request-job', 'start-job'],
    version="0.0.1",
    author="unfoldingWord",
    author_email="unfoldingword.org",
    description="Lambda functions for tX Manager",
    license="MIT",
    keywords="tX manager lambda",
    url="https://github.org/unfoldingWord-dev/tx-manager-lambda",
    long_description=read('README.rst'),
    classifiers=[],
    dependency_links=[
        'git+git://github.com/unfoldingWord-dev/tx-manager.git@develop#egg=tx-manager',
    ],
    install_requires=[
        'tx-manager'
    ]
)

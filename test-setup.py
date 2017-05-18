from setuptools import setup

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
    description="Unit test setup file.",
    license="MIT",
    keywords="tX manager lambda",
    url="https://github.org/unfoldingWord-dev/tx-manager-lambda",
    long_description='Unit test setup file',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    install_requires=[
        'tx-manager>=0.2,<0.3',
        'mock'  # travis reports syntax error in mock setup.cfg if we give version
    ],
    test_suite='tests'
)

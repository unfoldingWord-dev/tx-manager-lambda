from setuptools import setup

setup(
    name="tx-manager",
    package_dir={'list-endpoints': 'functions/tx-manager_list-endpoints',
                 'register-module': 'functions/tx-manager_register-module',
                 'request-job': 'functions/tx-manager_request-job',
                 'start-job': 'functions/tx-manager_start-job'},
    packages=['list-endpoints', 'register-module', 'request-job', 'start-job'],
    version="0.0.1",
    author="unfoldingWord",
    author_email="unfoldingword.org",
    description="Unit test setup file.",
    keywords="",
    url="https://github.org/unfoldingWord-dev/tx-manager",
    long_description='Unit test setup file',
    classifiers=[],
    dependency_links=[
        'git+git://github.com/unfoldingWord-dev/tx-manager.git@develop#egg=tx-manager',
    ],
    install_requires=[
        'tx-manager'
    ],
    test_suite='tests'
)

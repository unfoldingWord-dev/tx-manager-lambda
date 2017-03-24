master:

.. image:: https://travis-ci.org/unfoldingWord-dev/tx-manager-lambda.svg?branch=master
    :alt: Build Status
    :target: https://travis-ci.org/unfoldingWord-dev/tx-manager-lambda

.. image:: https://coveralls.io/repos/github/unfoldingWord-dev/tx-manager-lambda/badge.svg?branch=master
    :alt: Coveralls
    :target: https://coveralls.io/github/unfoldingWord-dev/tx-manager-lambda?branch=master

develop:

.. image:: https://travis-ci.org/unfoldingWord-dev/tx-manager-lambda.svg?branch=develop
    :alt: Build Status
    :target: https://travis-ci.org/unfoldingWord-dev/tx-manager-lambda

.. image:: https://coveralls.io/repos/github/unfoldingWord-dev/tx-manager-lambda/badge.svg?branch=develop
    :alt: Coveralls
    :target: https://coveralls.io/github/unfoldingWord-dev/tx-manager-lambda?branch=develop


tx-manager-lambda
=================

Lambda functions for tx Manager. Requires the [tx-manager library](https://github.com/unfoldingWord-dev/tx-manager).

Project description at https://github.com/unfoldingWord-dev/door43.org/wiki/tX-Development-Architecture#tx-manager-lambda-module.

Issue for its creation at https://github.com/unfoldingWord-dev/door43.org/issues/53


Setting up as deployed in virtual environment
=============================================

In IntelliJ terminal, switch to virtual environment and install requirements.

.. highlight:: bash
    source ~/venv/txml/bin/activate
    ./install-requirements.sh


Deploying your branch of tx-manager to AWS
==========================================
For developing the tx-manager library which this repo uses for every function, you can deploy your code to a test AWS
environment with apex by doing the following:

* Copy project.test.json.sample to project.test.json
* Edit project.test.json and change <username> and <branch> to your tx-manager branch
* Install apex from http://apex.run/#installation
* Set up your AWS credentials as specified at http://apex.run/#aws-credentials
* Run `apex deploy --env test` to deploy all functions, or `apex deploy --env test [function-name]` for a single function

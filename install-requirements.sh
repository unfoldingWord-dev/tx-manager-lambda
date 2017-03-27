#!/usr/bin/env bash
#
# Script to install requirements based on branch being processed by Travis CI
#
# If the branch is 'master' it will use the requirements.master.txt file which
# installs tx-manager from PyPI
#
# For all other branches, it will install the requirements in requirements.txt, 
# which includes downloading tx-manager from the GitHub develop branch
#

if [ $TRAVIS_BRANCH == "master" ]; then
  # Install tx-manager from PyPI and other requirements
  pip install -r requirements.master.txt
else
  # Install tx-manager from GitHub@develop and other requirements
  pip install -r requirements.txt
fi


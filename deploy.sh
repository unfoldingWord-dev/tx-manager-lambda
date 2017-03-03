#!/usr/bin/env bash
################################################################################
#
# The AWS environment variables will only be available when merging a
# pull request from develop into master due to travis security settings.
#
################################################################################

if [[ ${TRAVIS_EVENT_TYPE} == "push" && (${TRAVIS_BRANCH} == "master" || ${TRAVIS_BRANCH} == "develop") && ${TRAVIS_SECURE_ENV_VARS} == "true" ]]
then
    echo "Deploying..."
    eval export AWS_ACCESS_KEY_ID=\$${TRAVIS_BRANCH}_AWS_ACCESS_KEY_ID
    eval export AWS_SECRET_ACCESS_KEY=\$${TRAVIS_BRANCH}_AWS_SECRET_ACCESS_KEY
    eval export AWS_REGION=\$${TRAVIS_BRANCH}_AWS_REGION
    repoDir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
    thisDir="$( dirname "${repoDir}" )"
    "${thisDir}/apex" deploy -C "${repoDir}" --env ${TRAVIS_BRANCH}
else
    echo "Not deploying:"
    echo "  TRAVIS_EVENT_TYPE = $TRAVIS_EVENT_TYPE (must be 'push')"
    echo "  TRAVIS_BRANCH = $TRAVIS_BRANCH (must be 'master' or 'develop')"
    echo "  TRAVIS_SECURE_ENV_VARS = $TRAVIS_SECURE_ENV_VARS (must be 'true')"
fi

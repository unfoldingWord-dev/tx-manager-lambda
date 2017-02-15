#!/usr/bin/env bash

set -e

pip install --upgrade pip

for dir in `ls -d functions/*_*`
do
  echo ${dir}
  if [ -d ${dir} ];
  then
    pip install --upgrade git+git://github.com/unfoldingWord-dev/tx-manager.git@develop#egg=tx-manager -t ${dir}
  fi
done

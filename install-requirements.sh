#!/usr/bin/env bash

set -e

pip install --upgrade pip

for dir in `ls -d functions/*_*`
do
  echo ${dir}
  if [ -d ${dir} ];
  then
    pip install --upgrade git+git://git@github.com/unfoldingword-dev/tx-manager.git@develop#egg=tx-manager-0.2.1 -t ${dir}
  fi
done

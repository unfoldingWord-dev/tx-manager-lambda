#!/usr/bin/env bash

set -e

for dir in `ls -d functions/*_*`
do
  echo $dir
  if [ -d $dir ];
  then
    pip install --upgrade pip install git+ssh://git@github.com/unfoldingword-dev/tx-manager.git@develop -t $dir
  fi
done

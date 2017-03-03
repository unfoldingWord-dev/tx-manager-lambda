#!/usr/bin/env bash

THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PARENT_DIR="$( dirname "${THIS_DIR}" )"

LATEST=$(curl -s https://api.github.com/repos/apex/apex/tags | grep -Eo '"name":.*?[^\\]",'  | head -n 1 | sed 's/[," ]//g' | cut -d ':' -f 2)
URL="https://github.com/apex/apex/releases/download/${LATEST}/apex_linux_amd64"
DEST="${PARENT_DIR}/apex"

curl -sL ${URL} -o ${DEST}
chmod +x ${DEST}

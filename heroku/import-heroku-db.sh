#!/bin/bash
set -e

HEROKU_DIR=$(dirname $0)
source ${HEROKU_DIR}/env

python3 manage.py loaddata \
    ${HEROKU_DIR}/heroku.db.dump.json

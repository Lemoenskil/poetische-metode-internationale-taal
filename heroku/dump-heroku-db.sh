#!/bin/bash
set -e

HEROKU_DIR=$(dirname $0)
source ${HEROKU_DIR}/env

heroku run python3 manage.py dumpdata \
    --exclude auth.permission \
    --exclude contenttypes \
    >${HEROKU_DIR}/heroku.db.dump.json

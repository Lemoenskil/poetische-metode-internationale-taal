#!/bin/bash
set -e
set -x

HEROKU_DIR=$(dirname $0)
source ${HEROKU_DIR}/env
TOP_DIR=${HEROKU_DIR}/..
CURRENT_TIME=$(date "+%Y.%m.%d-%H.%M.%S")

cd ${TOP_DIR}
${HEROKU_DIR}/dump-heroku-db.sh
if [ -f "db.sqlite3" ]; then
	mv db.sqlite3 backups/db.${CURRENT_TIME}.sqlite3
fi
python3 manage.py migrate
${HEROKU_DIR}/import-heroku-db.sh

#!/bin/bash
# -*- coding: utf8 -*-
# Start up a postgres database for development.
PG_DIR="$HOME/.authcore"
PG_LOG="$PG_DIR/logfile"
PG_DATA_DIR="$PG_DIR/data"


ensure_pg() {
    [[ ! pg_ctl ]] && echo 'pg_ctl is not on your path. Ensure PostgreSQL is properly installed.' && exit 1
    [[ ! createuser ]] && echo 'createuser is not on your path. Ensure PostgreSQL is properly installed.' && exit 1
    [[ ! createdb ]] && echo 'createdb is not on your path. Ensure PostgreSQL is properly installed.' && exit 1
    [[ ! psql ]] && echo 'psql is not on your path. Ensure PostgreSQL is properly installed.' && exit 1
}


main() {
    # Kill any current dev setup.
    pg_ctl stop -D $PG_DATA_DIR &> /dev/null
    rm -rf $PG_DIR
    mkdir $PG_DIR

    # Boot everything up.
    pg_ctl initdb -s -D $PG_DATA_DIR -o "-A trust" || exit 1
    pg_ctl start -s -D $PG_DATA_DIR -l $PG_LOG || exit 1
    sleep 5

    # Create default users and databases.
    createuser -E authcoreadmin
    createdb -O authcoreadmin authcore
    psql -U $(whoami) makash -c "ALTER USER authcoreadmin WITH PASSWORD 'authcoreadmin'" > /dev/null
}

ensure_pg
main
echo "PostgreSQL listening on localhost:5432."

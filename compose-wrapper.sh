#!/bin/bash
# -*- coding: utf8 -*-
# Wrap the docker-compose command line tool, and export any variables needed for development.
# It is expected that you will be using docker-machine with virtualbox. Deal with it.

[[ ! docker ]] && echo 'Ensure `docker` is on your PATH.' && exit 1
[[ ! docker-machine ]] && echo 'Ensure `docker-machine` is on your PATH.' && exit 1
[[ ! docker-compose ]] && echo 'Ensure `docker-compose` is on your PATH.' && exit 1
[[ ! VboxManage ]] && echo 'Ensure `VBoxManage` (virtualbox) is on your PATH.' && exit 1

# Ensure machine is created.
docker-machine inspect authcore &> /dev/null
MACHINE_EXISTS=$? # Last command executed.
if [ ! $MACHINE_EXISTS ]; then
    echo "Creating authcore machine."
    docker-machine create \
        -d virtualbox \
        --virtualbox-cpu-count "1" \
        --virtualbox-memory "1024" \
        --virtualbox-disk-size "5120" \
        authcore
fi

# Ensure machine is started and sourced.
docker-machine start authcore > /dev/null
eval $(docker-machine env authcore)
export AUTHCORE_BACKEND_HOST=$(docker-machine ip authcore)
echo "AUTHCORE_BACKEND_HOST=$AUTHCORE_BACKEND_HOST"

# Wrap compose. Pass any args provided directly to compose.
if [[ "$@" != '' ]]; then
    docker-compose $@
fi

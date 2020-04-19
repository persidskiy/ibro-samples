#!/bin/sh

set -e

if [ -z "$LE_FQDN" ] || [ -z "$LE_EMAIL" ]; then
    echo "LE_FQND and LE_EMAIL env variables are required"
    exit 1
fi

docker-compose -f docker-compose.yml -f docker-compose.prod.yml stop
docker-compose -f docker-compose.yml -f docker-compose.prod.yml rm
docker-compose -f docker-compose.yml -f docker-compose.prod.yml down
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up --build -d --remove-orphans

#!/bin/sh

set -e

if [ -z "$LE_FQDN" ] || [ -z "$LE_EMAIL" ] || [ -z "$CR_KEY" ]; then
    echo "LE_FQND, LE_EMAIL, CR_KEY env variables are required"
    exit 1
fi

echo "build"
docker-compose -f docker-stack.yml build

echo "login to docker registry"
docker login --username json_key --password $CR_KEY cr.yandex

echo "push"
docker-compose -f docker-stack.yml push

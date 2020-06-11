#!/bin/sh

set -e

cd /opt/ibro-samples
docker-compose pull 
docker-compose up -d

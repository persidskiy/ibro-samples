#!/bin/sh

cd /src

case $MODE in
"DEBUG")
    echo "starting in DEBUG mode"
    ls -la
    FLASK_APP=main.py FLASK_DEBUG=1 FLASK_ENV=development flask run -h 0.0.0.0 -p 8080
    ;;

"PRODUCTION")
    echo "starting in PRODUCTION mode with gunicorn"
    gunicorn -b 0.0.0.0:8080 main:app
    ;;
*)
    echo "env MODE=PRODUCTION|DEBUG is required"
    exit 1
esac

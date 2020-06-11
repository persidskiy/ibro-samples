#!/bin/sh


if [ -z "$APP_VERSION" ]; then 
echo "APP_VERSION is required"
exit 1
fi

cd /src

case $MODE in
"DEBUG")
    echo "starting ver:$APP_VERSION in DEBUG mode"
    FLASK_APP=main.py FLASK_DEBUG=1 FLASK_ENV=development flask run -h 0.0.0.0 -p 8080
    ;;

"PRODUCTION")
    echo "starting in ver:$APP_VERSION PRODUCTION mode with gunicorn"
    gunicorn -b 0.0.0.0:8080 main:app
    ;;
*)
    echo "env MODE=PRODUCTION|DEBUG is required"
    exit 1
esac

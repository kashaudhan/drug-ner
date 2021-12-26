#!/usr/bin/env bash
# start-server.sh
(cd drug_ner; gunicorn drug_ner.wsgi --user www-data --bind 0.0.0.0:8000 --timeout 600  --worker-class=gevent --worker-connections=1000 --workers=33 ) & nginx -g "daemon off;"
Ks
#!/bin/sh

uwsgi \
    --http 0.0.0.0:80 \
    --wsgi-file askcompany/wsgi.py \
    --reload-on-rss 200 \
    --post-buffering-bufsize 8192 \
    --die-on-term


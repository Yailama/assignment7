#!/bin/sh
# cgi wrapper for xcal2

    echo "Content-Type: text/plain"
    echo "X-Content-Type-Options: nosniff"
    echo ""
    ./xcal2 $QUERY_STRING

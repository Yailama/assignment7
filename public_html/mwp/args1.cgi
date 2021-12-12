#!/bin/sh
# args1.cgi
# demonstrates how a URL with a trailing ?string passes the
# string as $QUERY_STRING 

printf "Content-Type: text/plain\n\n"
echo "My name is $0"
echo "QUERY_STRING has the value: " $QUERY_STRING

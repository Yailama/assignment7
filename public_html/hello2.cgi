#!/bin/sh
# my second cgi program. Wow!

echo "Content-Type: text/html"
echo ""

echo "<html><body style='background-color:yellow; color:green'>"
echo "Hello from <b>"
hostname
echo "</b>";
echo "The local time here is <span style='color:blue'>"
date
echo "</span>"

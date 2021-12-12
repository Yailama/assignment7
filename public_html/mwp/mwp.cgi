#!/bin/sh
# cgi wrapper for xcal2
echo ""
echo "<!doctype html>"
echo "<html>"
echo "<head>"
echo "        <title>cities</title>"
echo "</head>"
echo "<body bgcolor='white'>"
echo "<b>A Web Page for cities</b>"
echo "<hr>"
echo "Customized Links for cities"
echo "<p>"
echo "<center>"
echo "<table border='1' cellpadding='5'>"

echo "$(./fl data/cities.fmt -d'|' data/$QUERY_STRING.tab)"


echo "</table>"
echo "</body>"
echo "</html>"

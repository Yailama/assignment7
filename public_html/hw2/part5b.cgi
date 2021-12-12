#!/bin/sh
#
# cgi program to test tt2ht3
#
	echo "Content-Type: text/html"
	echo ""
	echo "<html><body><table>"
	 ( cat tt2ht3_input  )| ./tt2ht3
	echo "</table></body></html>"

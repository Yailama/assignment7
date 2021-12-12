#!/bin/sh
# 
# add_item.cgi
# this script is called from ewp.html for the Add function
# it takes the specified items and creates a new record on the
# end of the named file in the data directory
#
        eval `./qryparse`               # receive form data
        DATAFILE=$pagename.tab          # $pagename set by qryparse


        if test ! -d data               # if no data directory
        then
                mkdir data              # try to make it
                if test $? -ne 0        # and check for errors
                then
                        echo "Cannot create data directory."
                        exit
                fi
        fi

        cd data
	rm $DATAFILE

        if test $? -eq 0
        then
		echo ""
                echo "<html>"
                echo "<head>"
                echo "<meta http-equiv='refresh' content='0;url=https://cscie26.dce.harvard.edu/~ama952/mwp/ewp.cgi' />"
                echo "</head>"
                echo "<body>"
                echo "Delition of $title was successful. Redirect back..."
                echo "</body>"
                echo "</html>"
        else
                echo ""
                echo "$DATAFILE does not exist"
        fi


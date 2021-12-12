#!/bin/sh
# cgi version for ewp

echo ""
echo "<!doctype html>"
echo "<html>"
echo "<head>"
echo "        <style type='text/css'>"
echo "                td.rj { text-align: right; }"
echo "			table.pages_table, table.pages_table th {"
echo "  			border-top: 1px solid black;"
echo "  			border-bottom: 1px solid black;"
echo " 				border-collapse: collapse;}"
echo "			table { width: 100%; }"
echo "        </style>"
echo ""
echo "        <title>My Web Page Designer</title>"
echo "</head>"
echo ""
echo "<body bgcolor='white'>"
echo "<center>"
echo "        <hr>"
echo "        <span style='color: blue; font-size: larger;'>"
echo "        My Web Page<br> Page Creator/Editor Tool<br>"
echo "        </span>"
echo "        <hr>"
echo "</center>"
echo "<p>"
set $(ls data | grep \.tab | tr '\r\n' ' ')
echo "<dt>"
echo "Use this page to create and edit customized web pages.  You can add"
echo "items to pages, edit items on pages, and delete items on pages.  "
echo "<hr><b>PAGES</b></dt>"
echo "<table class='pages_table'><tbody>"
if [ $# -gt 0 ]
then
	echo "<tr><th>FILE NAME</th><th>TITLE(S)</th><th></th></tr>"
fi

while [ $# -gt 0 ]
do
	FILENAME=$1
	FILENAME_NOTAB=$(echo $FILENAME | rev | cut -c 5- | rev)
	TITLE=$(./fl data/title.fmt -d'|' data/$FILENAME)
	echo "<tr><td><a href='view_page.cgi?pagename=$FILENAME_NOTAB'>$FILENAME</href></td>"
	echo "<td>$TITLE</td>"
	echo "<td><a href='delete_item.cgi?pagename=$FILENAME_NOTAB'>DELETE</href></td></tr>"
	shift
done

echo "</tbody></table>"
echo ""
echo "<!-- a def list allows for headers and indented blocks -->"
echo ""
echo "<dl>"
echo "<dt><b>Add/Edit an Item</b></dt>"
echo "        <dd>"
echo "        <p>"
echo "        Use this function to add new items to your web page or"
echo "        edit existing items.  Include"
echo "        the name of the page and all the details about the item."
echo "        When you are done, press the <b>update</b> button, and the"
echo "        new item will be added to the named web page.  If the"
echo "        page contains an item with the same title, that item"
echo "        will be replaced with the data you provide."
echo "        <p>"
echo "        <form action='add-edit_item.cgi' method='get'>"
echo "        <table border='0' cellpadding='2' cellspacing='0'>"
echo "        <tr>"
echo "           <td class='rj'>Page name:</td>"
echo "           <td><input type='text' name='pagename' size='20'></td>"
echo "        </tr>"
echo "        <tr>"
echo "           <td class='rj'>Item title:</td>"
echo "           <td><input type='text' name='title' size='20'></td>"
echo "        </tr>"
echo "        <tr>"
echo "           <td class='rj'>Title color:</td>"
echo "           <td><input type='text' name='titlecolor' size='20'></td>"
echo "        </tr>"
echo "        <tr>"
echo "           <td class='rj'>Description:</td>"
echo "           <td><input type='text' name='descrip' size='40'></td>"
echo "        </tr>"
echo "        <tr>"
echo "           <td class='rj'>URL:</td>"
echo "           <td><input type='text' name='url' size='40'></td>"
echo "        </tr>"
echo "        <tr>"
echo "           <td></td>"
echo "           <td><input type='submit' value=' update '></td>"
echo "        </tr>"
echo "        </table>"
echo "        </form>"
echo "        </dd>"
echo "<dt>"
echo "<hr>"
echo "</body>"
echo "</html>"
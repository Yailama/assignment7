#!/bin/sh
# page to retrieve quantity of outbond trains by given params
#since number of lines is limited and this is first web form,
#simpy hardcoded input"
echo "Content-Type: text/html"
echo ""

echo "<html><body style='background-color:blue color:white'>"
echo "<p>Choose line and day:<span style='color:red'></p>"

#hardcoded form
echo "<form method = 'GET' action =''>"
echo "<select name = 'lines': id = 'lines'>"
echo "<option value = 'fairmount'>FAIRMOUNT</option>"
echo "<option value = 'fitchburg'>FITCHBURG</option>"
echo "<option value = 'franklin'>FRANKLIN</option>"
echo "<option value = 'greenbush'>GREENBUSH</option>"
echo "<option value = 'haverhill'>HAVERHILL</option>"
echo "<option value = 'kingston'>KINGSTON</option>"
echo "<option value = 'lowell'>LOWELL</option>"
echo "<option value = 'middleborough'>MIDDLEBOROUGH</option>"
echo "<option value = 'needham'>NEEDHAM</option>"
echo "<option value = 'newburyport'>NEWBURYPORT</option>"
echo "<option value = 'providence'>PROVIDENCE</option>"
echo "<option value = 'worcester'>WORCESTER</option>"
echo "</select>"
echo "<p>Select days:</p>"
echo "<input type='radio' id='day1' name='day' value='m-f'>"
echo "<label for='age1'>Monday - Friday</label><br>"
echo "<input type='radio' id='day2' name='day' value='sa'>"
echo "<label for='age2'>Saturday</label><br>"
echo "<input type='radio' id='day3' name='day' value='su'>"
echo "<label for='age3'>Sunday</label><br><br>"
echo "<input type='submit' value='Submit'>"
echo "</form>"
echo "<div>Number of outbound trains for specified day and line:"

#parse form output into query
./qryparse > query.txt

#clean parsed query to form line <linevalue> day <dayvalue>
#and print output
eval "./count_outbound_trains" $(cat query.txt | tr ";\n=\'" " ")
echo "</div>"
echo "</body></html>"

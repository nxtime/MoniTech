#!/bin/bash
echo "content-type: text/html"
echo
cat main/main1.html
for x in $(cat rsimple.txt) ; do
	echo "<tr>"
	for y in $(echo $x) ; do
		NAME=$(echo $y | cut -d";" -f1)
		LOCL=$(echo $y | cut -d";" -f2)
		IPAS=$(echo $y | cut -d";" -f3)
		STAT=$(echo $y | cut -d";" -f4)
		echo "<td>$NAME</td>"
		echo "<td>$LOCL</td>"
		echo "<td>$IPAS</td>"
		echo "<td>$STAT</td>"
	done
	echo "</tr>"
done
cat main/main2.html

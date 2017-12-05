#!/bin/bash
IFS=$'\n'
echo "content-type: text/html"
echo
cat vequip/vequip1.html
for x in $(cat equips.csv) ; do
	echo "<tr>"
	for y in $(echo $x) ; do
		NAME=$(echo $y | cut -d";" -f1)
		LOCL=$(echo $y | cut -d";" -f2)
		USER=$(echo $y | cut -d";" -f3)
		IPAS=$(echo $y | cut -d";" -f4)
		echo "<td>$NAME</td>"
		echo "<td>$LOCL</td>"
		echo "<td>$USER</td>"
		echo "<td>$IPAS</td>"
	done
	echo "</tr>"
done
cat vequip/vequip2.html

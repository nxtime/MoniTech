#!/bin/bash

read VAR

echo "content-type: text/html"
echo

IP=$(echo $VAR | cut -d"&" -f1 | cut -d"=" -f2)
CIP=$(echo $VAR | cut -d"&" -f2 | cut -d"=" -f2)

echo "<script lang='javascript'>"
if [[ $IP == $CIP ]] ; then
	sed "/;$IP$/d" equips.csv
	echo "$(date);$IP;REMOVED" >> /usr/lib/cgi-bin/log/equip.txt
	echo "alert('Equipamento removido.')"
	echo "location.href='../index.html'"
else
	echo "alert('Campos não coincidem-se.')"
	echo "location.href='../index.html'"
fi
echo "</script>"

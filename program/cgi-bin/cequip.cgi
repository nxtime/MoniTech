#!/bin/bash

read VAR

echo "content-type: text/html"
echo

TYPE=$(echo $VAR | cut -d"&" -f1 | cut -d"=" -f2)
IP=$(echo $VAR | cut -d"&" -f2 | cut -d"=" -f2)
INF=$(echo $VAR | cut -d"&" -f3 | cut -d"=" -f2)
CINF=$(echo $VAR | cut -d"&" -f4 | cut -d"=" -f2)
CIP=$(grep "^$IP;" equips.csv | cut -d";" -f3)
F1=$(grep "^$IP;" equips.csv | cut -d";" -f1)
F2=$(grep "^$IP;" equips.csv | cut -d";" -f2)
F3=$(grep "^$IP;" equips.csv | cut -d";" -f3)

if [[ $IP == $CIP ]] ; then
	if [[ $INF != "" ]] ; then
		if [[ $INF == $CINF ]] ; then
			if [[ $TYPE == "name" ]] ; then
				sed -i "/^$IP;/ s/^$F1;/$INF;/g" equips.csv > equips.new
				mv equips.new equips.csv
				echo "$(date);$IP;$TYPE;CHANGED" >> /usr/lib/cgi-bin/log/equip.txt
				echo "alert('Equipamento alterado.');"
				echo "location.href='../index.html'"
			elif [[ $TYPE == "local" ]] ; then
				sed -i "/^$IP;/ s/;$F2;/;$INF;/g" equips.csv > equips.new
				mv equips.new equips.csv
				echo "$(date);$IP;$TYPE;CHANGED" >> /usr/lib/cgi-bin/log/equip.txt
				echo "alert('Equipamento alterado.');"
				echo "location.href='../index.html'"
			elif [[ $TYPE == "ip" ]] ; then
				sed -i "/^$IP;/ s/;$F3$/;$INF/g" equips.csv > equips.new
				mv equips.new equips.csv
				echo "$(date);$IP;$TYPE;CHANGED" >> /usr/lib/cgi-bin/log/equip.txt
				echo "alert('Equipamento alterado.');"
				echo "location.href='../index.html'"
			fi
		fi
	fi
else
	echo "alert('Campos não coincidem-se');"
	echo "location.href='../index.html'"
fi

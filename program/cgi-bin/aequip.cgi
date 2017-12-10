#!/bin/bash

read VAR

echo "content-type: text/html"
echo

urldecode(){
	echo -e $(sed 's/%/\\x/g')
}

EQUIP=$(echo $VAR | cut -d"&" -f1 | cut -d"=" -f2 | tr + ' ' | urldecode)
LOCAL=$(echo $VAR | cut -d"&" -f2 | cut -d"=" -f2 | tr + ' ' | urldecode)
IP=$(echo $VAR | cut -d"&" -f3 | cut -d"=" -f2)
CIP=$(echo $VAR | cut -d"&" -f4 | cut -d"=" -f2)

echo "<script lang=javascript>"
grep "^$EQUIP;" equips.csv> /dev/null
if [[ $? != "0" ]] ; then
	if [[ $EQUIP != "" ]] ; then
		if [[ $LOCAL != "" ]] ; then
			if [[ $IP != "" ]] ; then
				if [[ $CIP != "" ]] ; then
					if [[ $IP == $CIP ]] ; then
						echo "$EQUIP;$LOCAL;$IP" >> equips.csv
						echo "$(date);$EQUIP;ADD" >> log/equip.txt
						echo "alert('Equipamento adicionado.')"
						echo "location.href='../index.html'"
					fi
				fi
			fi
		fi
	fi
else
	echo "alert('Campos não coincidem-se.')"
	echo "location.href='../index.html'"
fi
echo "</script>"

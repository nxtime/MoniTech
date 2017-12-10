#!/bin/bash
read EQUIP
echo "content-type: text/html"
echo
urldecode(){ echo -e $(sed '/s/%/\\x/g') ;}
EQUIP=$(echo $EQUIP | urldecode | tr + ' ')
NAME=$(echo $EQUIP | cut -d"&" -f1 | cut -d"=" -f2)
LOCL=$(echo $EQUIP | cut -d"&" -f2 | cut -d"=" -f2)
USER=$(echo $EQUIP | cut -d"&" -f3 | cut -d"=" -f2)
IPAS=$(echo $EQUIP | cut -d"&" -f4 | cut -d"=" -f2)
CIPA=$(grep ";$IPAS$" equips.csv)
if [[ $IPAS = $CIPA ]] ; then
	echo "$NAME;$LOCL;$USER;$IPAS" >> equips.csv
	echo "<h1>Deu Certo</h1>"
else
	echo "<h1>Equipamento não existente.</h1>"
fi

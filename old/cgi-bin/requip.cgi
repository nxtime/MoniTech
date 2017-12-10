#!/bin/bash
read EQUIP
echo "content-type: text/html"
echo
IPAS=$(echo $EQUIP | cut -d"=" -f2)
CIPA=$(grep ";$IPAS$" equips.csv)
if [[ $IPAS == $CIPA ]] ; then
	sed "/;$IPAS$/d" equips.csv > equips.csv
	echo "<h1>Deu certo</h1>"
else
	echo "<h1>Equipamento não existente</h1>"
fi

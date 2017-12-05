#!/bin/bash
read POST
echo "content-type: text/html"
echo
IP=$REMOTE_ADDR
STATE=$(grep $IP login.txt | cut -d";" -f6)
TYPE=$(grep $IP login.txt | cut -d";" -f4)
REDIRECT=$(echo $POST | cut -d"=" -f2)
REDIRECT=$(echo $REDIRECT | sed "s/%2F/\//g")
PPT="/var/www/html/pages/index.html"
if [[ $REDIRECT != "" ]];then
	cat $REDIRECT
	PPT=""
else
	break
fi
grep $IP login.txt > /dev/null
if [[ $? == 0 ]]; then
	if [[ $STATE == "logado" ]]; then
		if [[ $TYPE == "tecnico" ]]; then
			cat $PPT
		else
			cat $PPT
		fi
	else
		cat /var/www/html/pages/login.html
	fi
else
	cat /var/www/html/pages/login.html
fi	

#!/bin/bash
echo "content-type: text/html"
echo
IP=$REMOTE_ADDR
STATE=$(grep $IP login.txt | cut -d";" -f5)
grep $IP login.txt > /dev/null
if [[ $? == 0 ]]; then
	if [[ $STATE == "logado" ]]; then
		break3
	else
		cat /var/www/html/pages/login.html
	fi
else
	cat /var/www/html/pages/login.html
fi	

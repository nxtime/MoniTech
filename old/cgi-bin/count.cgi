#!/bin/bash
echo "content-type: text/html"
echo
TYPE=$(grep $REMOTE_ADDR login.txt | cut -d";" -f4)
STATE=$(grep $REMOTE_ADDR login.txt | cut -d";" -f5)
grep $REMOTE_ADDR login.txt >> /dev/null
if [[ $? == 0 ]]; then
	if [[ $STATE == "logado" ]]; then
		if [[ $TYPE == "tecnico" ]]; then
			cat /var/www/html/pages/index.html
		else
			cat /var/www/html/pages/index.html
		fi
	else
		cat /var/www/html/pages/login.html
	fi
else
	cat /var/www/html/pages/login.html
fi

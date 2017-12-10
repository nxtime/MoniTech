#!/bin/bash

read VAR

echo "content-type: text/html"
echo

IP=$REMOTE_ADDR
USER=$(echo "$VAR" | cut -d"&" -f1 | cut -d"=" -f2)
PASS=$(echo "$VAR" | cut -d"&" -f2 | cut -d"=" -f2 | sha256sum | cut -d" " -f1)
CUSER=$(grep "^$USER;" users.csv | cut -d";" -f1)
CPASS=$(grep "^$USER;" users.csv | cut -d";" -f2)

echo "<script lang=javascript>"
if [[ $USER == $CUSER ]] ; then
	if [[ $PASS == $CPASS ]] ; then
		sed -i "/^$USER;/ s/nlogged/logged/g" users.csv > users.new
		mv users.new users.csv
		sed -i "/^$USER;/ s/IP/$IP/g" users.csv > users.new
		mv users.new users.csv
		echo "$(date);$USER;ON" >> /usr/lib/cgi-bin/log/login.txt
		echo "location.href='../index.html';"
	else
		echo "alert('Usuário/senha incorreto, por favor tente novamente.');"
		echo "location.href='../index.html'"
	fi
else
	echo "alert('Usuário/senha incorreto, por favor tente novamente.');"
	echo "location.href='../index.html'"
fi
echo "</script>"

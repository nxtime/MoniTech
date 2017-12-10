#!/bin/bash

read VAR

echo "content-type: text/html"
echo

USER=$(echo $VAR | cut -d"&" -f1 | cut -d"=" -f2)
CUSER=$(echo $VAR | cut -d"&" -f2 | cut -d"=" -f2)

echo "<script lang='javascript'>"
if [[ $USER == $CUSER ]] ; then
	sed "/^$USER;/d" users.csv
	echo "$(date);$USER;REMOVED" >> /usr/lib/cgi-bin/log/user.txt
	echo "alert('Usuário removido.')"
	echo "location.href='../index.html'"
else
fi
echo "</script>"

#!/bin/bash

read VAR

echo "content-type: text/html"
echo

urldecode (){
	echo -e $(sed 's/%/\\x/g')
}

TYPE=$(echo $VAR | cut -d"&" -f1 | cut -d"=" -f2)
USER=$(echo $VAR | cut -d"&" -f2 | cut -d"=" -f2)
PASS=$(echo $VAR | cut -d"&" -f3 | cut -d"=" -f2 | sha256sum | cut -d" " -f1)
CPASS=$(echo $VAR | cut -d"&" -f4 | cut -d"=" -f2 | sha256sum | cut -d" " -f1)
EMAILA=$(echo $VAR | cut -d"&" -f5 | cut -d"=" -f2 | tr + ' ' | urldecode)
CEMAILA=$(echo $VAR | cut -d"&" -f6 | cut -d"=" -f2 | tr + ' ' | urldecode)

echo "<script lang=javascript>"
grep "^$USER;" users.csv> /dev/null
[[ $? != "0" ]] && [[ $TYPE != "" ]] && [[ $USER != "" ]] && [[ $PASS != "" ]] && [[ $CPASS != "" ]] && [[ $EMAILA != "" ]] && [[ $CEMAILA != "" ]] && [[ $PASS == $CPASS ]] && [[ $EMAILA == $CEMAILA ]] && echo "$USER;$PASS;$EMAILA;$TYPE;IP;nlogged" >> users.csv && echo "$(date);$USER;ADDED" >> log/user.txt && echo "alert('Usuário adicionado.');" && echo "location.href='../index.html'" || echo "alert('Campos não coincidem-se.');" ; echo "location.href='../index.html'"
echo "</script>"

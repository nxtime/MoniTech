#!/bin/bash
read POST
IP=$REMOTE_ADDR
USER=$(echo $POST | cut -d"&" -f1 | cut -d"=" -f2)
PASS=$(echo $POST | cut -d"&" -f2 | cut -d"=" -f2)
PASS=$(echo $PASS | sha256sum | cut -d" " -f1)
CUSER=$(grep "$USER;" login.txt | cut -d";" -f1)
CIP=$(grep "$USER;" login.txt | cut -d";" -f4)
CPASS=$(grep "$USER;" login.txt | cut -d";" -f2)
CSTATE=$(grep "$USER;" login.txt | cut -d";" -f5)
				echo "content-type: text/html"
echo
echo "<head lang='pt-br'>"
	echo "<meta charset='utf-8'>"
	echo "<script lang='javascript'>"
if [[ $USER == $CUSER ]]; then
	if [[ $PASS == $CPASS ]]; then
			sed -ie "/$USER;/s/IP/$IP/" login.txt
			sed -ie "/$USER;/s/deslogado/logado/" login.txt 	
				echo "location.href='../index.html';"
	else
			echo "alert('Senha incorreta, por favor tente novamente');"
			echo "location.href='../index.html';"
	fi
else
			echo "alert('Usuário incorreto, por favor tente novamente');"
			echo "location.href='../index.html';"
fi
	echo "</script>"
echo "</head>"

#!/bin/bash
read POST
echo "content-type: text/html"
echo
TYPE=$(echo $POST | cut -d"&" -f1 | cut -d"=" -f2)
USER=$(echo $POST | cut -d"&" -f2 | cut -d"=" -f2)
EMAIL=$(echo $POST | cut -d"&" -f3 | cut -d"=" -f2)
EMAIL=$(echo $EMAIL | sed "s/%40/@/g")
CEMAIL=$(echo $POST | cut -d"&" -f4 | cut -d"=" -f2)
CEMAIL=$(echo $CEMAIL | sed "s/%40/@/g")
PASS=$(echo $POST | cut -d"&" -f5 | cut -d"=" -f2)
CPASS=$(echo $POST | cut -d"&" -f6 | cut -d"=" -f2)
CADASTRAR="echo <meta http-equiv='refresh' content='0;url=./cadastro.cgi'>"
echo "<head>"
echo "<meta charset='utf-8'>"
echo "$POST"
if [[ $TYPE != "" ]]; then
	grep "$USER;" login.txt > /dev/null
	if [[ $? != 0 ]]; then
		grep "$EMAIL;" login.txt > /dev/null
		if [[ $? != 0 ]]; then
			if [[ $EMAIL == $CEMAIL ]]; then
				if [[ $PASS == $CPASS ]]; then
					echo "passou"
					PASS=$(echo $PASS | sha256sum | cut -d" " -f1)
					echo "$USER;$PASS;$EMAIL;$TYPE;IP;deslogado" >> login.txt
					echo "<meta http-equiv='refresh' content='0;url=../index.html'>"
				else
					echo "<script>"
					echo "alert('Desculpe, tente novamente as senhas não se coincidem');"
					echo "</script>"
					$CADASTRAR
				fi
			else
				echo "<script>"
				echo "alert('Desculpe, tente novamente os emails não se coincidem');"
				echo "</script>"
				$CADASTRAR
			fi
		else	
			echo "<script>"
			echo "alert('Desculpe, tente novamente esse email já foi cadastrado');"
			echo "</script>"
			$CADASTRAR
		fi
	else
		echo "<script>"
		echo "alert('Desculpe, tente novamente esse usuário) já foi cadastrado');"
		echo "</script>"
		$CADASTRAR
	fi
else
	echo "<script>"
	echo "alert('Por favor, informe um tipo de usuário');"
	echo "</script>"
	$CADASTRAR
fi
echo "</head>"

#!/bin/bash

read VAR

echo "content-type: text/html"
echo

VAR=$(echo $VAR | cut -d"=" -f2)

echo "<html>"
echo "<head>"
echo "</head>"
echo "<body>"
echo "<script lang='javascript'>"
case $VAR in
	Iniciar)
		while : ; do
			ping.cgi &
			echo "$!"> /usr/lib/cgi-bin/log/pid.txt
		done
		echo "alert('Monitoramento iniciado.');"
		echo "location.href='../index.html'"
		;;
	Encerrar)
		kill -9 $(cat /usr/lib/cgi-bin/log/pid.txt)
		rm -rf /usr/lib/cgi-bin/log/pid.txt
		echo "alert('Monitoramento encerrado.');"
		echo "location.href='../index.html'"
		;;
	Reiniciar)
		$0 Encerrar
		$0 Iniciar
		;;
	Status)
		if [ -e /usr/lib/cgi-bin/log/pid.txt ] ; then
			echo "alert('Monitoramento está em funcionamento. PID=$(cat /usr/lib/cgi-bin/log/pid.txt)')"
			echo "location.href='../index.html'"
		else
			echo "alert('Monitoramento está desligado.')"
			echo "location.href='../index.html'"
		fi
		;;
esac
echo "</script>"
echo "</body>"
echo "</html>"

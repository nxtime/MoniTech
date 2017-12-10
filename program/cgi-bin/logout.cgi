#!/bin/bash

echo "content-type: text/html"
echo

IP=$REMOTE_ADDR

sed -i "/;$IP;/ s/logged/nlogged/g" users.csv > users.new
mv users.new users.csv
sed -i "/;$IP;/ s/$IP/IP/g" users.csv > users.new
mv users.new users.csv

if [[ $? == '0' ]] ; then
	echo "<script lang=javascript>"
	echo "alert ('Deslogando...');"
	echo "location.href='../index.html'"
	echo "</script>"
fi

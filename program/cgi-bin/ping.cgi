#!/bin/bash

echo "content-type: text/html"
echo

IP=$REMOTE_ADDR

echo ""> rsimple.txt
for name in $(cat equips.csv | cut -d";" -f1) ; do
	for ip in $(grep "^$name;" equips.csv | cut -d";" -f3) ; do
		ping -W 1 -c 1 -i 1 $ip &> /dev/null
		local=$(grep "^$name;" equips.csv | cut -d";" -f2)
		if [[ $? == "0" ]] ; then
			echo "$(date);$name;$local;$ip;UP" >> log/rdetails.txt
			echo "$name;$local;$ip;UP" >> log/rsimple.txt
		else
			echo "$(date);$name;$local;$ip;DOWN" >> log/rdetails.txt
			echo "$name;$local;$ip;DOWN" >> log/rsimple.txt
		fi
	done
done

#!/bin/bash
echo "content-type: text/html"
echo
IP=$REMOTE_ADDR
sed -ie "/$IP/s/logado/deslogado/" login.txt
sed -ie "/$IP/s/$IP/IP/" login.txt
echo "<script>alert('Deslogando...');location.href='../index.html';</script>"

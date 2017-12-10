#!/bin/bash
remove(){
	echo "Aguarde enquanto os programas são removidos..."
	apt-get remove apache2 --purge -y &> /dev/null
	apt-get remove sendemail --purge -y &> /dev/null
	apt-get purge apache2 -y &> /dev/null
	apt-get purge sendemail -y &> /dev/null
	apt-get autoremove -y &> /dev/null
	rm -rf /var/www/html/*
	rm -rf /usr/lib/cgi-bin/*
	read -p "Programa desinstalado. Pressione [ENTER] para sair."
	exit 0
}
echo Este desinstalador removerá os seguintes programas:
echo - apache2
echo - sendemail
echo - MoniTech
echo E excluirá todo o conteúdo das pastas:
echo - /var/www/html
echo - /usr/lib/cgi-bin
echo
read -p "Deseja continuar com desinstalação?" OPTION
case $OPTION in
	[Ss][Ii][Mm]|[Ss]|[Yy][Ee][Ss]|[Yy]) remove ;;
	[Nn][Ãã][Oo]|[Nn][Aa][Oo]|[Nn][Oo]|[Nn]) clear ; exit 0 ;;
	*) read -p "Opção inválida. Pressione [ENTER] para sair." ;;
esac
